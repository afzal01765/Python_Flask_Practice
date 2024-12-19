from  flask import  Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PASSWORD"] =''
app.config["MYSQL_DB"] ='flaskapp'
app.config["MYSQL_USER"] ='root'
mysql = MySQL(app)

@app.route("/")

def index():
   cur = mysql.connection.cursor()
   cur.execute("select* from users")
   data = cur.fetchall()
   cur.close()
   return str(data)

if __name__ =="__main__":
   app.run(debug=True)



