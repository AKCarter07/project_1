from flask import Flask
from controller.employee_controller import ec
from controller.user_controller import uc



if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(uc)
    app.register_blueprint(ec)
    app.run(port=8080, debug=True)
