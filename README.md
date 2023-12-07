GPT4 Vision Web Crawler Tool
This is a tool powered by GPT4 Vision API and Puppeteer that can answer questions based on website screenshots. You ask it a question, and it will browse to a website and take a screenshot. Then, it uses the GPT4 Vision API to answer the question based on the screenshot. The server uses a Flask API to communicate with the client. Users can input a URL and ask a question on the client side, and the server will return the answer to the client side. The client side will then display the answer on the page.

Python Version
The Python version (vision_crawl.py) is the original version that opens one URL at a time. The Python version also uses JavaScript for the Puppeteer part.

Installation
First, you need to install the required npm and pip packages. You can install them using the following commands:

$ npm install
$ pip install -r requirements.txt

Then, you can run webcrwalerbot.py using the following command:
$ python3 webcrwalerbot.py


Demo Screenshot
(Add your screenshot here)

Demo Video
(Add your video link here)

Packages Introduction-Puppeteer
Puppeteer is a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol. Puppeteer runs headless by default, but can be configured to run full (non-headless) Chrome or Chromium.


