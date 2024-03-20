# ai-video-commentator

必要な環境
 ・ Python 3.11.8
 ・ FFmpeg
 ・ Voicevox

```
git clone https://github.com/yourusername/ai-video-commentator.git
cd ai-video-commentator
```
Voicevoxをインストールして起動します。
Voicevoxの公式ウェブサイト（https://voicevox.hiroshiba.jp/）
からお使いのOSに対応したVoicevoxエンジンをダウンロードしてインストールします。

Voicevoxエンジンを起動します。デフォルトでは、```localhost:50021```で動作します。

使用方法

```bash
python ai_video_commentator.py
```
以下のコマンドを実行して、生成されたコメントを音声ファイルに変換します。

```bash
python scripts/comment_to_speech.py
```

ai_video_commentator.pyスクリプトを変更することで、AIモデルやコメント生成のロジックをカスタマイズできます。
comment_to_speech.pyスクリプトを変更することで、音声合成のパラメータや音声ファイルの形式などを調整できます。
