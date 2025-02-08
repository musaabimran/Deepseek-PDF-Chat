# Deepseek PDF Chat

A application that enables users to upload PDF documents and ask questions about their content using LangChain and Ollama. The system utilizes embeddings and vector storage for efficient document retrieval and provides concise, context-aware answers.

## Features

- PDF document upload and processing
- Text chunking and embedding generation
- Semantic search for relevant context retrieval
- Question answering using the Deepseek language model
- Streamlit-based user interface

## Prerequisites

- Python 3.9+
- Ollama installed and running locally
- The Deepseek model downloaded in Ollama

## Installation

1. Clone the repository:

```bash
git clone https://github.com/musaabimran/Deepseek-PDF-Chat.git
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# On Windows use: .venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Dependencies

```
streamlit
pypdf
langchain
langchain-community
langchain-core
langchain-ollama
```

## Usage

1. Start the Ollama service and ensure the Deepseek model is available:

```bash
ollama run deepseek-r1:1.5b
```

2. Run the Streamlit application:

```bash
python -m streamlit run app.py --server.runOnSave true
```

3. Access the application in your web browser at `http://localhost:8501`
4. Upload a PDF document using the file uploader
5. Ask questions about the document content using the chat input

## Configuration

Key parameters can be adjusted in the `Config` class within `main.py`:

- `CHUNK_SIZE`: Size of text chunks (default: 1000)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 200)
- `MODEL_NAME`: Ollama model to use (default: "deepseek-r1:1.5b")
- `MAX_RETRIES`: Maximum retry attempts for operations (default: 3)
