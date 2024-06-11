from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Vanakam Da Maapla Soul Society la Irundhu"


if __name__=="__main__":
    app.run(debug=True)