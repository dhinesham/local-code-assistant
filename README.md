# 🧠 Code Assistant Chatbot using CodeGemma + Gradio

A lightweight, real-time **coding assistant chatbot** built with [CodeGemma](https://ai.google.dev/gemma), powered by a local LLM server (e.g., [Ollama](https://ollama.ai/)) and an elegant frontend powered by [Gradio](https://www.gradio.app/). Designed for developers who want a local, privacy-preserving AI assistant that can generate and explain code on demand.

---


## 🚀 Features

* 🧠 **CodeGemma-powered** LLM backend for accurate and domain-specific coding support
* 🔁 **Streaming chat interface** for natural, incremental response generation
* 📜 **Maintains multi-turn conversation** (up to 3 turns for efficiency)
* 🧼 **Clear Chat button** to reset the conversation
* 🔐 **Runs locally** – no data goes to the cloud
* ⚡ **Minimal UI with Gradio** – ready to go in seconds!

---

## 📂 Project Structure

```bash
├── app.py             
├── requirements.txt   
```

---

## 🛠️ How It Works

### Backend Logic

* The function `chat_with_codegemma(message, chat_history)` constructs a prompt by appending the last `MAX_TURNS = 3` from chat history.
* It sends this prompt to a locally hosted LLM via a `POST` request to:

  ```
  http://localhost:11434/api/generate
  ```
* The model returns a **streamed response**, which is parsed token-by-token and displayed in real-time.
* Errors are gracefully caught and shown in the chat.

### Frontend (Gradio)

* The UI consists of:

  * Markdown header
  * Chatbox component
  * Text input field
  * Clear button
* Uses `gr.State` to store and update the conversation history dynamically.

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dhinesham/local-code-assistant.git
cd local-code-assistant
```

### 2. Install Dependencies

```bash
pip install gradio requests
```

### 3. Set Up CodeGemma Locally

You need a local model server that can serve the CodeGemma model. The easiest way is using [Ollama](https://ollama.ai/):

```bash
ollama run codegemma
```

> 📝 Make sure the model is listening on `http://localhost:11434`.

### 4. Run the App

```bash
python app.py
```

The app will launch in your browser at:
`http://localhost:7860`

---

## 📦 Configuration

Inside `app.py`, you can adjust the following:

| Variable     | Description                                      |
| ------------ | ------------------------------------------------ |
| `API_URL`    | URL of the CodeGemma model server                |
| `MODEL_NAME` | Name of the model (e.g., `codegemma`)            |
| `MAX_TURNS`  | Number of previous chat turns to keep in context |
| `MAX_TOKENS` | Max number of tokens to generate per reply       |

---

## ⚠️ Troubleshooting

* ❌ **Connection error**: Ensure that your local model server is up and running on `localhost:11434`.
* ❌ **CORS or JSON decode errors**: May occur due to malformed streaming responses. These are caught and displayed as error messages in the chat.
* 🧠 **Model doesn’t respond well?** Try adjusting the context or reducing turn length to avoid prompt overflow.

---

## 🧠 Learnings from the Project

* How to build conversational agents using local LLMs.
* Using **Gradio's `yield`** functionality for live response streaming.
* Managing **prompt context efficiently** in multi-turn chats.
* Real-time error handling for API-based language models.
* Developing an intuitive UI/UX with almost no frontend code.

---

## 🧩 Future Improvements

* Switchable models (dropdown)
* Token usage and latency display
* Syntax highlighting for code responses
* Save chat history locally or to a file
* Voice-to-text input using Whisper integration

---

## 🙌 Acknowledgements

* [Gradio](https://gradio.app/) for the effortless UI components
* [Ollama](https://ollama.ai/) for enabling local LLM hosting
* [CodeGemma](https://ai.google.dev/gemma) by Google for model capabilities

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Dhinesh A M**
📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/dhinesh-a-m-a0637234b/)

---
