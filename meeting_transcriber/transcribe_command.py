import typer
from pathlib import Path

from meeting_transcriber.audio_transcribe import transcribe_to_text_file

app = typer.Typer()


@app.command()
def transcribe(audio_file: Path, output: Path = Path("./transcription.txt")):
    """
    Transcribe an audio file to text and write it to the output.
    """
    transcription = transcribe_to_text_file(audio_file, chunk_length=1, num_chunks=1)
    output.write_text(transcription)


if __name__ == "__main__":
    app()
