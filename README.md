# Streamlit AI Chatbot





A minimalist and powerful AI chatbot built with Streamlit and Google Gemini. This project provides a clean web interface for real-time conversations with a state-of-the-art language model.

### 🤖 Live Demo

*<img width="1911" height="1021" alt="Screenshot 2025-07-29 203001" src="https://github.com/user-attachments/assets/d25645cb-4890-452a-9c73-e9e5c3e8f2b7" />
*



## Core Functionality

-   **Real-time Interaction**: Engage in dynamic, real-time conversations with Google's Gemini model.
-   **Intuitive UI**: A clean, responsive, and user-friendly interface powered by the Streamlit framework.
-   **Lightweight & Simple**: Minimal dependencies and straightforward code, making it easy to run and modify.
-   **Secure Configuration**: Designed to load your API key securely from environment variables.

## Technology Stack

This project leverages a modern stack for AI application development:

-   **Framework**: [Streamlit](https://streamlit.io/)
-   **Language Model**: Google Gemini (`gemini-2.0-flash`)
-   **LLM Orchestration**: [LangChain](https://www.langchain.com/)

## Getting Started

Follow these steps to get the chatbot running on your local machine.

### Prerequisites

-   Python 3.8 or newer
-   An active Google API Key with access to the Gemini model.

### 1. Clone the Repository

First, clone the project to your local machine:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

Install the required Python packages using pip:
```bash
pip install streamlit langchain-google-genai
```

### 3. Configure Your API Key

For security, the application loads your Google API Key from an environment variable.

**On macOS/Linux:**
```bash
export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

**On Windows:**
```powershell
$env:GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```
> **Note:** Remember to replace `"YOUR_API_KEY_HERE"` with your actual key. Do not commit your key directly into the source code.

### 4. Run the Application

Launch the Streamlit server:
```bash
streamlit run app.py
```
*(Replace `app.py` with the name of your Python script if it's different.)*

Your default web browser will open a new tab with the running chatbot application.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file in the repository for the full text.
