import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate                        # ✅ new
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import glob
load_dotenv()


# 🔹 Shared embeddings
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# 🔹 Load documents


def load_documents():
    docs = []
    
    # ✅ Auto-loads all txt files
    for txt_file in glob.glob("data/*.txt"):
        docs.extend(TextLoader(txt_file, encoding="utf-8").load())
    
    # ✅ Auto-loads all pdf files
    for pdf_file in glob.glob("data/*.pdf"):
        docs.extend(PyPDFLoader(pdf_file).load())
    
    return docs


# 🔹 Create vector DB (RUN ONLY ONCE)
def create_vectorstore():
    documents = load_documents()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(texts, get_embeddings())
    vectorstore.save_local("vectorstore/faiss_index")
    print("✅ Vector DB created successfully!")


# 🔹 Load vector DB
def load_vectorstore():
    return FAISS.load_local(
        "vectorstore/faiss_index",
        get_embeddings(),
        allow_dangerous_deserialization=True
    )


# 🔹 QA Chain
def get_qa_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever()

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template("""
You are a friendly travel assistant for India. 

If the user says a greeting like "hi", "hello", "hey", "good morning" etc., 
reply warmly and ask how you can help with their travel plans.

Otherwise, answer based on the context below. 
Format your response clearly using:
- Bullet points for lists
- Separate lines for each item
- Bold headers for sections like Hotels, Transport, Places
- Include prices, timings and distances where available
- End with a helpful tip if possible

If the information is not in the context, say "I don't have details on that."

Context: {context}
Question: {question}
""")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # ✅ Simple LCEL chain (no langchain.chains needed)
    qa = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return qa