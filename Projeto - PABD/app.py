from flask import Flask
import mysql.connector

app = Flask(__name__)

def conexaobd():
    return mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        senha = "labinfo",
        database = "ajudaibd"
    )

