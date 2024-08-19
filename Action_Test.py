import json
import yaml
import os
import sys

def convert_json_to_github_actions(json_file_path, github_actions_yaml_path):
    # Step 1: Read the JSON file
    if not os.path.isfile(json_file_path):
        print(f"Error: The file {json_file_path} does not exist.")
        return
    
    with open(json_file_path, 'r') as json_file:
        generic_config = json.load(json_file)
    
    # Step 2: Transform the JSON configuration to GitHub Actions configuration
    steps = []
    for step in generic_config.get('Steps', []):
        for action in step.get('Actions', []):
            steps.append({
                'name': action.get('Name', 'Unnamed Step'),
                'run': action['Properties'].get('Octopus.Action.Script.ScriptBody', '')
            })
    
    github_actions_config = {
        'name': generic_config.get('Name', 'Default Workflow Name'),
        'on': ['push'],
        'jobs': {
            'build': {
                'runs-on': 'ubuntu-latest',
                'steps': steps
            }
        }
    }
    
    # Step 3 & 4: Convert to YAML and write to file
    yaml_data = yaml.dump(github_actions_config, default_flow_style=False)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(github_actions_yaml_path), exist_ok=True)
    
    # Write the YAML string to a file
    with open(github_actions_yaml_path, 'w') as yaml_file:
        yaml_file.write(yaml_data)
    print(f"Output written to {github_actions_yaml_path}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Action_Test.py <input_json_file> <output_yaml_file>")
        sys.exit(1)
    
    input_json_file = sys.argv[1]
    output_yaml_file = sys.argv[2]
    
    convert_json_to_github_actions(input_json_file, output_yaml_file)
