import sys
import re

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

def main(args: list[str]) -> None:
    if len(args) < 2:
        print("Usage: python3 file_manipulator.py <argument1> <argument2> ...")
        sys.exit(1)

    cmd = args[0]

    try:
        if cmd == "reverse" and len(args) == 3:
            reverse_string(args[1], args[2])
        elif cmd == "copy" and len(args) == 3:
            copy_file(args[1], args[2])
        elif cmd == "duplicate-contents" and len(args) == 4:
            duplicate_contents(args[1], args[2], args[3])
        elif cmd == "replace-string" and len(args) == 5:
            replace_string(args[1], args[2], args[3], args[4])
        else:
            print("Not valid command")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])