import base64
import cv2
import tempfile
import math
import anthropic
from IPython.display import Image, display
import os
# Anthropic APIキーとクライアントの準備
os.environ["ANTHROPIC_API_KEY"] = ""

client = anthropic.Anthropic()

# Function to encode the image
def encode_image(image):
    _, buffer = cv2.imencode(".jpg", image)
    return base64.b64encode(buffer).decode('utf-8')

with tempfile.NamedTemporaryFile(suffix=".mp4") as f:
    video = cv2.VideoCapture("*.mp4")
    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        base64Frames.append(encode_image(frame))

    video.release()
    print(len(base64Frames), "frames read.")

if len(base64Frames) > 0:
    prompt_ms = """
    """

    segment_duration = 30
    num_segments = math.ceil(len(base64Frames) * 0.025 / segment_duration)

    for segment in range(num_segments):
        start_frame = segment * segment_duration * 40
        end_frame = (segment + 1) * segment_duration * 40

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_ms
                    },
                    *[{
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": frame
                        }
                    } for frame in base64Frames[start_frame:end_frame:60]]
                ]
            }
        ]

        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=500,
            messages=messages
        )

        comment = response.content

        print(f"[{segment * segment_duration:02d}:00] {comment}")
else:
    print("動画ファイルが空であるか、読み込みに失敗しました。")
