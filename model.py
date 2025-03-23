from transformers import pipeline


sarcasm_pipe = pipeline("text-classification", model="jkhan447/sarcasm-detection-Bert-base-uncased-newdata")
harm_pipe = pipeline("text-classification", model="unitary/toxic-bert")

def detect_sarcasm(text):
    result = sarcasm_pipe(text)
    return "Sarcasm detected!" if result[0]['label'] == 'LABEL_1' else "No sarcasm detected."

def detect_harm(text):
    result = harm_pipe(text)
    return "Harmful content detected!" if result[0]['label'] == 'toxic' else "No harmful content detected."
