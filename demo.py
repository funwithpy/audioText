import assemblyai as aai
# replace with your API token
aai.settings.api_key = f"45fb00a050624830a4c29fa36e8da8dc"
# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)
print(transcript.text)
