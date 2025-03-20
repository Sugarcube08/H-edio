# H-Edio: Bulk Audio Volume Adjustment Script 🎶🔊

**H-Edio** is a Python script designed to help you easily **increase or decrease the volume** of audio files in bulk. Whether you're working with `.mp3`, `.wav`, or `.ogg` files, this program allows you to apply a volume adjustment to all audio files in a specified folder, based on a **percentage input**.

## 🚀 Features:
- **Bulk Processing**: Adjust the volume of multiple audio files in a folder at once. 🔄
- **Custom Volume Adjustment**: Increase or decrease volume by a percentage (e.g., `100` for a 100% increase, `-50` for a 50% decrease). 📈📉
- **Supports Common Audio Formats**: Works with `.mp3`, `.wav`, and `.ogg` audio files. 🎵
- **Simple and Easy to Use**: Just input the folder path and the percentage to adjust the volume. 🛠️

## 🖥️ Requirements:
- **Python 3.x** 🐍
- Dependencies listed in the `requirements.txt` file 📦
- **ffmpeg** (or `libav`) installed on your system for `pydub` to handle various audio formats. 🎬

### 🔧 Installing Required Libraries
To install the necessary dependencies, use `pip` to install from the `requirements.txt` file:

```
pip install -r requirements.txt
```
You also need to install FFmpeg for pydub to process audio files correctly. You can download FFmpeg from here and follow the installation instructions for your operating system.

🚶 How to Use:

1. Clone or Download the Repository 📥

If you haven't already, clone or download the repository.
```
git clone http://github.com/sugarcube08/H-Edio
cd H-Edio
```

Here's the updated section with the code block included:

2. Installing Required Libraries🔧

To install the necessary dependencies, use pip to install from the requirements.txt file:
```
pip install -r requirements.txt
```
3. Run the Script ▶️

Run the script using Python:
```
python run-edio.py
```
4. Provide Input 📝

Folder Path: The script will ask for the path to the folder containing the audio files. 📂

Percentage: Provide the percentage by which you want to adjust the volume (e.g., 100 for a 100% increase, -50 for a 50% decrease). 🎚️


Example:

If you want to increase the volume by 50%, you would input 50 📈.

To decrease the volume by 30%, you would input -30 📉.


The script will process all compatible audio files in the folder and adjust the volume accordingly. 🎶

🛠️ How It Works:

1. Volume Calculation: The script converts the percentage to decibels (dB). For example:

100% → +6 dB (doubling the volume) 🔊

50% → +3 dB

-50% → -3 dB



2. Processing: It then loads each audio file, applies the volume change, and saves the modified files back to the same folder. 📁



🐞 Troubleshooting:

Error: If the script doesn't work correctly, make sure FFmpeg is installed and accessible in your system's PATH. 🔄

Unsupported Formats: Currently, the script only supports .mp3, .wav, and .ogg formats. You can modify the script to add support for other formats if necessary. 🎧



---
## Made with ❤️ by SugarCube.
---
Feel free to customize the repository and use it for your own bulk audio volume adjustments! 😄🎶

---
## ☕ Support Me
If you like this project, consider buying me a coffee!
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20Me-orange?style=flat-square&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/sugarcube08)
---


