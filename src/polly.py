import boto3

polly = boto3.client("polly")

result = polly.synthesize_speech(Text="From the Tuesday, April 16th, 1912 edition of The Guardian newspaper: The maiden voyage of the White Star liner Titanic, the largest ship ever launched ended in disaster. The Titanics tarted her trip from Southampton for New York on Wednesday. Late on Sunday night she struck an iceberg off the Grand Banks of Newfoundland. By wireless telegraphy she sent out signals of distress, and several liners were near enough to catch and respond to the call.", OutputFormat="mp3", VoiceId="Amy", Engine="neural")

audio = result["AudioStream"].read()

with open("output.mp3", "wb") as f:
    f.write(audio)
