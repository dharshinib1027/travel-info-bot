from flask import Flask, render_template, request, jsonify
from rag_pipeline import create_vectorstore, get_qa_chain

app = Flask(__name__)

# 🔴 RUN ONLY FIRST TIME — uncomment, run once, then comment back
# create_vectorstore()

qa_chain = get_qa_chain()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_query = request.json["query"]

        # ✅ simple string input now
        response = qa_chain.invoke(user_query)

        return jsonify({"response": response})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"response": "⚠️ Error occurred. Please try again."})

if __name__ == "__main__":
    app.run(debug=True)