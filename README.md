# Text To Speech

This Python script converts the text from a PDF file into spoken audio using the `pyttsx3` text-to-speech engine and saves the output as an audio file (WAV or MP3).

## Features

- **Interactive Voice Selection:** Lists all available system voices/languages for you to choose from.
- **PDF Text Extraction:** Reads and extracts text from every page in a selected PDF.
- **Custom Output:** Lets you specify the filename and location of the output audio file.
- **Offline Processing:** No internet connection required.
- **Simple GUI file picker:** Uses a file dialog to select your PDF file.

## Requirements

Install dependencies with pip:

```
pip install pyttsx3 PyPDF2
```

> **Note:** On macOS and Linux, you may need additional TTS voices or audio libraries for functionality. On Windows, most voices work out-of-the-box.

## Usage

You will be prompted to:

1. **Select the PDF** you want to record.
2. **Choose a voice/language** from the printed list by entering its number.
3. **Specify the output audio file name** (e.g., `output.wav` or `output.mp3`).
4. Wait for the script to finish processing. The audio will be saved alongside the script.

## Example

```
Available voices/languages:
0: Name: Microsoft David Desktop, Lang: ['en_US'], ID: HKEY_LOCAL_MACHINE\...
1: Name: Microsoft Zira Desktop, Lang: ['en_US'], ID: HKEY_LOCAL_MACHINE\...
Enter the number of the voice/language you want to use: 1
Enter the output audio file name (e.g., audio.wav / audio.mp3): my_book_audio.mp3
Audio saved at /path/to/my_book_audio.mp3
```

## How it works

- Uses `tkinter.filedialog` to open a file picker for your PDF.
- Extracts text from all PDF pages using `PyPDF2`.
- Cleans up text formatting (removes unnecessary single newlines).
- Lists all available `pyttsx3` voices.
- Converts the extracted text to speech and saves it as an audio file.

## Limitations

- The quality and language of voices are determined by your system's installed TTS voices.
- PDF text extraction may not work perfectly for scanned documents or PDFs without selectable text.
- Large PDFs may take longer to process.

## License

MIT

## Credits

- [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
- [pypdf2]https://pypdf2.readthedocs.io/en/3.x/
