import typer
from pathlib import Path

from src.audio_transcribe import transcribe_to_text_file

app = typer.Typer()


@app.command()
def transcribe(audio_file: Path, output: Path = Path("./transcription.txt")):
    """
    Transcribe an audio file to text and write it to the output.
    """
    # Placeholder for the transcription logic
    transcribe_to_text_file(audio_file, output)


if __name__ == "__main__":
    app()
