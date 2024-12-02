# ldb-reader
A Python-based tool to read and parse .ldb (LevelDB) files, commonly used in blockchain and related applications. This script uses the ldbdump utility to extract key-value pairs stored in LevelDB files and outputs the results in a human-readable JSON format.

## Features:
Reads .ldb files and extracts data using ldbdump.
Safely parses the dumped data using Python’s ast.literal_eval for security.
Outputs key-value pairs as formatted JSON, with proper encoding for special characters.
Supports Python 3 and provides error handling for malformed data or execution errors.

## Requirements:
Python 3.x
ldbdump utility (for dumping LevelDB contents)

## Installation:
Clone the repository:

```bash
git clone https://github.com/pbrudny/ldb-reader.git
cd ldb-reader
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Usage:
To run the script, provide the path to the directory containing the .ldb files as a command-line argument:

```bash
python main.py /path/to/your/ldb/files
```

## License

This project is licensed under the MIT License.
