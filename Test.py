from flask import Flask, request
import subprocess
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'
  
@app.route('/start')
def start():
    browser = request.args.get('browser')
    URL = request.args.get('url')
    # return URL
    if browser=="chrome":
        subprocess.call([chrome_path,'-new-window', URL])
    elif browser=="firefox":
        subprocess.call([firefox_path,'-new-window', URL])
    return ""
    #return ('Hello from Server')
@app.route('/stop')
def stop():
    browser = request.args.get('browser')
    if browser=="chrome":
        os.system("taskkill /im chrome.exe /f")
    elif browser=="firefox":
        os.system("taskkill /im firefox.exe /f")
    return ""

if __name__ == '__main__':
    chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
    firefox_path="C:\Program Files\Mozilla Firefox\Firefox.exe"
    app.run()