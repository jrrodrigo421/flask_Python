from flask import Flask
app =Flask(__name__)

@app.route("/<numero>", methods=['GET','POST'])
# @app.route("/")
def hello(numero):
    return 'Olá MUNDO! {}'.format(numero)
    
if __name__== "__main__":
    app.run(debug=True)
