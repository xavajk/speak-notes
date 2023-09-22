# SpeakNotes

# Introduction

This repository is a Python program that uses [**gTTS**](https://pypi.org/project/gTTS/) (Google Text-to-Speech) and the [**SpeechRecognition**](https://pypi.org/project/SpeechRecognition/) library to quickly and effectively create, read, update, and delete tasks consolitdated within your Notion workspace.

# Requirements

The requirements for this repository can be found in requirements.txt. Once a virtual environment is activated, run `pip3 install -r requirements.txt` on MacOS, or `pip install -r requirements.txt` on other machines.

# Usage

There are two quick and easy steps to get this program running on your machine:

1. The first step is to add your own environment variables. To do this, once the repository is cloned to your machine, look for the **.env.example** file. Once it’s located, fill in the fields `NOTION_INTEGRATION_TOKEN` and `NOTION_DB_NAME`. The first can be obtained after [**creating an integration for your Notion page**](https://developers.notion.com/docs/create-a-notion-integration). Next, with the Notion database page open in a browser, copy the sequence of characters after the final forward slash and before the ‘?v’. (e.g. ~~notion/~~ **11b2g81g12a6281cc408e9073** ~~?v=e1a92913fajf2d6ecb678e124b50e~~ ). Note: you’ll want to change ‘**.env.example**’ to simply ‘**.env**’.
2. Then, if you are using MacOS, simply run `python3 main.py` in the terminal. If you are using any other operating system run `python main.py` in the terminal or command prompt.

Once the program is run, “Listening…” will be printed to the console showing that it is idle and actively listening for the activation command. The program is hard-coded with “Make a note” as the activation command but this can be changed to anything. After the command is received, sound acknowledgement will be played to the user and the content of the note will be added to the Notion page with the date and time it was added. The default status is Not started.

In future commits, the ability to read, update, and delete these notes will also be supported.
