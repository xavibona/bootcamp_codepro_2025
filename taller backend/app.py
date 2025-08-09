from flask import Flask, render_template, request, redirect #desde flask importamos la clase Flask
from flask_sqlalchemy import SQLAlchemy



#se crea la instancia de flask (un objeto)
app = Flask(__name__) # Llamamos a la clase flask, luego el __name__ asigna el nombre de este archivo

#configurar aplicacion para crear nuestro modelo de bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tarea(db.Model):
    #Columna identificador unico
    id = db.Column(db.Integer, primary_key = True)

    #Columna titulo
    titulo = db.Column(db.String(100), nullable = False)  # nullable le dice que no puede estr vacio

    #Columna descripcion
    descripcion = db.Column(db.Text, nullable = True)

    #Columna prioridad
    prioridad = db.Column(db.String(20), nullable = True)
    

    #Columna fecha
    fecha_inicio = db.Column(db.String(20), nullable = True)
    fecha_fin = db.Column(db.String(20), nullable = True)

    #Columna de la tarea
    estado = db.Column(db.String(20), nullable = True)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    #consulta a la base de datos
    tareas = Tarea.query.all()
    return render_template('index.html', tarea=tareas)

@app.route('/tarea', methods=['POST'])
def manejar_tarea():
    accion = request.form.get('accion')
    tarea_id = request.form.get('id')

    if accion == 'agregar':
        nueva = Tarea(
            titulo = request.form.get('titulo'),
            descripcion = request.form.get('descripcion'),
            prioridad = request.form.get('prioridad'),
            fecha_inicio = request.form.get('fecha_inicio'),
            fecha_limite = request.form.get('fecha_limite'),
            estado = request.form.get('estado')
        )
        db.session.add(nueva)
        db.session.commit()
    
    #si la operacion es editar
    elif accion == 'editar' and tarea_id:
        #buscar la tarea por su id en la db
        tarea = Tarea.query.get(tarea_id)
        tareas = Tarea.query.all()

        return render_template('index.html', tarea=tareas, tarea_editando=tarea)
    elif accion == 'actualizar' and tarea_id:
        tarea = Tarea.query.get(tarea_id)
        #si la tarea existe, actualizamos con los nuevos datos
        if tarea:
            tarea.titulo = request.form.get('titulo')
            tarea.descripcion = request.form.get('descripcion')
            tarea.prioridad = request.form.get('prioridad')
            tarea.fecha_inicio = request.form.get('fecha_inicio')
            tarea.fecha_limite = request.form.get('fecha_limite')
            tarea.fecha_estado = request.form.get('fecha_estado')

            db.session.commit()
    elif accion == 'eliminar' and tarea_id:
        #buscar la tarea q queremos borrar
        tarea = Tarea.query.get(tarea_id)
        
        #si la tarea existe, se marca pa borrar
        if tarea:
            db.session.delete(tarea)
            
            #se confirma / commitea
            db.session.commit()

            #redirigimos a la pagina principal
            return redirect('/')


if __name__ == '__main__':
    app.run()