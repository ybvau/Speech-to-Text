# Speech-to-Text tool.
## Stack: Terminal, Python, IBM Watson API, Web browser (for spinning the instance: easy)
### Let me know if I missed anything!

To use IBM Watson Speech to Text service to transcribe an audio file and save the result in a .txt file, follow these steps:

### Create an account:
Sign up for an IBM Cloud account or sign in to your existing one: https://cloud.ibm.com/

### Create an instance:
Create an instance of the Speech to Text service: https://cloud.ibm.com/catalog/services/speech-to-text

### Get the API key and URL:
Go to the "Manage" tab of your Speech to Text service instance and note down the API Key and URL.

### Install the Watson SDK:
You will need to install the IBM Watson SDK for Python. You can do this using pip:
```pip3 install ibm-watson```

## Transcribe the audio:
Run the script using the following command in the terminal:
```python transcribe.py <input_audio_file> <output_text_file>```
Replace <input_audio_file> with the path to your audio file and <output_text_file> with the path to the desired output .txt file.

The script will transcribe the audio file and save the result in a .txt file.

Note: The sample code assumes the audio file is in the MP3 format. If you have a different format, change the content_type parameter in the recognize method accordingly. For example, for a WAV file, use content_type='audio/wav'.

## Using the Tool
Run the file using this method:
```python transcribe.py <input_audio_file> <output_text_file>```

Replace <input_audio_file> with the path to your audio file and <output_text_file> with the path to the desired output .txt file.

The script will transcribe the audio file and save the result in a .txt file.

Note: The sample code assumes the audio file is in the MP3 format. If you have a different format, change the content_type parameter in the recognize method accordingly. For example, for a WAV file, use content_type='audio/wav'.

## How to find Path Location
Open Finder and navigate to the file.
Hold the 'Option' key and right-click on the file.
Click on 'Copy ... as Pathname'. The file path will be copied to your clipboard.

When running the transcribe.py script, provide the full path to the input file, and the output text file will be saved in the same directory as the input file if you don't provide a path in the output file name. For example:


```python transcribe.py /path/to/your/input_audio_file.mp3 /path/to/your/output_text_file.txt```

This will save the output_text_file.txt in the same directory as the input audio file. If you want to save the output file in a different directory, provide the full path for the output file:

```python transcribe.py /path/to/your/input_audio_file.mp3 /path/to/your/output_text_file.txt```

This will save the output_text_file.txt in the specified directory.