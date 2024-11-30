import typer
from pathlib import Path

from meeting_transcriber.transcription_utils import (
    transcribe_and_clean_audio,
)

app = typer.Typer()


@app.command()
def transcribe(audio_file: Path, output: Path = Path("./transcription.txt")):
    """
    Transcribe an audio file to text and write it to the output.
    """
    text = transcribe_and_clean_audio(audio_file)
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    app()
