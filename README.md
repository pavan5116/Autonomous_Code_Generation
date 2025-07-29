# Autonomous Code Generation and Edit

**An intelligent Python command-line tool designed for autonomous code generation, reading, editing, and deletion of files using AI.**

*🤖 Live Demo
*<img width="1915" height="1019" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/42bf03e9-6710-4613-9ec5-70911199bdff" />
*

## ✨ Key Features

This tool streamlines your development workflow with the following core functionalities:

-   **AI-Powered Code Generation**: Leverage the power of AI (e.g., Google Gemini) to interpret your natural language instructions and generate Python code snippets.
-   **File Creation & Appending**: Seamlessly create new Python files or append AI-generated code to existing ones.
-   **File Reading**: Easily display the content of any specified file directly within the terminal.
-   **Code Editing**: Precisely remove specific lines or code snippets from your files.
-   **Secure File Deletion**: Safely delete files from your project with a confirmation prompt to prevent accidental data loss.

## 🚀 Getting Started

Follow these steps to get your Autonomous Code Generation and Edit tool up and running:

### Prerequisites

Before you begin, ensure you have the following installed:

-   Python 3.x
-   `pip` (Python package installer)

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/autonomous-code-generation-edit.git
    cd autonomous-code-generation-edit
    ```
    (Replace `your-username` with your actual GitHub username and adjust the repository name if it differs.)

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *If you don't have a `requirements.txt` file, you'll need to create one. Based on your project's code, it should contain:*
    ```
    langchain-google-genai
    langchain-core
    # Add any other libraries your code uses, e.g., google-generativeai
    ```

3.  **Set Your Google API Key**:
    Obtain a Google API Key for Generative AI. It is highly recommended to set this as an environment variable rather than hardcoding it directly in your script for security.

    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
    (Replace `"YOUR_API_KEY_HERE"` with your actual API key.)

### Usage

To start the interactive tool, run:

```bash
python main.py
```
(Replace `main.py` with the actual name of your Python script if it's different.)

Follow the interactive prompts in your terminal. You can type instructions for the AI or use specific commands for file management.

### Command Examples

Here are some commands you can use within the tool:

-   **Generate Code**:
    Simply type your instruction, for example: `Write a Python function to calculate the factorial of a number.`
-   **Read a File**:
    ```
    read my_script.py
    ```
-   **Remove Lines from a File**:
    ```
    remove my_script.py lines 10-15
    ```
-   **Remove Code Snippet from a File**:
    ```
    remove my_script.py "import os"
    ```
-   **Delete a File**:
    ```
    delete old_file.txt
    ```
-   **Exit the Tool**:
    ```
    exit
    ```

## 📚 About the Project

This project originated from a desire for a minimalist, yet powerful, AI-driven development assistant. It focuses solely on the core functionalities of code generation and file manipulation, intentionally omitting features like extensive session history, linting, formatting, or external tool integrations to maintain a lean and efficient workflow. It's ideal for developers seeking a direct and uncomplicated AI coding companion.

## 📄 License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details.

[1] https://github.com/abhisheknaiidu/awesome-github-profile-readme
[2] https://dev.to/github/10-standout-github-profile-readmes-h2o
[3] https://github.com/matiassingers/awesome-readme
[4] https://www.reddit.com/r/github/comments/uulygm/what_are_some_really_nice_github_profile_readmes/
[5] https://www.hatica.io/blog/best-practices-for-github-readme/
[6] https://hackernoon.com/5-professional-tips-for-crafting-a-winning-readme
[7] https://eheidi.dev/tech-writing/20221212_documentation-101/
[8] https://dev.to/mfts/how-to-write-a-perfect-readme-for-your-github-project-59f2
[9] https://www.dhiwise.com/post/how-to-write-a-readme-that-stands-out-in-best-practices
[10] https://dev.to/radiomorillo/what-are-some-examples-of-open-source-projects-with-great-readmes-35gm
[11] https://coding-boot-camp.github.io/full-stack/github/professional-readme-guide/
[12] https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
[13] https://dev.to/github/how-to-create-the-perfect-readme-for-your-open-source-project-1k69
[14] https://github.com/othneildrew/Best-README-Template
[15] https://github.com/jehna/readme-best-practices
[16] https://www.reddit.com/r/opensource/comments/txl9zq/next_level_readme/
[17] https://www.youtube.com/watch?v=rCt9DatF63I
[18] https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
[19] https://www.makeareadme.com
[20] https://gprm.itsvg.in
