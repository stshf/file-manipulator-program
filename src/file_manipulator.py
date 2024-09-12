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

def reverse_string(input_path: str, output_path: str) -> None:
    contents = read_contents(input_path)
    reversed_contents = contents[::-1]
    write_contents(output_path, reversed_contents)

def copy_file(input_path: str, output_path: str) -> None:
    contents = read_contents(input_path)
    write_contents(output_path, contents)

def duplicate_contents(input_path: str, output_path: str, times: int) -> None:
    contents = read_contents(input_path)
    contents_times = contents * int(times)
    write_contents(output_path, contents_times)

def replace_string(input_path: str, output_path: str, target: str, new_string: str) -> None:
    contents = read_contents(input_path)
    # 置換を実行(大文字と小文字を区別しない)
    replaced_contents = re.sub(target, new_string, contents, flags=re.IGNORECASE)
    write_contents(output_path, replaced_contents)

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
            reverse_string(args.input, args.output)
        elif args.command == "copy":
            copy_file(args.input, args.output)
        elif args.command == "duplicate-contents":
            duplicate_contents(args.input, args.output, args.times)
        elif args.command == "replace-string":
            replace_string(args.input, args.output, args.target, args.new_string)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()