from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config["TEMPLEATES_AUTO_RELOAD"]=True

@app.route("/")
def home():
    return render_template ("index.html")

@app.route ("/guardar")
def guardar():
    return "Producto Guardado Correctamente"

@app.route ("/login")
def login():
    return render_template("login.html")
@app.route ("/logout")
def logout():
    return redirect("login")

if __name__ == "__main__":
    app.run(port=5000)
