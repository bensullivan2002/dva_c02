import boto3
import os
import dotenv

dotenv.load_dotenv()

polly = boto3.client(
    "polly",
    region_name="eu-west-2",
    aws_access_key_id=os.environ["USERNAME"],
    aws_secret_access_key=os.environ["PASSWORD"],
)

result = polly.synthesize_speech(
    Text="Hello world", OutputFormat="mp3", VoiceId="Aditi"
)

audio = result["AudioStream"].read()

with open("output.mp3", "wb") as f:
    f.write(audio)
