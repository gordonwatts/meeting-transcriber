const dropArea = document.getElementById('drop-area');
const fileElem = document.getElementById('fileElem');
let selectedFile = null;

dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dropArea.classList.add('highlight');
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('highlight');
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dropArea.classList.remove('highlight');
    const files = event.dataTransfer.files;
    handleFiles(files);
});

function handleFiles(files) {
    if (files.length > 0) {
        selectedFile = files[0];
        dropArea.querySelector('p').textContent = `File selected: ${selectedFile.name}`;
    }
}

async function transcribeAudio() {
    if (!selectedFile) {
        alert('Please select an audio file first.');
        return;
    }

    const transcribeButton = document.getElementById('transcribeButton');
    const dropArea = document.getElementById('drop-area');
    const copyButton = document.getElementById('copyButton');
    transcribeButton.disabled = true;
    dropArea.classList.add('disabled');

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        const response = await fetch('/api/transcribe', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Transcription failed.');
        }

        const result = await response.json();
        document.getElementById('transcriptionResult').textContent = result.transcription;
        copyButton.disabled = false; // Enable the copy button
    } catch (error) {
        alert(error.message);
    } finally {
        transcribeButton.disabled = false;
        dropArea.classList.remove('disabled');
    }
}

function copyToClipboard() {
    const transcriptionResult = document.getElementById('transcriptionResult');
    transcriptionResult.select();
    document.execCommand('copy');
    alert('Transcription copied to clipboard.');
}