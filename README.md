# 🚀 MidJourney Discord Automation Bot
![github-getmidjourney](https://github.com/user-attachments/assets/9226cf8c-38b7-4863-8432-4ef173f81958)

## 📖 Table of Contents

- [📌 Features](#-features)
- [🛠 Prerequisites](#-prerequisites)
- [📦 Requirements](#-requirements)
- [⚙️ Configuration](#-configuration)
- [▶️ Usage](#-usage)
- [📝 Notes](#-notes)
- [📜 License](#-license)

This Python script automates sending prompts to MidJourney's Discord bot and downloading the upscaled images using Selenium and cURL.

## 📌 Features

- Automatically logs into Discord.
- Sends prompts from a `prompts.txt` file.
- Automatically clicks the upscale buttons (U1, U2, U3, U4) and downloads the upscaled images.

## 🛠 Prerequisites

- Python 3.x installed ([Download Python](https://www.python.org/downloads/))
- Google Chrome installed ([Download Chrome](https://www.google.com/chrome/))
- Chrome WebDriver ([Download Here](https://googlechromelabs.github.io/chrome-for-testing/))
- MidJourney bot added to your Discord server

## 📦 Requirements

### Install Dependencies

Ensure you have Python installed, then install the required dependencies:

```sh
pip install -r requirements.txt
```

### WebDriver Setup

Download and install the Chrome WebDriver compatible with your Chrome version:

- [ChromeDriver Download](https://googlechromelabs.github.io/chrome-for-testing/)
- Place the WebDriver in the project directory or set it in your system PATH.

## ⚙️ Configuration

1. **Set Chrome Profile Path:**

   - Open Chrome and navigate to `chrome://version/`
   - Copy the "Profile Path" and replace it in the script:

   ```python
   options.add_argument(r'--user-data-dir=C:\Users\Username\AppData\Local\Google\Chrome\User Data\Default')
   ```

2. **Modify Discord Channel URL:**

   - Replace the Discord URL with your channel's link:

   ```python
   driver.get("https://discord.com/channels/@me")
   ```

## ▶️ Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/kadangkesel/get_midjourney
   ```
2. Navigate into the project directory:
   ```sh
   cd get_midjourney
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `prompts.txt` file and add your prompts (one per line).
5. Run the script:
   ```sh
   python bot.py
   ```
6. The script will send prompts, wait for responses, upscale images, and save them to the `downloads` folder.

## 📝 Notes

- Ensure MidJourney Bot is added to your Discord channel.
- The script depends on the Discord UI structure; if it changes, XPaths may need updating.

## 📜 License

MIT License

Copyright (c) 2025 kadang_kesel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

