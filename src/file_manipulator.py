import sys
import re

def read_contents(input_path):
    contents = ''
    with open(input_path) as f:
        contents = f.read()
    return contents

def write_contents(output_path, contents):
    with open(output_path, 'w') as f:
        f.write(contents)

def reverse_string(input_path, output_path):
    contents = read_contents(input_path)
    reversed_contents = contents[::-1]
    write_contents(output_path, reversed_contents)


def copy_file(input_path, output_path):
    contents = read_contents(input_path)
    write_contents(output_path, contents)

def duplicate_contents(input_path, output_path, times):
    contents = read_contents(input_path)
    contents_times = contents * int(times)
    write_contents(output_path, contents_times)

def replace_string(input_path, output_path, target, new_string):
    contents = read_contents(input_path)
    # 置換を実行(大文字と小文字を区別しない)
    replaced_contents = re.sub(target, new_string, contents, flags=re.IGNORECASE)
    write_contents(output_path, replaced_contents)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 file_manipulator.py <argument1> <argument2> ...")
        sys.exit(1)
    # CLI引数を取得
    arguments = sys.argv[1:]

    print("引数: ", arguments)

    cmd = arguments[0]

    if cmd == "reverse" and len(arguments) == 3:
        reverse_string(arguments[1], arguments[2])
    elif cmd == "copy" and len(arguments) == 3:
        copy_file(arguments[1], arguments[2])
    elif cmd == "duplicate-contents" and len(arguments) == 4:
        duplicate_contents(arguments[1], arguments[2], arguments[3])
    elif cmd == "replace-string" and len(arguments) == 5:
        replace_string(arguments[1], arguments[2], arguments[3], arguments[4])
    else:
        print("Not valid command")
        sys.exit(1)

if __name__ == "__main__":
    main()