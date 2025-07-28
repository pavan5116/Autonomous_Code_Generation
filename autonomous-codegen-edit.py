import re
import os
import subprocess
from langchain_google_genai import GoogleGenerativeAI as ai
from langchain.prompts import ChatPromptTemplate

os.environ["GOOGLE_API_KEY"] = "AIzaSyD4D82n6QJqllwif14MojSQgEm1KnHa33s"  # insert your API key

llm = ai(temperature=0, model="gemini-2.0-flash")

def check_syntax(filename):
    try:
        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ Code ran successfully! Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ Error running the code:")
        print(e.stderr)

print("Welcome to the Simple AI Code Tool!")
print("Type your instruction (or 'exit' to quit):")

user_input = input(">> ").strip()

while user_input.lower() != 'exit':
    # --- Read Feature ---
    if user_input.lower().startswith("read "):
        filename = user_input[5:].strip()
        if os.path.exists(filename):
            with open(filename, "r") as f:
                content = f.read()
            print(f"\n--- Contents of {filename} ---\n")
            print(content)
        else:
            print(f"❌ File {filename} does not exist.")
        user_input = input(">> ").strip()
        continue

    # --- Remove Feature ---
    if user_input.lower().startswith("remove "):
        parts = user_input.split()
        if len(parts) >= 3:
            filename = parts[1]
            if not os.path.exists(filename):
                print(f"❌ File {filename} does not exist.")
                user_input = input(">> ").strip()
                continue
            with open(filename, "r") as f:
                lines = f.readlines()
            if "lines" in user_input:
                match = re.search(r"lines\s+(\d+)-(\d+)", user_input)
                if match:
                    start = int(match.group(1)) - 1
                    end = int(match.group(2))
                    new_lines = lines[:start] + lines[end:]
                    with open(filename, "w") as f:
                        f.writelines(new_lines)
                    print(f"✅ Removed lines {start + 1}-{end} from {filename}.")
                else:
                    print("❌ Please specify lines as: remove filename.py lines 10-15")
            else:
                code_snippet = user_input.split(filename, 1)[1].strip()
                if (code_snippet.startswith('"') and code_snippet.endswith('"')) or \
                        (code_snippet.startswith("'") and code_snippet.endswith("'")):
                    code_snippet = code_snippet[1:-1]
                if code_snippet:
                    new_lines = [line for line in lines if code_snippet not in line]
                    with open(filename, "w") as f:
                        f.writelines(new_lines)
                    print(f"✅ Removed lines containing '{code_snippet}' from {filename}.")
                else:
                    print("❌ Please specify the code to remove.")
        else:
            print("❌ Usage: remove filename.py lines 10-15 OR remove filename.py \"code snippet\"")
        user_input = input(">> ").strip()
        continue

    # --- Delete Feature ---
    if user_input.lower().startswith("delete "):
        filename = user_input[7:].strip()
        if os.path.exists(filename):
            print(f"Are you sure you want to delete {filename}? This cannot be undone! (yes/no)")
            confirm = input(">> ").strip().lower()
            if confirm == "yes":
                try:
                    os.remove(filename)
                    print(f"✅ Deleted {filename}.")
                except Exception as e:
                    print(f"❌ Could not delete {filename}: {e}")
            else:
                print("Deletion cancelled.")
        else:
            print(f"❌ File {filename} does not exist.")
        user_input = input(">> ").strip()
        continue

    # --- AI Code Generation ---
    template = ChatPromptTemplate.from_messages([
        ("system", "You are an expert software developer. Just generate code. If you need to say something, use Python comments (#) or triple quotes (''')."),
        ("human", "Interpret this instruction and generate code:\n\n{instruction}\n")
    ])
    instruction = user_input
    prompt = template.format_messages(instruction=instruction)
    result = llm.invoke(prompt)
    print("\nGenerated code:\n", result)
    print("\nDo you want to add this code to a file? (yes/no)")
    save_choice = input(">> ").strip().lower()
    if save_choice == "yes":
        print("Which file should I update? (e.g., my_script.py)")
        filename = input("Filename: ").strip()
        if os.path.exists(filename):
            print(f"Appending code to {filename}...")
            with open(filename, "a") as f:
                f.write("\n\n# --- Code added by AI agent ---\n")
                f.write(result)
        else:
            print(f"Creating new file {filename}...")
            with open(filename, "w") as f:
                f.write("# --- Code generated by AI agent ---\n")
                f.write(result)
        print(f"Code saved to {filename}.\n")
        print("Testing the updated file for syntax and runtime errors...")
        check_syntax(filename)
    else:
        print("Code not saved.\n")

    user_input = input(">> ").strip()
