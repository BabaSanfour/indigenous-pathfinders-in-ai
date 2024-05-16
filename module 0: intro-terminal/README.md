# intro-terminal

## Introduction to the use of terminals

### What is a terminal?
A terminal, often referred to as a command line interface (CLI) or console, is a text-based interface used to interact with a computer system. Unlike graphical user interfaces (GUIs) which rely on visual elements like windows and buttons, terminals allow users to perform tasks by typing commands into a prompt. This method of interaction is highly efficient, flexible, and powerful, especially for programming, automating tasks, managing files, and handling data.

### Why Use Terminals in Coding and Data Science?
- **Efficiency and Speed**: Many tasks can be done quicker through command line than through graphical interfaces.
- **Power and Flexibility**: Terminals provide access to a wide range of tools and utilities for complex operations, which are essential in coding and data science.
- **Automation**: Through scripting, repetitive tasks can be automated, saving time and reducing errors.
- **Access to Remote Systems**: Terminals are key for accessing and managing remote servers, often used in data science for handling large datasets and computational tasks.

### Operating Systems
This course is written to help you understand the basics of CLIs irrespective of the OS you are using. All of these examples work on Linux and MacOSX, because they use similar shells (named bash and zsh). For Windows users, most commands are similar but can be slightly different. In most case where they differ, a simple Google search will be able to provide the Windows equivalent of a Linux/MacOSX command. I personnaly advise aspiring scientists to familiarize with Linux as it is often the most straightforward, transparent and intuitive way to handle code and data projects (among many other advantages such as openeness, reproducibility, security, etc...). You can do that by installing Linux (Ubuntu) through the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) or by [installing it on a computer to give it a second wind](https://www.zdnet.com/article/how-to-install-linux-on-an-old-laptop/). Ultimately the choice is yours, 

## Course Outline

#### 1. The Command Line Interface (CLI)
   - Understanding the CLI environment
   - Navigating the file system
   - Basic commands (like `ls`, `cd`, `mkdir`, `rm`)
#### 2. Understanding File Paths
   - Types of File Paths
   - Key Concepts
   - Working with File Paths
#### 3. File Manipulation
   - Creating, viewing, and editing files
   - File permissions and ownership
#### 4. System Information and Management
   - Checking system status (like `top`, `free`)
   - Installing and updating software
#### 5. Text Processing Tools
   - Using `grep`
   - Introduction to `sed`
   - Utilizing `awk`
   - Sorting and Uniqueness
#### 6. Shell Scripting Basics
   - Introduction to Shell Scripts
   - Basic Scripting Elements
   - Writing and Executing a Script
   - Debugging and Best Practices

## 1: The Command Line Interface (CLI)

### Understanding the CLI Environment
The Command Line Interface (CLI) is a powerful tool for interacting with your computer. Unlike graphical user interfaces, the CLI provides a direct way to communicate with your operating system through text commands. 

#### Key Concepts
- **Prompt**: This is where you type your commands. It typically shows your username, the host name of your computer, and your current directory.
- **Command Syntax**: Most commands follow a format of `command -options arguments`. The command is the action you want to perform, options modify the behavior of the command, and arguments are the targets of the command.
- **Command History**: The CLI keeps a history of your commands, which can be accessed using the up and down arrow keys.

### Navigating the File System
Understanding how to move around your file system is crucial. Here's how you can do it:

- `pwd` (Print Working Directory): Displays the directory you are currently in.
- `ls` (List): Shows the files and folders in the current directory. Use `ls -l` for a detailed list, and `ls -a` to show hidden files.
- `cd` (Change Directory): Moves you to another directory. For example, `cd Documents` will move you to the Documents directory.

### Basic Commands
- `mkdir` (Make Directory): Creates a new directory.
- `rm` (Remove): Deletes files or directories. Use with caution, as this cannot be undone.
- `cp` (Copy) and `mv` (Move): Used for copying and moving files or directories.
- `cat` (Concatenate): Displays the content of a file, can also be used to combine files.

### Practice Exercises
1. **Navigate to a Different Directory**: Use `cd` to move to your Documents directory and back to your home directory.
2. **Create and View Files**: Make a new directory with `mkdir`, create a simple text file using a text editor, and view its contents with `cat`.
3. **Experiment with Command Options**: Try using different options with the `ls` command, like `ls -l` and `ls -a`.

## 2: Understanding File Paths

Understanding file paths is crucial for navigating and manipulating files and directories in the command line. This module will cover the basics of file path notations and how to use them effectively.

### Types of File Paths
- **Absolute Paths**: These paths start from the root directory (denoted by `/` in Linux/macOS and `C:\` or similar in Windows) and provide the complete path to a file or directory. For example, `/home/user/documents` or `C:\Users\user\documents`.
- **Relative Paths**: These paths are relative to the current directory. For example, `documents/project` refers to the 'project' directory inside the 'documents' directory, which is relative to the current directory.

### Key Concepts
- **Home Directory Shortcut**: In Unix-like systems, `~` represents the user's home directory. For example, `~/documents` is an absolute path starting from the home directory.
- **Parent Directory**: `..` represents the parent directory. For instance, `cd ..` moves you one directory up in the hierarchy.
- **Current Directory**: `.` represents the current directory. It is often used in scripting and running local scripts or applications.

### Working with File Paths
- When specifying paths in commands like `cd`, `cp`, `mv`, it's essential to understand whether to use an absolute or relative path.
- Be aware of case sensitivity in Unix-like systems (`Documents` and `documents` are different), whereas Windows paths are case-insensitive.
- Special characters in file names (like spaces) may require escaping or quoting. For example, `cd My\ Documents` or `cd "My Documents"`.

### Practice Exercises
1. **Navigating Using Absolute and Relative Paths**: From your home directory, navigate to a different directory using both its absolute and relative path.
2. **Parent Directory Navigation**: Use `..` to move up in your directory hierarchy and then return to your original directory.
3. **Special Characters in Paths**: Create a directory with a space in its name and practice navigating into it using escaping and quoting.


## 3: File Manipulation

Now, we will explore how to create, view, edit, and manage the permissions of files using the command line. This is a fundamental skill for navigating and organizing your data effectively.

### Creating, Viewing, and Editing Files
- `touch`: Creates a new empty file. For example, `touch example.txt` creates a new file named 'example.txt'.
- `nano`, `vi`, `emacs`: Text editors available in the terminal to edit files. For beginners, `nano` is the most straightforward to use.
- `cat`: Displays the content of a file. It can also be used to create a new file by combining the contents of existing files.
- `less` and `more`: View the contents of a file one page at a time, useful for large files.

### File Permissions and Ownership
Understanding file permissions and ownership is crucial for securing your files and controlling who can access them.

- `ls -l`: Displays file permissions, ownership, and size. Permissions are shown as a string like `-rwxr-xr-x`, representing different access rights.
- `chmod`: Changes the permissions of a file or directory. For example, `chmod 755 example.txt` sets read, write, and execute permissions for the owner, and read and execute permissions for others.
- `chown`: Changes the owner of a file. Requires administrative privileges.
- `chgrp`: Changes the group ownership of a file.

### Practice Exercises
1. **File Creation and Viewing**: Create a new file and use `nano` to write some content in it. View the content using `cat`.
2. **Changing Permissions**: Change the permissions of a file and verify the changes using `ls -l`.
3. **Ownership Modification**: If you have administrative access, try changing the owner or group of a file and verify with `ls -l`.


## 4: System Information and Management

Let's now focus on using the command line to gather system information and manage system resources, which is crucial for optimizing performance and understanding the environment where your code and data science applications run.

### Checking System Status
- `top`: This command shows the real-time view of the system’s ongoing processes and resource usage. It is essential for monitoring CPU and memory usage.
- `df`: Displays disk space usage for all mounted filesystems.
- `free`: Shows the amount of free and used memory in the system.

### Installing and Updating Software
Understanding how to install and update software from the command line is vital, as many development and data science tools are best managed this way.

- Package Managers: 
  - **Linux**: Use `apt` (Debian-based distributions) or `yum` (RedHat-based distributions) for installing and updating software. For example, `sudo apt-get install python3`.
  - **macOS**: `brew`, or Homebrew, is a popular package manager. For instance, `brew install python3`.
  - **Windows**: Windows users can use `choco` (Chocolatey) or Windows Subsystem for Linux (WSL) for similar functionalities.



### Practice Exercises
1. **System Monitoring**: Use `top` to monitor your system's resource usage. Try identifying which processes use the most resources.
2. **Install a Package**: Choose a simple package like `tree` or `htop` and install it using your system's package manager.

With these skills, you'll be able to maintain the health and performance of your coding or data science environment efficiently.

## 5: Linux commands

This is a [CheatSheet](https://www.git-tower.com/blog/command-line-cheat-sheet/) with different commands that you might find useful.