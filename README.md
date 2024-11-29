# Meeting-Transcriber

Experimental project to process audio files from meetings and generate transcriptions and summaries.

## Usage

`transcribe <file.mp4>`

Result will be in transcription.txt.

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

Use `pip install -e .[test]`
