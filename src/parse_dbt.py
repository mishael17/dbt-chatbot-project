import json
import os
from format_metadata import create_chunks

def load_manifest(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def extract_models(manifest):
    models = []
    for model_name, model_data in manifest.get('nodes', {}).items():
        models.append({
            'name': model_data.get('name'),
            'description': model_data.get('description', ''),
            'materialization': model_data.get('config', {}).get('materialized', 'unknown'),
            'columns': [
                {
                    'name': col_name,
                    'description': col_data.get('description', '')
                }
                for col_name, col_data in model_data.get('columns', {}).items()
            ]
        })
    return models

if __name__ == "__main__":
    manifest = load_manifest('data/target/manifest.json')
    models = extract_models(manifest)
    for m in models:
        print(m)

