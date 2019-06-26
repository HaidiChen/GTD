from flask import Flask, send_from_directory, make_response
from flask import request
from werkzeug.utils import secure_filename
import os
from yolo import detect

UPLOAD_FOLDER = 'images/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route('/detect', methods = ['POST'])
def obj_detect():
    if 'file' not in request.files:
        return 'no image file uploaded'

    File = request.files['file']

    # can check extension here before detecting
    # check_extension(file)

    fn = secure_filename(File.filename)
    File.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))

    imagePath = os.path.join(app.config['UPLOAD_FOLDER'], fn)
    detect(imagePath)

    resp = send_from_directory(UPLOAD_FOLDER, fn)
    resp.headers['filename'] = fn

#    os.remove(imagePath)

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
