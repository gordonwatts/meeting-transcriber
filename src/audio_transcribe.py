from pathlib import Path
from .audio_chunker import chunk_audio_file


def transcribe_to_text_file(audio_file: Path, output: Path):
    """Given an audio file, use a model to transcribe it.

    Args:
        audio_file (Path): The audio file to transcribe.
        output (Path): The output file to write the transcription to.
    """
    for chunk in chunk_audio_file(audio_file):
        print("chunk")
