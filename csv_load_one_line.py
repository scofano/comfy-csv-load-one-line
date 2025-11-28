import csv
import os

class CSVLoadOneLine:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": "E:\ComfyUI_windows_portable\ComfyUI\output\prompts.csv"}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 0xFFFFFFFFFFFFFFFF}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("first_column", "second_column", "full_line")
    FUNCTION = "process"
    CATEGORY = "CSV Load One Line"

    def process(self, file_path, seed=-1):
        if not os.path.isfile(file_path):
            raise ValueError(f"File not found: {file_path}")

        # Read all lines and count them
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            lines = f.readlines()
            total_lines = len(lines)
            print(f"Total lines found: {total_lines}")

        if total_lines == 0:
            raise ValueError("CSV file is empty")

        # Get the first line
        first_line = lines[0].strip()

        # Parse the first line using csv reader
        reader = csv.reader([first_line], delimiter=';')
        row = next(reader)
        if len(row) < 2:
            raise ValueError("First line must have at least 2 columns")

        first_column = row[0]
        second_column = row[1]
        full_line = first_line

        # Remove the first line and write back the rest
        remaining_lines = lines[1:]
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            f.writelines(remaining_lines)

        return first_column, second_column, full_line
