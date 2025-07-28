# 🛠️ Autonomous Code Generation & Edit

**An intelligent CLI assistant that bridges natural language and code through AI-powered automation**

Transform your development workflow with an interactive command-line tool that understands your intent and manipulates code files autonomously using Google's Gemini AI.

## 🎯 What It Does

This tool serves as your personal coding assistant, capable of:

| Feature | Description |
|---------|-------------|
| **🤖 AI Code Generation** | Convert natural language instructions into working code |
| **📖 File Reading** | Display file contents directly in your terminal |
| **✂️ Smart Editing** | Remove specific lines or code snippets with precision |
| **🗑️ Safe Deletion** | Delete files with confirmation prompts |
| **💾 File Management** | Create new files or append to existing ones |
| **🔍 Syntax Validation** | Automatically test generated code for errors |

## 🚀 Quick Start

### Requirements
- **Python 3.7+**
- **Google API Key** for Gemini access

### Setup

1. **Get the code**
   ```bash
   git clone https://github.com/your-username/autonomous-code-generation-edit.git
   cd autonomous-code-generation-edit
   ```

2. **Install dependencies**
   ```bash
   pip install langchain-google-genai langchain-core
   ```

3. **Configure API access**
   
   Replace the placeholder in the code with your actual Google API key:
   ```python
   os.environ["GOOGLE_API_KEY"] = "your-actual-api-key-here"
   ```

4. **Launch the assistant**
   ```bash
   python main.py
   ```

## 📋 Command Reference

### File Operations
```bash
# View file contents
read filename.py

# Remove specific lines
remove filename.py lines 5-10

# Remove code containing specific text
remove filename.py "import pandas"

# Delete a file (with confirmation)
delete old_script.py
```

### AI Interactions
Simply type any coding instruction in natural language:
```bash
>> Create a function to sort a list of dictionaries by a specific key
>> Write a class for handling API requests with error handling
>> Generate a script to read CSV files and calculate averages
```

### Control Commands
```bash
exit    # Quit the application
```

## 🔧 Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   User Input    │───▶│  AI Engine   │───▶│ File System │
│  (Natural Lang) │    │  (Gemini)    │    │   Handler   │
└─────────────────┘    └──────────────┘    └─────────────┘
         │                       │                  │
         └───────────────────────┼──────────────────┘
                                 ▼
                        ┌─────────────────┐
                        │ Syntax Checker  │
                        │   & Validator   │
                        └─────────────────┘
```

## 🎪 Example Session

```bash
Welcome to the Simple AI Code Tool!
Type your instruction (or 'exit' to quit):

>> Create a function to calculate fibonacci numbers

Generated code:
def fibonacci(n):
    if n > yes

Which file should I update? (e.g., my_script.py)
Filename: math_utils.py

Creating new file math_utils.py...
Code saved to math_utils.py.

Testing the updated file for syntax and runtime errors...
✅ Code ran successfully!
```

## ⚡ Pro Tips

- **Be specific** in your instructions for better code generation
- **Use descriptive filenames** to keep your projects organized  
- **Test regularly** - the tool automatically validates syntax after saving
- **Backup important files** before using remove/delete operations

## 🤝 Contributing

Found a bug or have a feature idea? We'd love your input!

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## 📜 License

Licensed under the MIT License - see [LICENSE](LICENSE) for details.

