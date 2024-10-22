import torch
import whisper

print(torch.cuda.get_device_name(0) + " is available:")
print(torch.cuda.is_available())

model = whisper.load_model("medium", device="cuda")
result = model.transcribe("audio.mp3", language="sk")
print(f"Detected language: {result['language']}")

formatted_paragraphs = []
current_paragraph = []

for segment in result['segments']:
    text = segment['text'].strip()
    current_paragraph.append(text)

    # Check if there’s a long enough pause (e.g., more than 1 second) to start a new paragraph
    if segment['end'] - segment['start'] > 1.0:
        formatted_paragraphs.append(" ".join(current_paragraph))
        current_paragraph = []

if current_paragraph:
    formatted_paragraphs.append(" ".join(current_paragraph))

formatted_text = "\n\n".join(formatted_paragraphs)
print(formatted_text)
