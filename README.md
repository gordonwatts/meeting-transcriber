# Meeting-Transcriber

Experimental project to process audio files from meetings and generate transcriptions and summaries.

## Usage

`transcribe <file.mp4>`

Result will be in transcription.txt.

To start a webapi (and PWA) running on port 8001:

`transcribe_app --port 8001`

And then open your browser at 8001 to see the interface. You can also get the docs by looking at the localhost link for docs, <http://localhost:8001/docs>.

## Goals

This is experimental and has several goals:

* [x] Take a typical Zoom meeting audio file (.mp4)
* [x] Use a model to transcribe it (e.g Whisper or similar)
  * [x] Understand how acronyms can be improved
* [ ] Have a very simple web interface that runs locally on a desktop that allows you to drag/drop the file, etc.
  * Time to see if there is an easy way to move away from command line for things that are immediately useful.
* [ ] Make it so we can have the "backend" sitting on another machine
  * Can't have this setup on every laptop as I travel!

## Installation

I've only tested this on WSL on windows.

1. Make sure ffmpeg is installed (required for audio editing and loading and transcription):
  `apt-get install ffmpeg libavcodec-extra`
1. Use `pip install -e .[test]`
