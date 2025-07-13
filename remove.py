import re
import json
from langchain_google_genai import GoogleGenerativeAI as ai
from langchain.prompts import ChatPromptTemplate
import os
import subprocess



os.environ["GOOGLE_API_KEY"] = "your-Google-api-key"  # Or set as env variable

llm = ai(temperature=0, model="gemini-2.0-flash")

session_history = []

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
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Error running the code:")
        print(e.stderr)
        return False

def open_in_vscode(filename):
    try:
        subprocess.run(["code", filename])
        print(f"Opened {filename} in VS Code.")
    except Exception as e:
        print(f"Failed to open {filename} in VS Code: {e}")

def run_linter(filename):
    print("\nRunning flake8 linter...")
    result = subprocess.run(["flake8", filename], capture_output=True, text=True)
    if result.stdout:
        print("Linting issues found:\n", result.stdout)
    else:
        print("No linting issues found.")

def run_formatter(filename):
    print("\nFormatting code with black...")
    subprocess.run(["black", filename])
    print("Code formatted.")

print("Welcome to the Autonomous Code Generation Agent!")
print("Type your instruction (or 'exit' to quit, or 'history' to see session history):")


user_input = input(">> ").strip()

while user_input.lower() != 'exit':
    # --- Read and Review Feature ---
    if user_input.lower().startswith("read "):
        filename = user_input[5:].strip()
        if os.path.exists(filename):
            try:
                with open(filename, "r") as f:
                    content = f.read()
                print(f"\n--- Contents of {filename} ---\n")
                print(content)
                print("\n--- End of file ---\n")
            except Exception as e:
                print(f"❌ Could not read {filename}: {e}")
        else:
            print(f"❌ File {filename} does not exist.")
        user_input = input(">> ").strip()
        continue
    if user_input.lower().startswith("remove "):
        parts = user_input.split()
        if len(parts) >= 3:
            filename = parts[1]
            if not os.path.exists(filename):
                print(f"❌ File {filename} does not exist.")
                user_input = input(">> ").strip()
                continue
            try:
                with open(filename, "r") as f:
                    lines = f.readlines()
                # Remove by line numbers
                if "lines" in user_input:
                    match = re.search(r"lines\s+(\d+)-(\d+)", user_input)
                    if match:
                        start = int(match.group(1)) - 1  # zero-based index
                        end = int(match.group(2))  # exclusive
                        new_lines = lines[:start] + lines[end:]
                        with open(filename, "w") as f:
                            f.writelines(new_lines)
                        print(f"✅ Removed lines {start + 1}-{end} from {filename}.")
                    else:
                        print("❌ Please specify lines as: remove filename.py lines 10-15")
                # Remove by code snippet
                else:
                    # Extract everything after filename as the code snippet
                    code_snippet = user_input.split(filename, 1)[1].strip()
                    # Remove surrounding quotes if present
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
            except Exception as e:
                print(f"❌ Could not modify {filename}: {e}")
        else:
            print("❌ Usage: remove filename.py lines 10-15 OR remove filename.py \"code snippet\"")
        user_input = input(">> ").strip()
        continue
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
        #---history----
    if user_input.lower() == 'history':
        print("\nSession History:")
        for i, entry in enumerate(session_history, 1):
            print(f"{i}. Instruction: {entry['instruction']}")
            if entry["file"]:
                print(f"   → Code saved to: {entry['file']}")
            else:
                print("   → Code not saved.")
        print()
        user_input = input(">> ").strip()
        continue

    template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert software developer. just generate code Note: if u need to say something while in generating code just do commenting ur words with '#' or ('''ur words''')  "),
    ("human", "Interpret this software development instruction and describe the code changes needed:\n\n{instruction}\n\nResponse:")])

    instruction = input("Type your instruction: ")
    prompt = template.format_messages(instruction=instruction)
    result = llm.invoke(prompt)
    print("\nAgent interpretation:\n", result)
    # Ask if user wants to save the code to a file
    print("\nDo you want to add this code to a file? (yes/no)")
    save_choice = input(">> ").strip().lower()
    filename = None
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
        print(f"Summary: Added code to {filename}.\n")
        # --- Testing & Validation ---
        print("\nTesting the updated file for syntax and runtime errors...")
        check_syntax(filename)

        print("\nDo you want to format and lint this file? (format/lint/both/none)")
        style_choice = input(">> ").strip().lower()
        if style_choice == "format":
            run_formatter(filename)
        elif style_choice == "lint":
            run_linter(filename)
        elif style_choice == "both":
            run_formatter(filename)
            run_linter(filename)
        else:
            print("No code style action taken.")

        # --- Tool Integration Example ---
        print("\nDo you want to open this file in VS Code? (yes/no)")
        vscode_choice = input(">> ").strip().lower()
        if vscode_choice == "yes":
            open_in_vscode(filename)

        # --- README.md Update ---
        print("\nDo you want to update the README.md with this change? (yes/no)")
        readme_choice = input(">> ").strip().lower()
        if readme_choice == "yes":
            with open("README.md", "a") as readme:
                readme.write("\n## New Feature Added\n")
                readme.write(f"- {user_input}\n")
            print("README.md updated.")
        else:
            print("README.md not updated.")

    else:
        print("Code not saved.\n")

        # --- User Feedback Loop ---
    print("\nDid the agent's code or explanation solve your problem? (yes/no/request change)")
    feedback = input(">> ").strip().lower()
    if feedback == "yes":
        print("Great! Ready for your next instruction.")
    elif feedback in ["no", "request change"]:
        print("Please describe what needs to be changed or improved:")
        user_input = input(">> ").strip()
        session_history.append({
            "instruction": user_input,
            "code_generated": result,
            "file": filename if save_choice == "yes" else None,
            "feedback": feedback
        })
        continue
    else:
        print("Feedback not recognized. Continuing...")

    # Store session history
    session_history.append({
        "instruction": user_input,
        "code_generated": result,
        "file": filename if save_choice == "yes" else None,
        "feedback": feedback
    })

    print("Type your instruction (or 'exit' to quit, or 'history' to see session history):")
    user_input = input(">> ").strip()

# Save session history to a file at the end
with open("session_history.json", "w") as f:
    json.dump(session_history, f, indent=2)
print("Session history saved to session_history.json.")
print("Goodbye!")
