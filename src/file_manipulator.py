import sys
import re
import argparse

def read_contents(input_path: str) -> str:
    try:
        with open(input_path) as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {input_path}: {e}")
        raise

def write_contents(output_path: str, contents: str) -> None:
    try:
        with open(output_path, 'w') as f:
            f.write(contents)
    except IOError as e:
        print(f"Error writing to file {output_path}: {e}")

def process_file(input_path:str, output_path: str, operation: callable, *args) -> None:
    contents = read_contents(input_path)
    proccessed_contents = operation(contents, *args)
    write_contents(output_path, proccessed_contents)

def reverse_string(contents: str) -> str:
    return contents[::-1]

def copy_file(contents: str) -> str:
    return contents

def duplicate_contents(contents:str, times: int) -> str:
    return contents * int(times)

def replace_string(contents: str, target: str, new_string: str) -> str:
    # 置換を実行(大文字と小文字を区別しない)
    return re.sub(target, new_string, contents, flags=re.IGNORECASE)

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="File content manipulator")
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # Reverse command
    reverse_parser = subparsers.add_parser("reverse", help="Reverse the content of a file")
    reverse_parser.add_argument("input", help="Input file path")
    reverse_parser.add_argument("output", help="Output file path")

    # Copy command
    copy_parser = subparsers.add_parser("copy", help="Copy the content of a file")
    copy_parser.add_argument("input", help="Input file path")
    copy_parser.add_argument("output", help="Output file path")

    # Duplicate command
    duplicate_parser = subparsers.add_parser("duplicate-contents", help="duplicate the content of a file")
    duplicate_parser.add_argument("input", help="Input file path")
    duplicate_parser.add_argument("output", help="Output file path")
    duplicate_parser.add_argument("times", type=int, help="Number of times to duplicate")

    # Replace command
    replace_parser = subparsers.add_parser("replace-string", help="Replace the content of a file")
    replace_parser.add_argument("input", help="Input file path")
    replace_parser.add_argument("output", help="Output file path")
    replace_parser.add_argument("target", help="String to replace")
    replace_parser.add_argument("new_string", help="New string")

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    try:
        if args.command == "reverse":
            process_file(args.input, args.output, reverse_string)
        elif args.command == "copy":
            process_file(args.input, args.output, copy_file)
        elif args.command == "duplicate-contents":
            process_file(args.input, args.output, duplicate_contents, args.times)
        elif args.command == "replace-string":
            process_file(args.input, args.output, replace_string, args.target, args.new_string)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()