import os
from flask import Flask, flash, request, redirect ,render_template, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['SECRET_KEY'] = 'webdevround2'

UPLOAD_FOLDER = '/Users/anujpatel/Coding/Python'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

valid_extensions = {'csv'}

def valid_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in valid_extensions

@app.route('/', methods=['GET'])
def index():
    return render_template("home.html", messages=[])

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file uploaded')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('There are no files selected')
        return redirect(request.url)
    
    if file and valid_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File uploaded successfully')
    else:
        flash('Invalid file type. Please upload CSV files only.')
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)