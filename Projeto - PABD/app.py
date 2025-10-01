from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        senha = "labinfo",
        database = "ajudaibd"
    )
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        nascimento = request.form['nascimento']
        email = request.form['email']
        senha = request.form['senha']

        try:
            cursor.execute(
                "INSERT INTO usuarios (email, nome, telefone, nascimento, senha) VALUES (%s, %s, %s, %s, %s)",
                (email, nome, telefone, nascimento, senha)
            )
            db.commit()
            return "Usuário cadastrado com sucesso!"
        except mysql.connector.IntegrityError:
            return "Erro: email já cadastrado!"

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)