from flask import Flask
from flask import request 
from flask import render_template
from flask import redirect
from flask import url_for
from database import db_session
from werkzeug.utils import secure_filename



from database import Database
from database import engine


import models
import os

app = Flask(__name__)

SESSION_TYPE = 'filesystem'
PROFILE_PICTURES_FOLDER = 'static/archivos'
ALLOWED_IMAGE_TYPES = ['png', 'jpg', 'jpeg','JPEG', 'JPG ']
SECRET_KEY = 'dmo5S4DxuD^9IWK1k33o7Xg88J&D8fq!'


def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_IMAGE_TYPES:
        return True
    
def lista_Archivos():
    urlFiles = 'static/archivos'
    return(os.listdir(urlFiles))  

Database.metadata.create_all(engine)



@app.get('/')
def index():
    peliculas = db_session.query(models.Peliculas)
    return render_template('index.html', peliculas = peliculas)


@app.get('/agregar')
def agregar():
    return render_template('agregar.html')

@app.post('/agregar/pelicula')
def agregar_pelicula():

    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    imagen = request.files['imagen']
    filename=secure_filename(imagen.filename)

    if imagen and allowed_file(filename):
        imagen.save(os.path.join(PROFILE_PICTURES_FOLDER,filename))

    nueva_pelicula = models.Peliculas (
        titulo=titulo, 
        descripcion=descripcion, 
        imagen=filename)


    db_session.add(nueva_pelicula)
    db_session.commit()
    db_session.refresh(nueva_pelicula)

    return redirect(url_for('index'))

@app.get('/actualizar/<id>')
def editar(id):
    peliculas= db_session.query(models.Peliculas).get(id)
    return render_template('editar.html', peliculas=peliculas)

@app.post('/<id>/actualizar')
def editar_pelicula(id):
    peliculas= db_session.query(models.Peliculas).get(id)

    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    imagen = request.files['imagen']
    filename=secure_filename(imagen.filename)

    
    if imagen and allowed_file(filename):
        imagen.save(os.path.join(PROFILE_PICTURES_FOLDER,filename))

    
    if titulo and titulo != '':
        peliculas.titulo = titulo
    
    if descripcion and descripcion != '':
        peliculas.descripcion = descripcion

    if imagen and imagen != '':
        peliculas.imagen = filename 

    db_session.add(peliculas)
    db_session.commit()
    return redirect(url_for('index'))


@app.get('/eliminar/pelicula/<id>/')
def eliminar_pelicula(id):
    peliculas = db_session.query(models.Peliculas).get(id)
    db_session.delete(peliculas)
    db_session.commit()
    return redirect(url_for('index'))   



    
if __name__ == '__main__':
    app.run('0.0.0.0', 8081, debug=True)
