# U-Phoria – AI Assistant

U-Phoria is a voice-based AI assistant with a graphical user interface. It can understand your voice commands, respond using text-to-speech, and reply using an AI model running locally via Ollama.

## Features

- Voice input using microphone
- Text-to-speech responses
- AI responses using Ollama (llama3.2 model)
- Maintains conversation context
- Simple and user-friendly GUI

## How to Run

1. Install the required libraries:

```
pip install pyttsx3 speechrecognition pillow ollama
```

2. Run the app:

```
python GUI.py
```

## Files

- `GUI.py` – Main application with GUI
- `AI_voice_output.py` – Converts text to speech
- `speech_conversion.py` – Converts speech to text
- `action.py` – Handles AI responses using Ollama

## Notes

- Make sure your microphone is connected.
- Ollama must be installed and running locally.