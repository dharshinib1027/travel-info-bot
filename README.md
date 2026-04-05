# 🌍 Travel & Transport RAG Bot

An AI-powered chatbot that provides **travel planning, transport information, and tourist guidance** using Retrieval-Augmented Generation (RAG).

This project combines **transport data + travel knowledge** to answer user queries intelligently.

---

## 🚀 Features

* 🧭 Travel itinerary generation (day-wise plans)
* 🚌 Transport details (bus, train, routes)
* 🌄 Tourist place recommendations
* 🏨 Hotel suggestions
* 💰 Budget estimation
* 📄 PDF/Text-based knowledge retrieval using RAG

---

## 🧠 Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* Google Gemini API (LLM)
* Flask (for UI integration)

---

## 📂 Project Structure

```bash
travel-rag-bot/
│
├── data/                 # Travel & transport data files
├── templates/            # HTML frontend
├── static/               # CSS & JS files
├── app.py                # Main Flask app
├── rag_pipeline.py       # RAG logic
├── requirements.txt      # Dependencies
├── .gitignore            # Ignored files
```

---

## ⚙️ How It Works

1. Load travel and transport documents
2. Split data into smaller chunks
3. Convert text into embeddings
4. Store embeddings in FAISS vector database
5. Retrieve relevant context based on query
6. Generate answers using Gemini LLM

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd travel-rag-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up API Key

Create a `.env` file and add:

```bash
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the application

```bash
python app.py
```

---

## 💬 Sample Queries

* “Best places to visit in Ooty”
* “Bus from Chennai to Madurai”
* “Plan a 2-day trip to Ooty”
* “Budget trip for Kodaikanal”
* “Hotels near Chennai beach”

---

## 📊 Use Case

This project can be used in:

* Travel assistant apps
* Tourism websites
* Smart AI chatbots
* Trip planning systems

---

## 🔥 Future Enhancements

* Add chat history (memory)
* Integrate weather API
* Add maps & navigation
* Voice-based chatbot
* Mobile app integration

---

## 🎯 Learning Outcomes

* Understanding RAG architecture
* Working with vector databases (FAISS)
* Prompt engineering
* Building AI-powered applications

---

## 👩‍💻 Author

**Dharshini B**
B.Tech Artificial Intelligence and Data Science

---

## ⭐ Acknowledgement

This project is developed for educational purposes to demonstrate the use of AI and RAG in real-world applications.

---


