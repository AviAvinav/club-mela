import os
import subprocess
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    if request.method == "POST":
        pythoninput = request.form.get("input")
        if checkInput(pythoninput) == True:
            result = subprocess.run(["python3", "-c", pythoninput], stdout=subprocess.PIPE, text=True)
            return render_template('index.html', value1=result.stdout)
        else:
            return render_template('err0r.html')

def checkInput(a):
    check = True
    for x in ['open','os','system','read','write','exec']:
        if x in a:
            check = False
    return check

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)