import gradio as gr
import requests
import json

# Constants
API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codegemma"
HEADERS = {'Content-Type': 'application/json'}
MAX_TURNS = 3  
MAX_TOKENS = 256  

# Streaming chat with trimmed prompt
def chat_with_codegemma(message, chat_history):
    recent_history = chat_history[-MAX_TURNS:]

    prompt = ""
    for user, bot in recent_history:
        prompt += f"User: {user}\nAssistant: {bot}\n"
    prompt += f"User: {message}\nAssistant:"

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": True,
        "num_predict": MAX_TOKENS
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload), stream=True, timeout=30)
        response.raise_for_status()

        reply = ""
        for line in response.iter_lines(decode_unicode=True):
            if line.strip():
                try:
                    data = json.loads(line)
                    token = data.get("response", "")
                    reply += token
                    yield "", chat_history + [(message, reply)]
                except json.JSONDecodeError:
                    continue

    except requests.exceptions.RequestException as e:
        yield "", chat_history + [(message, f"❌ Request error: {e}")]
    except Exception as e:
        yield "", chat_history + [(message, f"❌ Unexpected error: {e}")]

# UI setup
with gr.Blocks() as demo:
    gr.Markdown("## Code assistant Chatbot by Dhinesh A M\nAsk coding questions or request code generation.")
    
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Type your prompt here...", label="Your Message")
    clear_btn = gr.Button("🧹 Clear Chat")
    
    state = gr.State([])

    user_input.submit(chat_with_codegemma, [user_input, state], [user_input, chatbot])
    clear_btn.click(fn=lambda: ([], ""), outputs=[chatbot, state])

if __name__ == "__main__":
    demo.launch()
