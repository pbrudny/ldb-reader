import json
import sys

METAMASK_ID = "nkbihfbeogaeaoehlefnkodbefgpgknn"

def main():
    if len(sys.argv) < 2:
        print("Usage: python filter_json.py <input_file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "metamask_filtered_output.json"

    # Read the input JSON file
    with open(input_file, "r") as file:
        data = json.load(file)

    # Filter entries related to MetaMask
    metamask_data = [
        item for item in data if METAMASK_ID in item.get("path", "")
    ]

    # Write the filtered MetaMask data to the output file
    with open(output_file, "w") as file:
        json.dump(metamask_data, file, indent=2)

    print(f"MetaMask data saved to {output_file}")

if __name__ == "__main__":
    main()
