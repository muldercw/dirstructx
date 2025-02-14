import argparse
from .generator import generate_structure
from .formats import to_json_format, to_yaml_format, to_tree_format
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate directory structure in various formats.")
    parser.add_argument("directory", type=str, help="Path to the directory to scan")
    parser.add_argument("--format", type=str, choices=["json", "yaml", "tree"], default="tree",
                        help="Output format (default: tree)")
    args = parser.parse_args()
    structure = generate_structure(args.directory)
    if args.format == "json":
        output = to_json_format(structure)
    elif args.format == "yaml":
        output = to_yaml_format(structure)
    else:
        output = to_tree_format(structure)
    print(output)

if __name__ == "__main__":
    main()
