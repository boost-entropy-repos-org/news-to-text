from google.cloud import texttospeech
from google.cloud import storage

client = texttospeech.TextToSpeechClient()


def text_to_speech(text, filename):
    if len(text) > 5000:
        print('cannot send more than 5k chars, concatenating')
        text = text[:5000]
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL
    )

    audo_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(synthesis_input, voice, audo_config)

    # filename = 'outuput.mp3'
    filename = filename + '.mp3'
    with open(filename, 'wb') as out:
        out.write(response.audio_content)
        print('written output as {filename}')

    upload_to_gcp(filename)


def upload_to_gcp(source):
    storage_client = storage.Client()
    bucket = storage_client.bucket('storytime-audio')

    blob = bucket.blob(source)
    blob.upload_from_filename(source)

    print("File {} uploaded to {}".format(source, source))
