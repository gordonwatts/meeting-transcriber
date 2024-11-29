from pathlib import Path
from typing import Optional
from .audio_chunker import chunk_audio_file
from .util import load_openai_api_key
import tempfile
from openai import OpenAI
import diskcache as dc

cache = dc.Cache("/tmp/transcription_cache")


@cache.memoize()
def transcribe_to_text_file(
    audio_file: Path, num_chunks: Optional[int] = None, chunk_length: int = 20
) -> str:
    """Given an audio file, use a model to transcribe it.

    Args:
        audio_file (Path): The audio file to transcribe.
        num_chunks (int, optional): The number of chunks to process. If None, process all chunks.
        chunk_length (int, optional): The length of each chunk in minutes. Defaults to 20 minutes.

    Returns:
        str: The transcribed text.
    """
    transcription = ""
    load_openai_api_key()
    client = OpenAI()

    for i, chunk in enumerate(chunk_audio_file(audio_file, chunk_length)):
        if num_chunks is not None and i >= num_chunks:
            break
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
            chunk.export(tmp_file.name, format="mp3")
            with open(tmp_file.name, "rb") as audio:
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio,
                    response_format="text",
                    prompt="This is a meeting in the ATLAS experiment. Some common Acronyms "
                    "are ATLAS, CERN, LHC, AMG, OTP.",
                )
                transcription += response + " "

    return transcription.strip()
