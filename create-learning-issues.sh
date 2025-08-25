#!/bin/bash

# Script to create GitHub issues for each section of the Go Learning Roadmap
# This script requires the GitHub CLI (gh) to be installed and authenticated

echo "🚀 Creating GitHub Issues for Go Learning Roadmap Sections"
echo "============================================================"

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed. Please install it first:"
    echo "   https://cli.github.com/"
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub CLI. Please run 'gh auth login' first."
    exit 1
fi

# Array of issue titles and template files
declare -a sections=(
    "🟢 1. Go Basics (Language Core):01-go-basics.md"
    "🟡 2. Data Structures & Collections:02-data-structures.md"
    "🟠 3. Deeper Language Features:03-deeper-features.md"
    "🔵 4. Concurrency & Parallelism:04-concurrency.md"
    "🟣 5. Standard Library & Utilities:05-standard-library.md"
    "🔴 6. Advanced Topics:06-advanced-topics.md"
    "🟤 7. Go in Practice:07-go-in-practice.md"
    "⚫ 8. Ecosystem & Best Practices:08-ecosystem-best-practices.md"
)

created_issues=()

echo "Creating issues..."
echo ""

for section in "${sections[@]}"; do
    IFS=':' read -r title template <<< "$section"
    template_path=".github/ISSUE_TEMPLATE/$template"
    
    if [[ -f "$template_path" ]]; then
        echo "📝 Creating issue: $title"
        
        # Extract the issue body from the template (everything after the frontmatter)
        body=$(sed -n '/^---$/,/^---$/d; /./,$p' "$template_path")
        
        # Create the issue
        issue_url=$(gh issue create --title "Learn $title" --body "$body" --label "learning")
        
        if [[ $? -eq 0 ]]; then
            echo "✅ Created: $issue_url"
            created_issues+=("$issue_url")
        else
            echo "❌ Failed to create issue for: $title"
        fi
    else
        echo "❌ Template not found: $template_path"
    fi
    echo ""
done

echo "============================================================"
echo "🎉 Issue creation complete!"
echo ""
echo "Created ${#created_issues[@]} issues:"
for issue in "${created_issues[@]}"; do
    echo "  • $issue"
done
echo ""
echo "💡 Tip: You can view all your learning issues with:"
echo "   gh issue list --label learning"