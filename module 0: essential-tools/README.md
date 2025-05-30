# 🛠️ Module 0: Essential Tools Setup

Welcome to the first step! This module will help you set up all the essential tools you'll need.

## Table of Contents
1. [Setting Up Your Development Environment](#setting-up-your-development-environment)
2. [Introduction to VSCode](#introduction-to-vscode)
3. [Getting Started with Google Colab](#getting-started-with-google-colab)
4. [Basic Terminal Commands](#basic-terminal-commands)

## Setting Up Your Development Environment
### What is python? 
It is a high-level, versatile programming language known for its readability and simplicity. It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. What makes python great is the Open Source community around it and that it is free.

### Python Installation
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, make sure to check "Add Python to PATH"
3. Verify installation by opening a terminal and typing:
   ```bash
   python --version
   ```

### Virtual Environments
A virtual environment is an isolated Python environment that allows you to manage dependencies for different projects separately. This is crucial for AI development as different projects might require different versions of libraries.

#### Creating and Using Virtual Environments
```bash
# Create a new virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

# Your prompt should change to show the active environment
(myenv) $

# Deactivate when you're done
deactivate
```

#### Best Practices
- Create a new virtual environment for each project
- Always activate the environment before installing packages
- Keep a `requirements.txt` file to track dependencies:
  ```bash
  # Save dependencies
  pip freeze > requirements.txt
  
  # Install from requirements
  pip install -r requirements.txt
  ```

### Required Python Packages
Install essential packages using pip:

(Pip is a package manager for Python, used to install and manage Python packages. It simplifies the process of installing, upgrading, and managing external libraries.)

```bash
pip install numpy pandas scikit-learn
```

## Introduction to VSCode

### What is VScode?
[Visual Studio Code](https://code.visualstudio.com/) (VS Code) is a popular, free, and open-source code editor developed by Microsoft. It provides excellent support for Python development, making it a favorite choice among developers. It offers a great AI support known as [Copilot](https://code.visualstudio.com/docs/copilot/overview). Recently a new start-up created a fast growing code editor based on VScode that implements more and "better" AI models for coding, known as [Cursor](https://www.cursor.com/en).

### Installation
1. Download VSCode from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install recommended extensions:
   - Python (Microsoft)
   - Jupyter
   - GitLens
   - Python Indent
   - Pylance

### Key Features
- Integrated terminal
- Git integration
- Debugging tools
- Extensions marketplace
- IntelliSense

## Getting Started with Google Colab

### What is Google Colab?
Google Colab is a free cloud-based Jupyter notebook environment that requires no setup and runs entirely in the cloud.

### Getting Started
1. Visit [colab.research.google.com](https://colab.research.google.com)
2. Sign in with your Google account
3. Create a new notebook
4. Start coding!

### Key Features
- Free GPU/TPU access
- Pre-installed AI libraries
- Easy sharing and collaboration
- Integration with Google Drive

## Basic Terminal Commands
### What is Terminal:
A terminal, often referred to as a command line interface (CLI) or console, is a text-based interface used to interact with a computer system. Unlike graphical user interfaces (GUIs) which rely on visual elements like windows and buttons, terminals allow users to perform tasks by typing commands into a prompt. This method of interaction is highly efficient, flexible, and powerful, especially for programming, automating tasks, managing files, and handling data.

### Navigation
```bash
pwd          # Print working directory
ls           # List files and directories
cd           # Change directory
mkdir        # Make directory
```

### File Operations
```bash
touch        # Create empty file
cp           # Copy files
mv           # Move files
rm           # Remove files
```

### System Information
```bash
python --version    # Check Python version
pip list            # List installed packages
```

## Troubleshooting
- If you encounter any issues, check the [Python documentation](https://docs.python.org/)
- For VSCode issues, visit the [VSCode documentation](https://code.visualstudio.com/docs)
- For Colab issues, check the [Colab FAQ](https://research.google.com/colaboratory/faq.html)

## Additional Resources
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [VSCode Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [Colab Tutorial](https://colab.research.google.com/notebooks/intro.ipynb) 