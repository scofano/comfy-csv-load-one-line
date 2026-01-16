import csv
import os

class CSVLoadOneLine:
    TITLE = "CSV Load One Line (Line Delete)"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": "D:\\ComfyUI_windows_portable\\ComfyUI\\output\\prompts.csv"}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 0xFFFFFFFFFFFFFFFF}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("first_column", "second_column", "third_column", "full_line")
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

        # Dynamically assign columns, using empty strings for missing columns
        first_column = row[0] if len(row) >= 1 else ""
        second_column = row[1] if len(row) >= 2 else ""
        third_column = row[2] if len(row) >= 3 else ""
        full_line = first_line

        # Remove the first line and write back the rest
        remaining_lines = lines[1:]
        print(f"Deleting first line. Original lines: {total_lines}, Remaining: {len(remaining_lines)}")
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            f.writelines(remaining_lines)
        print("File updated, first line deleted.")

        return first_column, second_column, third_column, full_line


class CSVLoadOneLineNoDelete:
    TITLE = "CSV Load One Line (No Delete)"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": "E:\\ComfyUI_windows_portable\\ComfyUI\\output\\prompts.csv"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF, "control_after_generate": "increment"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("first_column", "second_column", "third_column", "full_line")
    FUNCTION = "process"
    CATEGORY = "CSV Load One Line"

    def process(self, file_path, seed=0):
        if not os.path.isfile(file_path):
            raise ValueError(f"File not found: {file_path}")

        # Read all lines and count them
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            lines = f.readlines()
            total_lines = len(lines)
            print(f"Total lines found: {total_lines}")

        if total_lines == 0:
            raise ValueError("CSV file is empty")

        # Cycle through lines using modulo
        line_index = seed % total_lines
        selected_line = lines[line_index].strip()
        print(f"Reading line at index {line_index} (seed {seed}): {selected_line}")

        # Parse the selected line using csv reader
        reader = csv.reader([selected_line], delimiter=';')
        row = next(reader)

        # Dynamically assign columns, using empty strings for missing columns
        first_column = row[0] if len(row) >= 1 else ""
        second_column = row[1] if len(row) >= 2 else ""
        third_column = row[2] if len(row) >= 3 else ""
        full_line = selected_line

        # No deletion of the line

        return first_column, second_column, third_column, full_line
