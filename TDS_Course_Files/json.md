## JSON

JSON (JavaScript Object Notation) is the de facto standard format for data exchange on the web and APIs. Its human-readable format and widespread support make it essential for data scientists working with web services, APIs, and configuration files.

For data scientists, JSON is essential when:

- Working with REST APIs and web services
- Storing configuration files and metadata
- Parsing semi-structured data from databases like MongoDB
- Creating data visualization specifications (e.g., Vega-Lite)

Watch this comprehensive introduction to JSON (15 min):

[](https://youtu.be/GpOO5iKzOmY)

Key concepts to understand in JSON:

- JSON only supports 6 data types: strings, numbers, booleans, null, arrays, and objects
- You can nest data. Arrays and objects can contain other data types, including other arrays and objects
- Always validate. Ensure JSON is well-formed. Comm errors: Trailing commas, missing quotes, and escape characters

JSON Lines is a format that allows you to store multiple JSON objects in a single line.
It's useful for logging and streaming data.

Tools you could use with JSON:

- JSONLint: Validate and format JSON
- JSON Editor Online: Visual JSON editor and formatter
- JSON Schema: Define the structure of your JSON data
- jq: Command-line JSON processor

Common Python operations with JSON:

```python
import json

# Parse JSON string
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)

# Convert to JSON string
json_str = json.dumps(data, indent=2)

# Read JSON from file
with open('data.json') as f:
    data = json.load(f)

# Write JSON to file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read JSON data a Pandas DataFrame. JSON data is typically stored as an array of objects.
import pandas as pd
df = pd.read_json('data.json')

# Read JSON lines from file into a DataFrame. JSON lines are typically one line per object.
df = pd.read_json('data.jsonl', lines=True)
```

Practice JSON skills with these resources:

- JSON Generator: Create sample JSON data
- JSON Path Finder: Learn to navigate complex JSON structures
- JSON Schema Validator: Validate JSON against schemas