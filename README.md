
# GPT4 Vision Web Crawler Tool
============================

## Introduction
This is a tool powered by GPT4 Vision API and Puppeteer that can answer questions based on website screenshots. You ask it a question, and it will browse to a website and take a screenshot. Then, it uses the GPT4 Vision API to answer the question based on the screenshot. The server uses a Flask API to communicate with the client. Users can input a URL and ask a question on the client side, and the server will return the answer to the client side. The client side will then display the answer on the page.

## Features
- [x] Browse to a website and take a screenshot
- [x] Use GPT4 Vision API to answer questions based on the screenshot
- [x] Use Flask API to communicate with the client
- [x] Display the answer on the client side



## Installation

Before you can run the tool, you need to install the required dependencies. Follow these steps:

1. Install the required npm packages. npm is a package manager for the JavaScript programming language. Run the following command in your terminal:

```bash
$ npm install
```

2. Install the required Python packages. pip is a package manager for Python. You can use it to install the Python packages listed in the requirements.txt file. Run the following command in your terminal:

```bash
$ pip install -r requirements.txt
```

3. After you have installed the dependencies, you can run the tool using the following command:
    
```bash
$ python3 webcrwalerbot.py
```




# Demo Screenshot
(Add your screenshot here)

# Demo Video
(Add your video link here)

## Packages Introduction-Puppeteer
Puppeteer is a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol. Puppeteer runs headless by default, but can be configured to run full (non-headless) Chrome or Chromium. 

## Packages Introduction-Flask
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.





