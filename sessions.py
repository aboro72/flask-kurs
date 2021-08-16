from flask import Flask, url_for, request, redirect, render_template, make_response, escape, session
from werkzeug.utils import secure_filename
import os

folder = "D:/PyCharmProjekt/flask-kurs/uploads"
extensions = set(['txt', 'rar', 'jpg', 'png', 'pdf', 'doc', 'docx'])

app = Flask(__name__)


def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions




@app.route("/", methods=['GET', 'POST'])
def sessions():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(request.url)
    else:
        if 'name' in session:
            return "Hallo " + escape(session['name'])
        else:
            return '''
                <form method="post">
                    <p><input type=text name=name>
                    <p><input type=submit value=login>
                </form>
            
            '''


app.secret_key = "b'\xces\xb3?\xcd\xbb\x02\x0e_%\x8b\x0bs[\xadPn\x924U\xe8\x822\xe7'"


@app.route("/logout")
def logout():
    session.pop('name', None)
    return redirect(url_for('sessions'))


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if allowed(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            return redirect(request.url)

    return '''
        <h1>Upload</h1>
        <form method=post  enctype=multipart/from-data>
        <input type=file name=file>
        <input type=submit  value=Upload >
    '''


@app.route("/login", methods=['POST', 'GET'])
def login():
    cookie = request.cookies.get('username')
    if cookie is not None:
        return "Hallo " + cookie
    if request.method == 'POST':
        name = request.form['name']

    else:
        name = request.args.get('name')

    resp = make_response("Hello " + name + "!")
    resp.set_cookie('username', name)
    return resp


if __name__ == "__main__":
    app.run(port=1337, debug=True)
