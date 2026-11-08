from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Miles in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_postgres_pgmg_user:gZ1uo6uysFReEJGuDHhs6Gta7jXF7T4K@dpg-dboe27rm8hqs738ad2h0-a/lab_10_postgres_pgmg")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://lab_10_postgres_pgmg_user:gZ1uo6uysFReEJGuDHhs6Gta7jXF7T4K@dpg-dboe27rm8hqs738ad2h0-a/lab_10_postgres_pgmg")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://lab_10_postgres_pgmg_user:gZ1uo6uysFReEJGuDHhs6Gta7jXF7T4K@dpg-dboe27rm8hqs738ad2h0-a/lab_10_postgres_pgmg")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://lab_10_postgres_pgmg_user:gZ1uo6uysFReEJGuDHhs6Gta7jXF7T4K@dpg-dboe27rm8hqs738ad2h0-a/lab_10_postgres_pgmg")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string +="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgresql://lab_10_postgres_pgmg_user:gZ1uo6uysFReEJGuDHhs6Gta7jXF7T4K@dpg-dboe27rm8hqs738ad2h0-a/lab_10_postgres_pgmg")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"


