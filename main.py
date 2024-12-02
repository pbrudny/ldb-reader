import os
import subprocess
import json
import ast
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Read and parse .ldb (LevelDB) files.")
parser.add_argument("path", help="Path to the directory containing .ldb files")
args = parser.parse_args()

base = args.path  # Get the directory path from the command line argument

# Check if the provided path exists
if not os.path.exists(base):
    print(f"Error: The directory '{base}' does not exist.")
    exit(1)

# Iterate over the files in the provided directory
for f in os.listdir(base):
    if f.endswith(".ldb"):
        try:
            # Run ldbdump to extract the data from the .ldb file
            process = subprocess.Popen(
                ["ldbdump", os.path.join(base, f)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
            )
            output, err = process.communicate()
            exit_code = process.wait()
            
            # If there's an error, print it
            if err:
                print(f"Error reading {f}: {err.decode()}")
                continue
            
            # Parse each line of the output (skipping the first line)
            for line in output.decode().split("\n")[1:]:
                if line.strip() == "":
                    continue
                try:
                    # Parse the line into a dictionary using ast.literal_eval
                    parsed = ast.literal_eval("{" + line + "}")
                    key = list(parsed.keys())[0]  # Get the first (and presumably only) key
                    print(json.dumps({
                        "key": key.encode('unicode_escape').decode('utf-8'),  # For Python 3, use unicode_escape
                        "value": parsed[key]
                    }))
                except Exception as e:
                    print(f"Error parsing line '{line}': {e}")
        except Exception as e:
            print(f"Error processing {f}: {e}")
