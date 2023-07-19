from tdc.multi_pred import DDI
import pandas as pd
import os
import json


def get_TWOSIDES_dataset(json_root="/root/autodl-tmp/datasets"):
    # Get the TWOSIDES dataset fron internet
    data = DDI(name = 'TWOSIDES')
    split = data.get_split()
    
    # Iterate over each split and write it to a CSV file
    for key in split:
        file_name = key + '.json'
        json_path = os.path.join(json_root, file_name)
        df = pd.DataFrame(split[key])
        df.to_json(json_path, orient="records", indent = 4)


def merge_csv_files(directory_path, output_file):
    # Get a list of all CSV files in the directory
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

    # Initialize an empty list to store the DataFrames from each CSV file
    dfs = []

    # Read and append each CSV file to the list of DataFrames
    for file in csv_files:
        file_path = os.path.join(directory_path, file)
        df = pd.read_csv(file_path)
        dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    merged_df = pd.concat(dfs, ignore_index=True)

    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)


def merge_json_files(directory_path, output_file):
    # Get a list of all JSON files in the directory
    json_files = [file for file in os.listdir(directory_path) if file.endswith('.json')]

    # Initialize an empty dictionary to store the merged data
    merged_data = {}

    # Read and merge each JSON file
    for file in json_files:
        file_path = os.path.join(directory_path, file)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for each in data:  
                merged_data.update(each)

    # Write the merged data to a new JSON file
    with open(output_file, 'w') as output_json:
        print(output_file)
        json.dump(merged_data, output_json, indent=4)


def describe_json_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

        # Get the number of keys in the JSON object
        num_keys = len(data)

        # Get the data type and basic statistics for each key
        key_info = {}
        for key, value in data.items():
            data_type = type(value).__name__
            key_info[key] = {
                'data_type': data_type,
            }

        # Print the general information about the JSON file
        print(f"Number of keys: {num_keys}")
        print("Key information:")
        for key, info in key_info.items():
            print(f"  Key: {key}")
            print(f"    Data Type: {info['data_type']}")
            print()


merge_json_files("/root/autodl-tmp/datasets", "twosides.json")