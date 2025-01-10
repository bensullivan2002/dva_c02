import boto3

polly = boto3.client("polly")

result = polly.synthesize_speech(
    Text="Hello world", OutputFormat="mp3", VoiceId="Joanna"
)

audio = result["AudioStream"].read()

with open("output.mp3", "wb") as f:
    f.write(audio)
