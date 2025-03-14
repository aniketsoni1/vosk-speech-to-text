import os
import json
import vosk
import wave
import docx

def recognize_audio(audio_filepath, model_path):
    """
    Recognizes speech from an audio file using Vosk.

    Args:
        audio_filepath (str): Path to the audio file.
        model_path (str): Path to the Vosk model directory.

    Returns:
        str: The transcribed text, or None if an error occurs.
    """
    if not os.path.exists(model_path):
        print(f"Error: Vosk model not found at '{model_path}'. Download from https://alphacephei.com/vosk/")
        return None

    if not os.path.exists(audio_filepath):
        print(f"Error: Audio file '{audio_filepath}' not found.")
        return None

    model = vosk.Model(model_path)

    try:
        with wave.open(audio_filepath, "rb") as wf:
            if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000, 32000, 44100]:
                print("Error: Unsupported audio format. Use mono WAV with 16-bit PCM.")
                return None

            rec = vosk.KaldiRecognizer(model, wf.getframerate())
            
            transcription = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    transcription += result.get("text", "") + " "
            
            final_result = json.loads(rec.FinalResult())
            transcription += final_result.get("text", "")
            
    except Exception as e:
        print(f"Error processing audio: {e}")
        return None
    
    return transcription.strip()

def save_transcription(transcription, output_file="transcript.docx"):
    """Saves the transcribed text into a DOCX file."""
    try:
        doc = docx.Document()
        doc.add_paragraph(transcription)
        doc.save(output_file)
        print(f"Transcription saved to {output_file}")
    except Exception as e:
        print(f"Error saving transcription: {e}")

if __name__ == "__main__":
    audio_filepath = input("Enter the path to your audio file: ").strip()
    model_path = input("Enter the path to your Vosk model: ").strip()
    
    transcription = recognize_audio(audio_filepath, model_path)
    
    if transcription:
        save_transcription(transcription)
    else:
        print("Transcription failed.")