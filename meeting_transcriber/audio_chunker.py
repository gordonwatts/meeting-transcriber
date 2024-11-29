from pathlib import Path
from typing import Generator
from pydub import AudioSegment


def chunk_audio_file(
    audio_file: Path, chunk_duration_minutes: int = 20
) -> Generator[AudioSegment, None, None]:
    """
    Generator function that chunks an audio file into sections of specified minutes.

    :param audio_file: Path to the audio file.
    :param chunk_duration_minutes: Duration of each chunk in minutes. Default is 20 minutes.
    :return: Generator yielding AudioSegment objects of the specified duration.
    """
    audio = AudioSegment.from_file(audio_file)
    chunk_duration_ms = (
        chunk_duration_minutes * 60 * 1000
    )  # Convert minutes to milliseconds
    duration_ms = len(audio)  # Duration of the audio in milliseconds

    start = 0

    while start < duration_ms:
        end = start + chunk_duration_ms
        yield audio[start:end]
        start = end
