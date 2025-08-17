#!/usr/bin/env python3
"""
Convert markdown to HTML for platforms that don't support markdown
"""

def markdown_to_html_basic(text):
    """Basic markdown to HTML conversion"""
    
    # Headers
    text = text.replace('# ', '<h1>').replace('\n\n', '</h1>\n\n')
    text = text.replace('## ', '<h2>').replace('\n\n', '</h2>\n\n')
    text = text.replace('### ', '<h3>').replace('\n\n', '</h3>\n\n')
    
    # Bold
    text = text.replace('**', '<strong>', 1).replace('**', '</strong>', 1)
    
    # Code blocks
    text = text.replace('```bash\n', '<pre><code>')
    text = text.replace('```python\n', '<pre><code>')
    text = text.replace('```\n', '</code></pre>')
    
    # Inline code
    text = text.replace('`', '<code>', 1).replace('`', '</code>', 1)
    
    # Lists
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('- '):
            lines[i] = f"<li>{line[2:]}</li>"
    
    return '\n'.join(lines)

# Usage for Medium
with open('medium_article.md', 'r') as f:
    markdown = f.read()

html = markdown_to_html_basic(markdown)

with open('medium_html.txt', 'w') as f:
    f.write(html)

print("HTML version created: medium_html.txt")