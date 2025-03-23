import gradio as gr
from model import detect_sarcasm, detect_harm
from ocr import extract_text_from_image


def analyze_chat(chat, image):
    if image is not None:
        chat = extract_text_from_image(image.name)

    if not chat.strip():
        return "Error: No text provided for analysis."

    sentences = chat.split("\n")
    results = []
    chat_is_harmful = False

    for message in sentences:
        sarcasm_result = detect_sarcasm(message)
        harm_result = detect_harm(message)
        results.append(f"Sentence: {message}\n{sarcasm_result}\n{'Harmful content detected!' if harm_result else 'No harmful content detected.'}\n")

        if harm_result:
            chat_is_harmful = True

    final_verdict = "🚨 **Harmful Chat Detected!** 🚨" if chat_is_harmful else "✅ **Chat is Safe.** ✅"

    return "\n".join(results) + "\n\n" + final_verdict

css = "static/styles.css"

with gr.Blocks(css=css) as app:
    gr.Markdown("<h1>Sarcasm & Harm Detector</h1>")
    
    img_input = gr.File(label="Upload Screenshot (PNG/JPG)")
    chat_input = gr.Textbox(label="Extracted/Typed Text", placeholder="Type chat messages or upload an image...", lines=5)
    analyze_button = gr.Button("Analyze")
    output = gr.Textbox(label="Results", interactive=False)

    analyze_button.click(analyze_chat, inputs=[chat_input, img_input], outputs=output)

app.launch()
