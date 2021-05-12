from flask import Flask,render_template
from flask.globals import request
import os
from flask.helpers import make_response, send_from_directory, url_for

from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)

UPLOAD_FOLDER=os.path.join(os.path.dirname(__file__), 'static/file')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

files_list = []

@app.route("/",methods=["POST","GET"])
def welcome():
    if request.method=="GET":
        return render_template("Menu.html",files=files_list)
    else:
        print(request.files.get("file"))
        file = request.files.get("file")
        # 第二个参数要使用secure_filename.(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER,(file.filename)))
        files_list.append(file.filename)
        return redirect(url_for("welcome"))

@app.route('/download/<filename>',methods=["GET"])
def filedownload(filename):
    return send_from_directory(UPLOAD_FOLDER, filename.encode('utf-8').decode('utf-8'), as_attachment=True)


if __name__=="__main__":
    app.run(debug=1)