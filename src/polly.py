import boto3

polly = boto3.client("polly")

result = polly.synthesize_speech(
    Text="Hello, good looking!",
    OutputFormat="mp3",
    VoiceId="Amy",
    Engine="neural",
)

audio = result["AudioStream"].read()

with open("output.mp3", "wb") as f:
    f.write(audio)
