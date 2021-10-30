from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from HospMercy import config



#from HospMercy.common.filters import format_datetime
#from HospMercy.models import Citas

app = Flask(__name__)
#
app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)

# after the db variable initialization
#login_manager = LoginManager()
#def register_filters(app):
    #app.jinja_env.filters['datetime'] = format_datetime
    
@app.route('/')
@app.route('/home/')
@app.route('/index/')
def index():
    return render_template('index.html', titulo = "Hospital de la Misericordia")
    #return 'Directorio raiz'

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registro_citas', methods=["GET","POST"])
def registro_citas():
    from HospMercy.models import Citas
    if request.method=="POST":
        citanew=Citas(id=request.form['id'], tipoId=request.form['tipoId'], tipoUsuario='P', 
                            idDoctor=request.form['idDoctor'], fecha=request.form['fecha'], hora=request.form['hora'])
        db.session.add(citanew)
        db.session.commit()          
        return redirect (url_for(render_template('registro_citas.html')))
    else:
    	return render_template('registro_citas.html')
                            
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

@app.route('/citas')
def citas():
    from HospMercy.models import Citas
    citas = Citas.query.all()
    return render_template("citas.html", citas=citas)

@app.route('/logout/')
def logout():
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404