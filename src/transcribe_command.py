import typer
from pathlib import Path

app = typer.Typer()


@app.command()
def transcribe(audio_file: Path, output: Path):
    """
    Transcribe an audio file to text and write it to the output.
    """
    # Placeholder for the transcription logic
    typer.echo(f"Transcribing {audio_file} to {output}")


if __name__ == "__main__":
    app()
