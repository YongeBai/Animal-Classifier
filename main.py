from flask import Flask, render_template, request
from detector import AnimalCLassifier

app = Flask(__name__)

detector = AnimalCLassifier()

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        filename = request.files['image']
        file_path = "./uploads/" + filename.filename  
        filename.save(file_path)
        img = detector.detect('uploads', filename.filename)
        return render_template('index.html', img=img)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

