#!/usr/bin/env python
import os
from huggingface_hub import hf_hub_download
import fire
from pathlib import Path

def download_files(repo_id, output_dir="models", files=None):
    # Extract the organization and model name from the repo_id
    org_name, model_name = repo_id.split("/")

    # Create the output directory structure
    model_dir = os.path.join(output_dir, org_name, model_name)
    os.makedirs(model_dir, exist_ok=True)

    # Default files to download if not specified
    if files is None:
        files = [
            "config.json",
            "special_tokens_map.json",
            "tokenizer.model",
            "tokenizer_config.json"
        ]

    for file in files:
        try:
            file_path = hf_hub_download(repo_id=repo_id, filename=file)
            output_path = os.path.join(model_dir, file)
            symlink = Path(os.readlink(file_path))
            target_file = Path(os.path.dirname(file_path)) / symlink

            os.symlink(target_file, output_path)
            print(f"Downloaded {file} to {output_path}")
        except Exception as e:
            print(f"Error downloading {file}: {str(e)}")

if __name__ == "__main__":
    fire.Fire(download_files)