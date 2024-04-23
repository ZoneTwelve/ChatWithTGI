# ChatWithTGI

This repository provides a web user interface (WebUI) built with Gradio that allows you to interact conversationally with a large language model (LLM). The backend utilizes the Text Generation Interface (TGI) and the powerful LLaMA 7B-Chat model.

**Key Features:**

- **Interactive Chat:** Engage in natural language conversations with the LLaMA model using the Gradio interface.
- **Customizable Model:** Easily update the model by specifying the TGI endpoint address through environment variables.
- **Error Handling:** Logs errors for debugging purposes to aid in troubleshooting unexpected behavior.
- **Clear Output:** The WebUI displays both user input and the model's generated responses in a clear and user-friendly format.

**Requirements:**

- Python 3.10 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- Gradio ([https://www.gradio.app/docs/interface](https://www.gradio.app/docs/interface))
- transformers ([https://huggingface.co/docs/transformers/en/index](https://huggingface.co/docs/transformers/en/index))
- huggingface_hub ([https://huggingface.co/docs/hub/en/index](https://huggingface.co/docs/hub/en/index))
- dotenv ([https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/))
- fire ([https://pypi.org/project/fire/](https://pypi.org/project/fire/))

**Installation:**

1. Clone this repository:

```bash
git clone https://github.com/ZoneTwelve/ChatWithTGI
```

2. Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
    
```bash
# I didn't provide a requirements.txt at the moment.
# pip install -r requirements.txt
```

**Downloading the Model Tokenizer:**

To ensure correct tokenization, download the tokenizer files associated with the hf model you're using. You can either manually download them from the Hugging Face Hub or use the provided `download.py` script:

**Manual Download:**

- Locate the appropriate tokenizer repository on Hugging Face Hub ([https://huggingface.co/models](https://huggingface.co/models)).
- Download the necessary tokenizer files (e.g., "tokenizer.model", "tokenizer_config.json", etc.) to a designated directory (e.g., `./model`).

**Using `download.py` (Recommended):**

1. Specify the Hugging Face Hub repository ID for your LLaMA 7B-Chat tokenizer (e.g., `organization/model-name`).
2. Run the following command, replacing `<repo_id>` with the actual ID:

```bash
# Exmaple: python download.py taide/TAIDE-LX-7B-Chat --output_dir ./models
python download.py download_files <repo_id>
```

   This will automatically download the required tokenizer files to the `models` directory within your project.

**Environment Variables:**

- Set the `API` environment variable to the TGI endpoint address for model inference:

   ```bash
   export API="your_tgi_endpoint_address"
   ```

   **Important:** Replace `your_tgi_endpoint_address` with the actual URL for your TGI endpoint.

**Running the WebUI:**

1. Start the WebUI server:

   ```bash
   python server.py --tokenizer <tokenizer_path> # Replace with your tokenizer path
   ```

2. Open a web browser and navigate to `http://127.0.0.1:8000` (or the port specified in your Gradio configuration) to interact with the LLaMA model through the conversational interface.

**Contributing:**

We welcome contributions to this project! Feel free to create pull requests if you have improvements or suggestions.

**License:**

This project is licensed under the Apache 2.0 License ([https://opensource.org/license/apache-2.0](https://opensource.org/license/apache-2.0)).

**Additional Notes:**

- Consider including usage examples to demonstrate how to interact with the WebUI.
- If you're using a cloud platform for deployment, provide instructions specific to that environment.
- For more advanced customization, refer to the Gradio documentation for configuration options.

/* warning message: this is an auto-generated README */