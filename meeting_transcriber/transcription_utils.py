import openai  # Import OpenAI library
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
