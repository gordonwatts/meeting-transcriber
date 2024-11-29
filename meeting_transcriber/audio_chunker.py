from pathlib import Path
from typing import Generator
from pydub import AudioSegment


def chunk_audio_file(audio_file: Path) -> Generator[AudioSegment, None, None]:
    """
    Generator function that chunks an audio file into 20 MB sections.

    :param audio_file: Path to the audio file.
    :return: Generator yielding AudioSegment objects of 20 MB each.
    """
    audio = AudioSegment.from_file(audio_file)
    chunk_size_bytes = 20 * 1024 * 1024  # 20 MB in bytes
    total_size_bytes = len(audio.raw_data)
    duration_ms = len(audio)  # Duration of the audio in milliseconds
    chunk_size_ms = (chunk_size_bytes / total_size_bytes) * duration_ms

    start = 0

    while start < duration_ms:
        end = start + chunk_size_ms
        yield audio[start:end]
        start = end
