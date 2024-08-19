import yaml
import os

def convert_yaml_to_github_actions(yaml_file_path, github_actions_yaml_path):
    # Step 1: Read the YAML file
    if not os.path.isfile(yaml_file_path):
        print(f"Error: The file {yaml_file_path} does not exist.")
        return
    
    with open(yaml_file_path, 'r') as yaml_file:
        generic_config = yaml.safe_load(yaml_file)