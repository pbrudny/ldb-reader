import json
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python filter_json.py <input_file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "filtered_output.json"

    # Read the input JSON file
    with open(input_file, "r") as file:
        data = json.load(file)

    # Filter out elements with empty 'data' attributes
    filtered_data = [item for item in data if item.get("data")]

    # Write the filtered data to the output file
    with open(output_file, "w") as file:
        json.dump(filtered_data, file, indent=2)

    print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    main()
