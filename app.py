from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/main')
def main():
    return render_template('sitio/main.html')

@app.route('/cursos')
def cursos():
    return render_template('sitio/cursos.html')

@app.route('/servicos')
def servicos():
    return render_template('sitio/servicos.html')

@app.route('/videos')
def videos():
    return render_template('sitio/videos.html')

@app.route('/hallelujah')
def hallelujah():
    return render_template('sitio/hallelujah.html')

@app.route('/mensagens')
def mensagens():
    return render_template('sitio/mensagens.html')

@app.route('/eventos')
def eventos():
    return render_template('sitio/eventos.html')

@app.route('/contato')
def contato():
    return render_template('sitio/contato.html')

@app.route('/photoshop')
def photoshop():
    return render_template('sitio/photoshop.html')

if __name__ == '__main__':
    app.run(debug=True)