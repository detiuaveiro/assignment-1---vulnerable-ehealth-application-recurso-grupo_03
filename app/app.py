from flask import Flask, render_template, request, redirect, url_for
from os import path, environ
import pymysql
from dotenv import load_dotenv

TEMPLATE_DIR = path.relpath('./templates')
app = Flask(__name__,template_folder=TEMPLATE_DIR)
load_dotenv(".env")

connection = pymysql.connect(host="localhost", port=5051, user='admin', password='admin', database='ecorp', cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM teste")
    #     result = cursor.fetchall()
    # return render_template('index.html', users=result)´
    return render_template('index.html')

@app.route('/checkdb')
def checkDB():
    with connection.cursor() as cursor:
        cursor.execute("SHOW STATUS")
        result = cursor.fetchall()
        return result


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
