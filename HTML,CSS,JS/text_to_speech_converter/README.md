# Text to Speech Converter

### This is a simple web-based text-to-speech (TTS) application that allows users to convert text into speech. It utilizes the Web Speech API's SpeechSynthesis interface to provide the text-to-speech functionality. The user can select a voice from the available list of voices in the browser and listen to the text they input in a text area.

## Features

* Text-to-Speech: Convert any input text into speech using the browser's built-in speech synthesis engine.
* Voice Selection: Choose from a list of available voices on your system.
* User Interaction: Input text into a textarea and click a button to listen to the speech.


## How it Works

* The script initializes a SpeechSynthesisUtterance object, which is responsible for the speech output.
* It fetches available voices using window.speechSynthesis.getVoices() and populates a dropdown (select element) with these voices.
* When the user selects a different voice, the voice of the SpeechSynthesisUtterance is updated accordingly.
* When the user clicks the "Speak" button, the text entered in the textarea is spoken using the selected voice.

# Prerequisites

* This application relies on the Web Speech API, which is supported in most modern browsers (such as Chrome, Firefox, Safari, and Edge).
* Ensure that your browser has access to the system voices, as the list of available voices may vary depending on the operating system and browser.


## Files

* index.html: The HTML structure for the demo page.
* style.css (Optional): You can add your own custom styles for the page.
* script.js: The JavaScript code that powers the text-to-speech functionality.
