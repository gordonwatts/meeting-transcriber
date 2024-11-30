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

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        const response = await fetch('/transcribe', { // Removed trailing slash
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Transcription failed.');
        }

        const result = await response.json();
        document.getElementById('transcriptionResult').textContent = result.transcription;
    } catch (error) {
        alert(error.message);
    }
}