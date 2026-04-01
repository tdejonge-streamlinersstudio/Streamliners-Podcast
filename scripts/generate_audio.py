import requests
import os

# Function to generate audio using ElevenLabs API

def generate_audio(script, voice_id, api_key):
    url = f'https://api.elevenlabs.io/v1/voice/{voice_id}/synthesize'
    headers = {
        'xi-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'text': script,
        'voice_id': voice_id
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception('Audio generation failed: ' + response.text)

# Function to save the audio file

def save_audio_file(audio_content, filename):
    with open(filename, 'wb') as audio_file:
        audio_file.write(audio_content)

# Function to handle the podcast's intro and outro

def handle_intro_outro(main_audio, intro_audio, outro_audio):
    final_audio = intro_audio + main_audio + outro_audio
    return final_audio

# Main execution flow

def main():
    # Set up your podcast script and API configuration
    podcast_script = "Your podcast script goes here."
    voice_id = "your_voice_id"
    api_key = os.environ.get('ELEVENLABS_API_KEY')

    try:
        audio_content = generate_audio(podcast_script, voice_id, api_key)
        save_audio_file(audio_content, 'podcast.mp3')
        print('Podcast audio has been generated and saved as podcast.mp3')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()