import re
import requests
import json
import time

def generate_voice(text, filename):
    params = {
        'text': text,
        'speaker': 1,  # 話者の選択（1～4）
    }
    response1 = requests.post('http://localhost:50021/audio_query', params=params)
    headers = {'Content-Type': 'application/json',}
    params = {
        'speaker': 1,
    }
    response2 = requests.post(
        'http://localhost:50021/synthesis',
        headers=headers,
        params=params,
        data=json.dumps(response1.json())
    )

    with open(filename, 'wb') as f:
        f.write(response2.content)

script = """
[00:00] 'はいはい'
[00:30] 'こんにちは！'
"""

# 30秒ごとに区切るための正規表現パターン
pattern = re.compile(r"(.{1,200}?[。！？.\n])")

lines = script.strip().split('\n')
for line in lines:
    if line.strip() == '' or ']' not in line:
        continue
    
    timestamp, text = line.split(']', 1)
    timestamp = timestamp[1:]
    
    min, sec = map(int, timestamp.split(':'))
    
    # テキストを30秒ごとに分割
    segments = pattern.findall(text)
    for i, segment in enumerate(segments):
        start_time = i * 30
        end_time = (i + 1) * 30
        
        filename = f"line_{min}_{sec}_{start_time}_{end_time}.wav"
        generate_voice(segment, filename)
        
        time.sleep(1)  # voicevox APIへの連続リクエストを避けるため、1秒待機
