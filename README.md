# Python CLI Chat Application

This project is a command-line interface (CLI) chat application that interacts with the Mistral 7B language model running locally via LM Studio (`localhost:1234`). It provides advanced features such as semantic search with FAISS, context retrieval, session memory, and chain-of-thought prompting, all orchestrated using [LangChain](https://python.langchain.com/).

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Running Mistral 7B with LM Studio](#running-mistral-7b-with-lm-studio)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Local LLM Integration:** Connects directly to a locally running Mistral 7B model via LM Studio's OpenAI-compatible API.
- **Semantic Search:** Uses FAISS vector store and HuggingFace embeddings to retrieve the most relevant context for each user query.
- **Session Memory:** Maintains conversation history for context-aware responses and multi-turn dialogue.
- **Chain of Thought:** Prompts the model to reason step-by-step, improving answer quality for complex queries.
- **LangChain Orchestration:** Utilizes LangChain for prompt management, context injection, and chaining logic.
- **Extensible Data Sources:** Easily ingest and index new documents for retrieval-augmented generation.

## Architecture

- **`chat.py`:** Main CLI loop, handles user input, context retrieval, and communication with the LLM.
- **FAISS Index:** Stores vectorized document chunks for fast semantic search.
- **Session Memory:** Keeps track of previous messages to provide conversational continuity.
- **Prompt Engineering:** Injects retrieved context and conversation history into prompts for the LLM.

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd python-cli-chat-app
   ```

2. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running Mistral 7B with LM Studio

1. **Download and install [LM Studio](https://lmstudio.ai/).**
2. **Download the Mistral 7B model** from within LM Studio.
3. **Start the LM Studio server:**
   - Go to the "Server" tab in LM Studio.
   - Start the OpenAI-compatible API server (default: `http://localhost:1234`).
   - Ensure the Mistral 7B model is loaded and active.

## Usage

1. **Start the chat application:**
   ```sh
   python src/chat.py
   ```

2. **Interact with the assistant:**
   - Type your questions or prompts.
   - The app will retrieve relevant context from indexed documents, maintain conversation history, and send a context-rich prompt to the Mistral 7B model.
   - Receive detailed, context-aware responses.

## How It Works

- **Document Ingestion:** Documents are embedded using HuggingFace models and indexed with FAISS for efficient retrieval.
- **Query Flow:**
  1. User enters a question.
  2. The app retrieves the top-k relevant document chunks using FAISS.
  3. The conversation history (session memory) and retrieved context are combined into a prompt.
  4. The prompt is sent to the Mistral 7B model via LM Studio's API.
  5. The model's response is displayed, and the conversation history is updated.
- **Chain of Thought:** Prompts encourage the model to reason step-by-step, improving accuracy and transparency.

## Extending the Application

- **Add Documents:** Place new `.txt` or supported files in the data directory and re-run the ingestion script to update the FAISS index.
- **Customize Prompts:** Modify the prompt templates in `chat.py` to adjust the assistant's behavior or persona.
- **Swap Embeddings/Models:** Easily switch to other HuggingFace embedding models or LLMs compatible with the OpenAI API.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.