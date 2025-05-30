# 🔄 Module 1: Version Control & Collaboration

Welcome to the world of version control! This module will cover the use of Git and GitHub, essential tools for collaborating on AI projects.

## Table of Contents
1. [Introduction to Git](#introduction-to-git)
2. [Getting Started with GitHub](#getting-started-with-github)
3. [Basic Git Commands](#basic-git-commands)
4. [Collaboration Workflow](#collaboration-workflow)

## Introduction to Git

### What is Git?
Git is a distributed version control system that helps you track changes in your code and collaborate with others.

### Installation
1. Download Git from [git-scm.com](https://git-scm.com/downloads)
2. Verify installation:
   ```bash
   git --version
   ```
3. Configure Git:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

## Getting Started with GitHub

### What is GitHub?
GitHub is a platform for hosting and collaborating on Git repositories.

### Setting Up
1. Create a GitHub account at [github.com](https://github.com)
2. Set up SSH keys for secure authentication
3. Create your first repository

## Basic Git Commands

### Repository Setup
```bash
git init              # Initialize a new repository
git clone <url>       # Clone an existing repository
git status           # Check repository status
```

### Making Changes
```bash
git add .            # Stage all changes
git commit -m "msg"  # Commit changes with message
git push             # Push changes to remote
git pull             # Pull changes from remote
```

### Branching
```bash
git branch           # List branches
git checkout -b new  # Create and switch to new branch
git merge branch     # Merge branch into current
```

## Collaboration Workflow

### Best Practices
1. Always pull before starting work
2. Create feature branches for new work
3. Write clear commit messages
4. Review code before merging
5. Keep commits focused and atomic

### Working with Others
1. Fork repositories
2. Create pull requests
3. Review and comment on code
4. Resolve merge conflicts

## AI Project Best Practices

### Repository Structure
```
project/
├── data/           # Data files
├── notebooks/      # Jupyter notebooks
├── src/           # Source code
├── tests/         # Test files
├── requirements.txt # Dependencies
└── README.md      # Documentation
```

### Version Control for AI Projects
- Track model versions
- Document data changes
- Version your datasets
- Keep track of experiments

## Troubleshooting
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Help](https://help.github.com)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## Additional Resources
- [GitHub Learning Lab](https://lab.github.com)
- [GitHub Skills](https://skills.github.com)
- [Pro Git Book](https://git-scm.com/book/en/v2) 