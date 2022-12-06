from flask import render_template
from models.UsersModel import User
import conf
import os
#from crypt import methods

app = conf.connex_app
app.add_api(conf.base_dir / "swagger.yml")


@app.route("/")
def index():
    
    return render_template("index.html")


# iniciar sesión
@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/form')
def form():
    return render_template('auth/form.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host="0.0.0.0", port=port, debug=True)