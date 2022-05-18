from flask import Flask
app = Flask(__name__)
# estas dos lineas de arriba siempre deben ponerse al principio













# estas dos líneas siempre deben estar al final de mi archivo
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)