from flask import Flask, request, render_template,jsonify
from vision_crawl import url2screenshot, visionExtract

app = Flask(__name__,template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    if request.method == 'POST':
        url = request.form.get('url')
        question = request.form.get('question')
        b64_image = url2screenshot(url)
        response = visionExtract(b64_image, question)
        response=response
        return jsonify(response=response)
    return render_template('index.html')
        
    # return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)