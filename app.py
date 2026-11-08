from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! from Miles in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_postgres_pgmg_user:gZ1uo6uysFReEJGuDHhs6Gta7jXF7T4K@dpg-dboe27rm8hqs738ad2h0-a/lab_10_postgres_pgmg")
    conn.close()
    return "Database Connection Successful"
