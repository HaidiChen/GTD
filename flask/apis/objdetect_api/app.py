from flask import Flask, send_from_directory, make_response
from flask import request
from werkzeug.utils import secure_filename
import os
from yolo import detect
from stitch import stitch

UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/detect', methods = ['POST'])
def obj_detect():
    if 'file' not in request.files:
        return 'no image file uploaded'

    File = request.files['file']

    # can check extension here before detecting
    if File.filename == '':
        return 'no file name provided'

    if File and allowed_file(File.filename):
        fn = secure_filename(File.filename)
        File.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))

        imagePath = os.path.join(app.config['UPLOAD_FOLDER'], fn)
        detect(imagePath)

        resp = send_from_directory(UPLOAD_FOLDER, fn)
        resp.headers['filename'] = fn

        os.remove(imagePath)

        return resp
    else:
        return 'file type is not supported'

@app.route('/stitch', methods = ['POST'])
def img_stitch():
    STITCH_FOLDER = 'stitch/'

    if 'file' not in request.files:
        return 'no images uploaded'

    File = request.files.getlist('file')

    if any(f.filename == '' for f in File):
        return 'file name needed'

    for file in File:
        if allowed_file(file.filename):
            fn = secure_filename(file.filename)
            file.save(os.path.join(STITCH_FOLDER, fn))
            
    img_extension = os.listdir(STITCH_FOLDER)[0].rsplit('.', 1)[1]
    output = STITCH_FOLDER + 'result.' + img_extension

    if stitch(STITCH_FOLDER, output):
        resp = send_from_directory(STITCH_FOLDER, 'result.' + img_extension)
        resp.headers['filename'] = fn

#        os.remove(output)
        files = os.listdir(STITCH_FOLDER)
        for file in files:
            os.remove(STITCH_FOLDER + file)

        return resp
    else:
        return 'stitching failed'

@app.route('/upload', methods = ['POST'])
def upload():
    if 'file' not in request.files:
        return 'no file uploaded'

    File = request.files['file']
    fn = secure_filename(File.filename)
    File.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))

    return 'uploaded'

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
