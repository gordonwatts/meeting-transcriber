import typer
from pathlib import Path

from meeting_transcriber.audio_transcribe import transcribe_to_text_file
from meeting_transcriber.transcription_utils import (
    clean_and_format_transcription,
)

app = typer.Typer()


@app.command()
def transcribe(audio_file: Path, output: Path = Path("./transcription.txt")):
    """
    Transcribe an audio file to text and write it to the output.
    """
    transcription = transcribe_to_text_file(audio_file, chunk_length=1, num_chunks=1)
    cleaned_transcription = clean_and_format_transcription(transcription)
    output.write_text(cleaned_transcription, encoding="utf-8")


if __name__ == "__main__":
    app()
