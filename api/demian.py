from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'HOST'
app.config['MYSQL_USER'] = 'USER'
app.config['MYSQL_PASSWORD'] = 'PASS'
app.config['MYSQL_DB'] = 'BD_NAME'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Para obtener resultados como diccionarios

mysql = MySQL(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM TOKEN')
        data = cur.fetchall()
        cur.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='172.25.39.36')
