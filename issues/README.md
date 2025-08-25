# GitHub Issues for Go Learning Roadmap

This directory contains GitHub issue templates generated from the main README.md file. Each file represents one section of the Go learning roadmap and can be used to create GitHub issues for tracking learning progress.

## Files Generated

1. `01-go-basics-language-core.md` - 🟢 Go Basics (Language Core)
2. `02-data-structures-collections.md` - 🟡 Data Structures & Collections
3. `03-deeper-language-features.md` - 🟠 Deeper Language Features
4. `04-concurrency-parallelism.md` - 🔵 Concurrency & Parallelism
5. `05-standard-library-utilities.md` - 🟣 Standard Library & Utilities
6. `06-advanced-topics.md` - 🔴 Advanced Topics
7. `07-go-in-practice.md` - 🟤 Go in Practice
8. `08-ecosystem-best-practices.md` - ⚫ Ecosystem & Best Practices

## How to Create GitHub Issues

### Option 1: Using GitHub CLI (Automated)

1. Install GitHub CLI: https://cli.github.com/
2. Authenticate: `gh auth login`
3. Run the script: `../create_issues.sh`

### Option 2: Manual Creation

1. Go to your GitHub repository
2. Click "Issues" tab
3. Click "New issue"
4. Copy the title from the filename (e.g., "🟢 1. Go Basics (Language Core)")
5. Copy the content from the corresponding `.md` file
6. Add labels: `learning`, `roadmap`
7. Create the issue

### Option 3: Using GitHub Web Interface with Templates

You can copy and paste the content from each `.md` file into new GitHub issues.

## Benefits of Using GitHub Issues

- ✅ Track progress with checkboxes
- 💬 Add comments with notes and resources
- 🏷️ Use labels for organization
- 📝 Link related issues and pull requests
- 👥 Collaborate with others learning Go
- 📊 View progress in GitHub's project boards

## Regenerating Templates

If the main README.md is updated, you can regenerate these templates by running:

```bash
cd /path/to/repository
python3 generate_issues.py
```

This will update all template files and the `create_issues.sh` script.