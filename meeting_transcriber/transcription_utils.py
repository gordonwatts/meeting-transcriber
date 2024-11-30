from pathlib import Path
import openai  # Import OpenAI library
from meeting_transcriber.audio_transcribe import transcribe_to_text_file
from meeting_transcriber.util import load_openai_api_key
from diskcache import Cache

# Initialize cache
cache = Cache("/tmp/transcription_cleanup_cache")


@cache.memoize()
def clean_and_format_transcription(transcription: str) -> str:
    """
    Clean up and format the transcription in markdown format using OpenAI's gtp-4o-mini.
    """
    # Load OpenAI API key
    load_openai_api_key()

    # Initialize OpenAI client
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who is cleaning up and formatting a "
                "audio meeting transcription.",
            },
            {
                "role": "user",
                "content": "Clean up and format the following transcription in markdown format "
                "for easy readability: \n\n" + transcription,
            },
        ],
    )
    return str(response.choices[0].message.content).strip()


def transcribe_and_clean_audio(audio_file: Path) -> str:
    """
    Transcribes an audio file and cleans the resulting transcription.
    This function takes an audio file, transcribes it to text, cleans and formats the
    transcription, and returns the cleaned transcription.

    Args:
        audio_file (Path): The path to the audio file to be transcribed.

    Returns:
        str: The cleaned transcription.
    """

    transcription = transcribe_to_text_file(audio_file)
    return clean_and_format_transcription(transcription)
