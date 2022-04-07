from flask import Flask, render_template, request
import db
from flask_ckeditor import CKEditor
from wtforms import TextAreaField

app =  Flask(__name__)
ckeditor = CKEditor(app)

@app.route('/test')
def test():
    db.db.collection.insert_one({"name":"Prathamesh"})
    return "DB Connected"

@app.route('/private')
def login():
    return render_template('./private.html')

@app.route('/private', methods=['POST'])
def login1():
    if request.form.get('user') == 'prathamesh.malage@marylandsmith.umd.edu' and request.form.get('pass') == 'Pratham@1234':
        return "<h1>Success</h1>"

@app.route('/blogs')
def blog():
    return render_template('./blogs.html')
if __name__ == '__main__':
    app.run()
