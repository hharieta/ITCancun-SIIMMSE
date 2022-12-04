from flask import render_template, request
import conf_server
import os
#from crypt import methods
ON_HEROKU = os.environt.get('ON_HEROKU')

if ON_HEROKU:
    port = int(os.environ.get('PORT', 17995)) # as per OP comments default is 17995
else:
    port = 8000

app = conf_server.connex_app


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
    app.run(host="0.0.0.0", port=port, debug=True)