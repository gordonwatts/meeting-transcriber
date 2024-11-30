from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from meeting_transcriber.transcription_utils import transcribe_and_clean_audio
import uvicorn
import hashlib
import os
import typer

app = FastAPI()
cli = typer.Typer()


@app.post("/api/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcribe and summarize the provided audio file.

    The file can be in `mp3` or `wav` format. This endpoint will transcribe the audio
    and summarize it, assuming it is a meeting.

    Args:
        file (UploadFile): The audio file to be transcribed.

    Returns:
        dict: A dictionary containing the transcription of the audio. The
              `transcription` key will contain the transcription of the audio.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided.")

    temp_file = Path("/tmp") / file.filename
    with temp_file.open("wb") as f:
        f.write(await file.read())

    # Generate a hash for the filename
    hash_object = hashlib.sha256(file.filename.encode())
    hashed_filename = hash_object.hexdigest()
    hashed_temp_file = temp_file.with_name(hashed_filename)

    # Rename the file to the hashed filename
    temp_file.rename(hashed_temp_file)

    try:
        transcription = transcribe_and_clean_audio(hashed_temp_file)
        return {"transcription": transcription}
    finally:
        # Ensure the temporary file is deleted
        if hashed_temp_file.exists():
            os.remove(hashed_temp_file)


# Serve static files
app.mount("/", StaticFiles(directory="web", html=True), name="web")


@cli.command()
def main(port: int = 8000):
    """
    Run the FastAPI app.

    Args:
        port (int): The port number to run the app on.
    """
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    cli()
