from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello_world():
  return 'hello world'

if __name__ == '__main__':
  # app.debug = True
  app.run(host='127.0.0.1', port=5011, debug=True)
