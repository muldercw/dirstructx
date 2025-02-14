import json
import yaml

def to_json_format(directory_structure):
    if not isinstance(directory_structure, dict):
        raise TypeError("Expected a dictionary as directory_structure.")
    return json.dumps(directory_structure, indent=4, ensure_ascii=False)

def to_yaml_format(directory_structure):
    if not isinstance(directory_structure, dict):
        raise TypeError("Expected a dictionary as directory_structure.")
    return yaml.dump(directory_structure, allow_unicode=True, default_flow_style=False)

def to_tree_format(directory_structure, prefix=""):
    if not isinstance(directory_structure, dict):
        raise TypeError("Expected a dictionary as directory_structure.")
    tree_output = []
    items = list(directory_structure.items())
    for index, (name, subitems) in enumerate(items):
        connector = "└──" if index == len(items) - 1 else "├──"
        tree_output.append(f"{prefix}{connector} {name}")
        if isinstance(subitems, dict):
            extension = "    " if index == len(items) - 1 else "│   "
            tree_output.append(to_tree_format(subitems, prefix + extension))
    return "\n".join(tree_output)
