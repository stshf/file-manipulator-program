#!/bin/bash

python3 /app/src/file_manipulator.py reverse /app/test/input_for_reverse_and_copy_test.txt /app/output/reversed_output.txt
python3 /app/src/file_manipulator.py copy /app/test/input_for_reverse_and_copy_test.txt /app/output/copy_output.txt
python3 /app/src/file_manipulator.py duplicate-contents /app/test/input_for_duplicate_test.txt /app/output/duplicated_output.txt 3
python3 /app/src/file_manipulator.py replace-string /app/test/input_for_replace_string_test.txt /app/output/replaced_output.txt fox cat