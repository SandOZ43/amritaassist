
Github:
git pull origin main      # Get latest from GitHub
# Do your work
git status                # Check changes
git add .                 # Stage all changes
git commit -m "Explain what you did"
git push origin main      # Push to GitHub

# 🖥️ Terminal Commands Cheatsheet for Daily Use

This cheatsheet collects **essential terminal commands** for daily work in your `amritaassist` project.

---

### 📁 Navigating the filesystem

✅ Go to a folder:
```bash
cd path/to/folder
```
✅ Go back one level:
```bash
cd ..
```
✅ Go to your home directory:

```bash
cd ~
```
✅ Show current directory:
```bash
pwd
```
---

### 📂 Listing contents

```bash
ls           # List files and folders
ls -la       # List all files (including hidden ones) with details
```

---

### 📄 Creating files and folders

✅ Create an empty file:
```bash
touch filename.py
```
✅ Create a folder:
```bash
mkdir foldername
```
---
### 🔨 File management commands

✅ Copy files:
```bash
cp source.txt destination.txt
```
✅ Copy entire folders:
```bash
cp -r source_folder/ destination_folder/
```
✅ Move (or rename) files:
```bash
mv oldname.txt newname.txt
mv file.txt target_folder/
```
✅ Delete files:
```bash
rm filename.txt
```
✅ Delete folders (recursively):
```bash
rm -r foldername
```
⚠️ **Be careful with `rm -r` — it deletes without sending to Trash!**

---

### 📝 Editing files
```bash
nano filename.py     # Open file in Nano editor (Ctrl+O to save, Ctrl+X to exit)
```
Or open in VS Code if installed:
```bash
code .               # Open current folder in VS Code
code filename.py     # Open a specific file in VS Code
```
---

### 🐍 Python and virtual environments

✅ Run Python script:
```bash
python3 filename.py
```
✅ Create virtual environment:
```bash
python3 -m venv venv
```
✅ Activate virtual environment:

* macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

✅ Deactivate virtual environment:

```bash
deactivate
```

---

### 🔧 Miscellaneous useful commands

✅ Clear terminal screen:
clear
```
✅ Show running processes:
top
```
✅ Show command history:
history
```


