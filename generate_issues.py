#!/usr/bin/env python3
"""
Script to generate GitHub issues for each heading in README.md
This script parses the README.md file and creates issue templates for each main section.
"""

import re
import os

def parse_readme(file_path):
    """Parse README.md and extract sections with their content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = []
    current_section = None
    current_items = []
    
    lines = content.split('\n')
    
    for line in lines:
        # Match main headings (## followed by emoji and number)
        heading_match = re.match(r'^## ([🟢🟡🟠🔵🟣🔴🟤⚫]) (\d+)\. (.+)$', line)
        
        if heading_match:
            # Save previous section if exists
            if current_section:
                sections.append({
                    'emoji': current_section['emoji'],
                    'number': current_section['number'],
                    'title': current_section['title'],
                    'items': current_items.copy()
                })
            
            # Start new section
            current_section = {
                'emoji': heading_match.group(1),
                'number': heading_match.group(2),
                'title': heading_match.group(3)
            }
            current_items = []
        
        # Match checkbox items
        elif line.startswith('- [ ]') and current_section:
            item = line[6:]  # Remove '- [ ] ' prefix
            current_items.append(item)
    
    # Add the last section
    if current_section:
        sections.append({
            'emoji': current_section['emoji'],
            'number': current_section['number'],
            'title': current_section['title'],
            'items': current_items.copy()
        })
    
    return sections

def generate_issue_template(section):
    """Generate a GitHub issue template for a section."""
    title = f"{section['emoji']} {section['number']}. {section['title']}"
    
    body = f"""This issue tracks the learning progress for: **{section['title']}**

## Learning Checklist

"""
    
    for item in section['items']:
        body += f"- [ ] {item}\n"
    
    body += f"""
## Notes

Please use this issue to:
- Track your progress by checking off completed items
- Add notes and resources in the comments
- Ask questions related to this learning section

## Resources

Feel free to add helpful links, tutorials, and resources in the comments below.

---
*This issue was generated from the [Go Learning Roadmap](README.md)*
"""
    
    return title, body

def generate_github_cli_commands(sections):
    """Generate GitHub CLI commands to create issues."""
    commands = []
    
    for section in sections:
        title, body = generate_issue_template(section)
        
        # Escape quotes and newlines for shell command
        escaped_title = title.replace('"', '\\"')
        escaped_body = body.replace('"', '\\"').replace('\n', '\\n')
        
        command = f'gh issue create --title "{escaped_title}" --body "{escaped_body}" --label "learning,roadmap"'
        commands.append(command)
    
    return commands

def save_issue_files(sections, output_dir="issues"):
    """Save individual issue template files."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    issue_files = []
    
    for i, section in enumerate(sections, 1):
        title, body = generate_issue_template(section)
        
        # Create safe filename
        safe_title = re.sub(r'[^\w\s-]', '', section['title'])
        safe_title = re.sub(r'[-\s]+', '-', safe_title).lower()
        filename = f"{i:02d}-{safe_title}.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(body)
        
        issue_files.append({
            'file': filepath,
            'title': title,
            'number': i
        })
    
    return issue_files

def main():
    """Main function to generate GitHub issues."""
    readme_path = 'README.md'
    
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found!")
        return
    
    print("🔍 Parsing README.md...")
    sections = parse_readme(readme_path)
    
    print(f"📋 Found {len(sections)} sections to convert to issues:")
    for section in sections:
        print(f"  {section['emoji']} {section['number']}. {section['title']} ({len(section['items'])} items)")
    
    print("\n📁 Generating issue template files...")
    issue_files = save_issue_files(sections)
    
    print(f"✅ Created {len(issue_files)} issue template files in 'issues/' directory:")
    for issue_file in issue_files:
        print(f"  {issue_file['number']}. {issue_file['file']}")
    
    print("\n🤖 Generating GitHub CLI commands...")
    commands = generate_github_cli_commands(sections)
    
    with open('create_issues.sh', 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# GitHub CLI commands to create issues for Go Learning Roadmap\n")
        f.write("# Make sure you have GitHub CLI installed and authenticated\n")
        f.write("# Run: chmod +x create_issues.sh && ./create_issues.sh\n\n")
        
        for i, command in enumerate(commands, 1):
            f.write(f"echo \"Creating issue {i}/{len(commands)}...\"\n")
            f.write(f"{command}\n")
            f.write("sleep 1  # Rate limiting\n\n")
    
    os.chmod('create_issues.sh', 0o755)
    
    print("✅ Created executable script: create_issues.sh")
    print("\n🎯 Next steps:")
    print("1. Review the generated issue templates in the 'issues/' directory")
    print("2. Install GitHub CLI: https://cli.github.com/")
    print("3. Authenticate: gh auth login")
    print("4. Run: ./create_issues.sh")
    print("\nAlternatively, you can manually create issues using the template files.")

if __name__ == "__main__":
    main()