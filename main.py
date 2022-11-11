from flask import Flask, render_template, request
from detector import AnimalCLassifier
import os

app = Flask(__name__)

detector = AnimalCLassifier()

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        filename = request.files['image']
        file_path = "./uploads/" + filename.filename  
        filename.save(file_path)
        prediction, animal = detector.detect('uploads', filename.filename)
        return render_template('index.html', prediction=prediction, animal=animal)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)