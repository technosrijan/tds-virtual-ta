## Documentation: Markdown

Markdown is a lightweight markup language for creating formatted text using a plain-text editor. It's the standard for documentation in software projects and data science notebooks.

Watch this introduction to Markdown (19 min):

[]()

Common Markdown syntax:

````
# Heading 1
## Heading 2

**bold** and *italic*

- Bullet point
- Another point
  - Nested point

1. Numbered list
2. Second item

Link text

```python
# Code block
def hello():
    print("Hello")
```

> Blockquote
````

There is also a GitHub Flavored Markdown standard which is popular. This includes extensions like:

```
- [ ] Incomplete task
- [x] Completed task

~~Strikethrough~~

Tables:

| Column 1 | Column 2 |
|----------|----------|
| Cell 1   | Cell 2   |

```

Tools for working with Markdown:

- markdown2: Python library to convert Markdown to HTML
- markdownlint: Linting
- Markdown All in One: VS Code extension
- pandoc: Convert between formats