from flask import Flask, send_from_directory, make_response
from flask import request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploaded/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route('/view')
def expose():
    path = UPLOAD_FOLDER
    fileList = os.listdir(path)
    if len(fileList) > 0:
        fname = fileList[0]

        resp = send_from_directory(path, fname)
        resp.headers['filename'] = fname

        os.remove(path + fname)

        return resp

    return "nothing here."

@app.route('/upload', methods = ['POST'])
def upload():
    if 'file' not in request.files:
        return 'no file uploaded'

    File = request.files['file']
    fn = secure_filename(File.filename)
    File.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))

    return "Uploaded"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
