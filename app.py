from flask import Flask
from config import Config
from database import mysql
from routes.moto_routes import moto_bp

app = Flask(__name__)

# Configuración MySQL
app.config['MYSQL_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_USER'] = Config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = Config.MYSQL_DB

mysql.init_app(app)

# Registrar rutas
app.register_blueprint(moto_bp)

if __name__ == '__main__':
    app.run(debug=True)