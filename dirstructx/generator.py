import os
import json
import yaml
from .formats import to_tree_format, to_json_format, to_yaml_format

def get_directory_structure(root_dir, order="files_first", max_depth=None, exclude=None, depth=0):
    if max_depth is not None and depth > max_depth:
        return []
    try:
        items = os.listdir(root_dir)
    except PermissionError:
        return []
    if exclude:
        items = [item for item in items if not any(ext in item for ext in exclude)]
    files = sorted([item for item in items if os.path.isfile(os.path.join(root_dir, item))])
    dirs = sorted([item for item in items if os.path.isdir(os.path.join(root_dir, item))])
    ordered_items = files + dirs if order == "files_first" else dirs + files
    structure = {}
    for item in ordered_items:
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            structure[item] = get_directory_structure(item_path, order, max_depth, exclude, depth + 1)
        else:
            structure[item] = None 
    return structure

def generate_structure(directory):
    structure = {}
    for entry in sorted(os.listdir(directory)): 
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            structure[entry] = ""
        elif os.path.isdir(full_path):
            structure[entry] = generate_structure(full_path)
    return structure


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a directory structure.")
    parser.add_argument("directory", help="The root directory to generate structure from")
    parser.add_argument("--format", choices=["tree", "json", "yaml"], default="tree", help="Output format")
    parser.add_argument("--order", choices=["files_first", "dirs_first"], default="files_first", help="Ordering")
    parser.add_argument("--max-depth", type=int, help="Maximum depth to traverse")
    parser.add_argument("--exclude", nargs="*", help="File extensions to exclude (e.g. .pyc .log)")
    args = parser.parse_args()
    print(generate_structure(args.directory, args.format, args.order, args.max_depth, args.exclude))
