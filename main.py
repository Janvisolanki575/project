from flask import Flask, render_template, request, redirect,session
from fileinput import filename
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

app = Flask(__name__)
app.secret_key='123'


@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/reg')
def indreg():
    return render_template("registration.html")

@app.route('/log')
def index222():
    return render_template("loginform.html")


@app.route('/pro')
def index223():
    return render_template("profileupload.html")

@app.route('/intreg', methods=['POST','GET'])
def intregi():
    try:
        name = request.form['name']
        psw = request.form['psw']
        gen = request.form['gen']
        phone = request.form['phone']
        email = request.form['email']
        mycursor = mydb.cursor()
        sql = """INSERT INTO `registration`(`password`, `Name`, `gender`, `email_id`, `mobile_no`) VALUES (%s,%s,%s,%s,%s) """
        val = (psw,gen,phone,email)
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect('/reg')
    except Exception as e:
        return render_template('loginform.html')

@app.route("/session_s",methods=['POST','GET'])
def verify():
    user = request.form['u_name']
    pass_s = request.form['p_name']
    cursor=mydb.cursor()
    cursor.execute("SELECT * FROM `registration` WHERE registration.email_id= '"+ user +"'    AND registration.password='"+ pass_s +"'")
    db= cursor.fetchone()
    return redirect('/pro')
    # return render_template('profile.html',db=db)

# @app.route('/pro')
# def pro():
#     # if 'user_see' in session:
#     #     user12 =str(session['user_see'])
#     #     cursor1.execute("SELECT * FROM `registration` WHERE registration.email_id= '"+ user12 +"' ")
#     #     db1 = cursor.fetchone()
#     return redirect("profile.html")

@app.route('/upload',methods=["POST","GET"])
def uploadd():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template("uploadmessage.html", name = f.filename)







if __name__ == "__main__":
    app.run(port=5000,debug=True)

