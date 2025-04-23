"""
This module provides a function to read data from a YAML file
and print its content to the console.
It includes error handling for file not found and invalid YAML format.
"""
import yaml

def read_and_print_yaml(file_path):
    """
    Reads data from a YAML file and prints its content.

    Args:
        file_path (str): The path to the YAML file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            print(data)
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file '{file_path}': {e}")

if __name__ == "__main__":
    read_and_print_yaml('test.yaml')
