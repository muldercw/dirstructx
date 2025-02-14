# dirstructx – Directory Structure Generator 📂

**dirstructx** is a Python package that generates structured representations of a directory. It supports multiple output formats such as **JSON, YAML, and tree-like structures**, making it useful for documenting project structures or analyzing filesystem layouts.

## ✨ Features
- **Generate directory structures** recursively with flexible formatting
- **Supports multiple output formats:**
  - `json` (machine-readable)
  - `yaml` (configuration-friendly)
  - `tree` (human-readable)
- **CLI Usage** for quick execution in the terminal
- **Library Usage** for integration into Python projects
- **Custom Sorting Options:**  
  - List **files before directories** or **directories first**  
  - Sort alphabetically or keep the natural order

---

## 🛠 Installation

To install **dirstructx**, clone the repository and install dependencies:

```sh
git clone https://github.com/muldercw/dirstructx.git
cd dirstructx
pip install -r requirements.txt
```

Or install via `pip` (if published on PyPI):

```sh
pip install dirstructx
```

---

## 🚀 Usage

You can use **dirstructx** via **CLI** or as a **Python library**.

### 📌 CLI Usage

Run `dirstructx` on any directory:

```sh
python -m dirstructx /path/to/project --format tree
```

Available output formats:

```sh
python -m dirstructx /path/to/project --format json
python -m dirstructx /path/to/project --format yaml
python -m dirstructx /path/to/project --format tree
```

To redirect output to a file:

```sh
python -m dirstructx /path/to/project --format tree > output.txt
```

---

### 📜 Example Output

#### JSON Output (`--format json`)
```json
{
    "README.md": null,
    "setup.py": null,
    "src": {
        "__init__.py": null,
        "main.py": null,
        "utils": {
            "helpers.py": null,
            "formatters.py": null
        }
    }
}
```

#### YAML Output (`--format yaml`)
```yaml
README.md: null
setup.py: null
src:
  __init__.py: null
  main.py: null
  utils:
    helpers.py: null
    formatters.py: null
```

#### Tree Output (`--format tree`)
```
├── README.md
├── setup.py
└── src
    ├── __init__.py
    ├── main.py
    └── utils
        ├── helpers.py
        └── formatters.py
```

---

## 🖥️ Library Usage

You can also use `dirstructx` in your Python scripts:

```python
from dirstructx import generate_structure

directory_path = "/path/to/project"
structure = generate_structure(directory_path)

print(structure)  # Prints the directory structure as a dictionary
```

To format the output in JSON:

```python
import json
print(json.dumps(structure, indent=4))
```

Or in YAML:

```python
import yaml
print(yaml.dump(structure, default_flow_style=False))
```

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 📫 Contact

For any issues or feature requests, please open an issue on [GitHub](https://github.com/muldercw/dirstructx).

Happy coding! 🚀
