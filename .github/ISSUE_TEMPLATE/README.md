# Issue Templates Documentation

This directory contains GitHub issue templates for the Go Learning Roadmap. Each template corresponds to a section in the main README.md file.

## Available Templates

| Template File | Section | Focus Area |
|---------------|---------|------------|
| `01-go-basics.md` | 🟢 Go Basics | Language fundamentals |
| `02-data-structures.md` | 🟡 Data Structures & Collections | Arrays, slices, maps, structs |
| `03-deeper-features.md` | 🟠 Deeper Language Features | Interfaces, errors, generics |
| `04-concurrency.md` | 🔵 Concurrency & Parallelism | Goroutines, channels, sync |
| `05-standard-library.md` | 🟣 Standard Library & Utilities | I/O, testing, networking |
| `06-advanced-topics.md` | 🔴 Advanced Topics | Context, performance, modules |
| `07-go-in-practice.md` | 🟤 Go in Practice | Web dev, databases, deployment |
| `08-ecosystem-best-practices.md` | ⚫ Ecosystem & Best Practices | Tooling, CI/CD, security |

## Template Structure

Each template includes:
- **Frontmatter**: Metadata for GitHub's issue template system
- **Description**: Overview of the learning section
- **Checklist**: Interactive todo items from the README
- **Resources**: Relevant documentation and learning materials
- **Notes section**: Space for personal notes and code examples

## Usage

### Automated Creation
Use the provided script to create all issues at once:
```bash
./create-learning-issues.sh
```

### Manual Creation
1. Navigate to the Issues tab in GitHub
2. Click "New Issue"
3. Select the desired template
4. Customize and create the issue

## Labels

Issues created from these templates will be automatically labeled with:
- `learning` - Indicates this is a learning progress issue
- Section-specific labels (e.g., `go-basics`, `concurrency`, etc.)