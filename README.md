# ComfyUI CSV Load One Line Nodes

This package provides two custom nodes for ComfyUI that read the first line from a CSV file and extract up to three columns and the full line. One node removes the processed line, while the other reads without modifying the file.

## Nodes

### CSV Load One Line (Line Delete)

Reads the first line from a CSV file, extracts the data, and removes the line from the file.

**Features:**
- Reads a CSV file using semicolon (`;`) as delimiter
- Outputs the total number of lines found to the console
- Provides four string outputs: first column, second column, third column, and full line
- Automatically handles CSV files with 1-3+ columns (returns empty strings for missing columns)
- Modifies the CSV file by removing the processed first line
- Includes a seed input (default -1) to ensure re-execution

**Inputs:**
- **file_path** (STRING): Full path to the CSV file
- **seed** (INT): Random seed (default -1, ensures re-execution)

**Outputs:**
- **first_column** (STRING): The first column of the processed line (empty string if not available)
- **second_column** (STRING): The second column of the processed line (empty string if not available)
- **third_column** (STRING): The third column of the processed line (empty string if not available)
- **full_line** (STRING): The complete processed line

**Usage:**
1. Place the "CSV Load One Line (Line Delete)" node in your ComfyUI workflow
2. Provide the full path to your CSV file
3. Connect the outputs as needed
4. Run the workflow - each execution will process and remove the current first line

### CSV Load One Line (No Delete)

Reads a specific line from a CSV file based on the seed value without modifying the file, with an incrementing seed.

**Features:**
- Reads a CSV file using semicolon (`;`) as delimiter
- Outputs the total number of lines found to the console
- Provides four string outputs: first column, second column, third column, and full line
- Automatically handles CSV files with 1-3+ columns (returns empty strings for missing columns)
- Does not modify the CSV file
- Seed starts at 0 and increments automatically after each generation, used as the line index with cycling (seed % total_lines)

**Inputs:**
- **file_path** (STRING): Full path to the CSV file
- **seed** (INT): Line index to read (0-based), increments after each run (default 0)

**Outputs:**
- **first_column** (STRING): The first column of the processed line (empty string if not available)
- **second_column** (STRING): The second column of the processed line (empty string if not available)
- **third_column** (STRING): The third column of the processed line (empty string if not available)
- **full_line** (STRING): The complete processed line

**Usage:**
1. Place the "CSV Load One Line (No Delete)" node in your ComfyUI workflow
2. Provide the full path to your CSV file
3. Connect the outputs as needed
4. Run the workflow - each execution will read the line at the current seed index without removing it

## Requirements

- ComfyUI
- Python with csv and os modules (standard library)

## Installation

Copy the `csv_load_one_line.py` and `__init__.py` files to your ComfyUI custom_nodes directory.

Restart ComfyUI to load the new node.
