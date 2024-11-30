from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
from meeting_transcriber.transcription_utils import transcribe_and_clean_audio
import uvicorn

app = FastAPI()


@app.post("/transcribe/")
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
    transcription = transcribe_and_clean_audio(temp_file)
    return {"transcription": transcription}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
