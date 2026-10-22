from flask import Flask, render_template

app = Flast(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if ___name___ == '__main__':
    app.run()