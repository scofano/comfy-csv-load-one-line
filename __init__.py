from .csv_load_one_line import CSVLoadOneLine, CSVLoadOneLineNoDelete

NODE_CLASS_MAPPINGS = {
    "CSVLoadOneLine": CSVLoadOneLine,
    "CSVLoadOneLineNoDelete": CSVLoadOneLineNoDelete,
}
