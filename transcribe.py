import sys
import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY = "API_KEY"
URL = "URL"

def get_content_type(file_path):
    file_extension = file_path.split('.')[-1].lower()
    content_type = None

    if file_extension == 'mp3':
        content_type = 'audio/mp3'
    elif file_extension == 'mp4' or file_extension == 'm4a':
        content_type = 'audio/mp4'
    elif file_extension == 'wav':
        content_type = 'audio/wav'
    else:
        print("Unsupported file format")
        sys.exit(1)

    return content_type

def transcribe_audio(file_path):
    authenticator = IAMAuthenticator(API_KEY)
    speech_to_text = SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(URL)

    content_type = get_content_type(file_path)

    with open(file_path, 'rb') as audio_file:
        result = speech_to_text.recognize(
            audio=audio_file,
            content_type=content_type
        ).get_result()

    return result

def save_transcription(result, output_path):
    with open(output_path, 'w') as output_file:
        for item in result['results']:
            output_file.write(item['alternatives'][0]['transcript'] + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transcribe.py <input_audio_file> <output_text_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        transcription = transcribe_audio(input_file)
        save_transcription(transcription, output_file)
        print("Transcription saved to", output_file)