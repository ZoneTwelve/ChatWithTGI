import gradio as gr
from huggingface_hub import InferenceClient
from transformers import AutoTokenizer
import os
import logging

from dotenv import load_dotenv
load_dotenv()

API = os.getenv("API")
client = InferenceClient(model=API)

tokenizer = AutoTokenizer.from_pretrained('./model')

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def convert_to_chat_format(history, message):
    res = []

    for user, assistant in history:
        res += [{"role": "user", "content": user}]
        res += [{"role": "assistant", "content": assistant}]
    res += [{"role": "user", "content": message}]
    chat = tokenizer.apply_chat_template(res, tokenize=False)
    return chat

def inference(message, history):
    logging.info(f"User input: {message}")  # Log user input
    partial_message = ""
    try:
        for token in client.text_generation(convert_to_chat_format(history, message), max_new_tokens=200, stream=True):
            partial_message += token
            yield partial_message
    except Exception as e:
        logging.error(f"Error during inference: {str(e)}")  # Log any errors
    logging.info(f"Assistant output: {partial_message}")  # Log assistant output

gr.ChatInterface(
    inference,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Chat with me!", container=False, scale=7),
    description="This is the demo for Gradio UI consuming TGI endpoint with LLaMA 7B-Chat model.",
    title="WebUI Using TGI",
    examples=["你是誰？", "你可以教我怎麼算數學嗎？ 1+1=?"],
    retry_btn="Retry",
    undo_btn="Undo",
    clear_btn="Clear",
).queue().launch()