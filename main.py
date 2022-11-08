from flask import Flask, render_template, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads


app = Flask(__name__)
app.secret_key='secret_key'
app.config['UPLOADED_IMG'] = 'uploads'

photos = UploadSet('images', IMAGES)
configure_uploads(app, photos)

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_IMG'], filename)

@app.route('/', methods=['GET', 'POST'])
def upload():
    filename = photos.save(photos.data)
    file_url = url_for('get_file', filename=filename)
    return render_template('index.html', file_url=file_url)

if __name__ == '__main__':
    app.run(debug=True)

