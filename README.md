# ComfyUI CSV Load One Line Node

This is a custom node for ComfyUI that reads the first line from a CSV file, extracts the first two columns and the full line, and then removes the first line from the file.

## Features

- Reads a CSV file using semicolon (`;`) as delimiter
- Outputs the total number of lines found to the console
- Provides three string outputs: first column, second column, and full line
- Modifies the CSV file by removing the processed first line
- Includes a seed input to ensure the node runs on each execution (non-deterministic)

## Inputs

- **file_path** (STRING): Full path to the CSV file
- **seed** (INT): Random seed (default -1, ensures re-execution)

## Outputs

- **first_column** (STRING): The first column of the processed line
- **second_column** (STRING): The second column of the processed line
- **full_line** (STRING): The complete processed line

## Usage

1. Place the node in your ComfyUI workflow
2. Provide the full path to your CSV file
3. Connect the outputs as needed
4. Run the workflow - each execution will process and remove the current first line

## Requirements

- ComfyUI
- Python with csv and os modules (standard library)

## Installation

Copy the `csv_load_one_line.py` and `__init__.py` files to your ComfyUI custom_nodes directory.

Restart ComfyUI to load the new node.
