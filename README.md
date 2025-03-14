# Vosk Speech-to-Text Converter

This Python script transcribes speech from an audio file using the [Vosk](https://alphacephei.com/vosk/) speech recognition system and saves the transcription to a DOCX file.

## Features
- Converts speech from a WAV audio file (mono, 16-bit PCM) to text.
- Uses Vosk, a lightweight speech recognition engine.
- Saves transcription in a Microsoft Word document.
- Handles errors and unsupported audio formats.

## Requirements

### Dependencies
Ensure you have the following Python libraries installed:
```
pip install vosk python-docx
```

### Vosk Model
Download a Vosk model from [Vosk Models](https://alphacephei.com/vosk/models) and extract it to a directory on your system.

## Usage
1. Run the script:
   ```sh
   python speech_to_text.py
   ```
2. Enter the path to your WAV audio file.
3. Enter the path to the downloaded Vosk model.
4. The transcription will be saved in `transcript.docx`.

## Notes
- Ensure your audio file is in WAV format (mono, 16-bit PCM) before running the script.
- If the transcription fails, check the model path and audio format.

## License
This project is open-source and available under the MIT License.

