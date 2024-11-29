from pathlib import Path
from typing import Optional
from .audio_chunker import chunk_audio_file
from .util import load_openai_api_key
import tempfile
from openai import OpenAI


def transcribe_to_text_file(
    audio_file: Path, output: Path, num_chunks: Optional[int] = None
):
    """Given an audio file, use a model to transcribe it.

    Args:
        audio_file (Path): The audio file to transcribe.
        output (Path): The output file to write the transcription to.
        num_chunks (int, optional): The number of chunks to process. If None, process all chunks.
    """
    transcription = ""
    load_openai_api_key()
    client = OpenAI()

    for i, chunk in enumerate(chunk_audio_file(audio_file, 1)):
        if num_chunks is not None and i >= num_chunks:
            break
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
            chunk.export(tmp_file.name, format="mp3")
            with open(tmp_file.name, "rb") as audio:
                response = client.audio.transcriptions.create(
                    model="whisper-1", file=audio, response_format="text"
                )
                transcription += response + "\n"

    with open(output, "w") as f:
        f.write(transcription.strip())
