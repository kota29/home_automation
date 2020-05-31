from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("login.html")

@app.route("/common", methods=["POST"])
def common():
    name = request.form.get("un")
    upas = request.form.get("pass")
    f = open('email.txt','r')
    s = '\n'
    l = []
    c=0
    while(s):
        s = f.readline()
        l = s.split()
        if name in l:
            break
        c = c + 1
    f1 = open('pass.txt','r')
    txt = f1.read()
    k = txt.split(",")
    pas = k[c]
    if pas == upas:
        f.close()
        f1.close()
        return render_template("common.html")
    else:
        f.close()
        f1.close()
        return render_template("login.html")

@app.route("/forgot", methods=["POST","GET"])
def forgot():
    if request.method == "GET":
        return render_template("forgot.html")
    if request.method == "POST":
        mail_content = """Hello,
        click below link to reset your password

        https://kota29.github.io/home_automation/reset%20password.html

        Thank You
        """
        #The mail addresses and password
        rm = request.form.get("ei")
        sender_address = 'friends63097@gmail.com'
        sender_pass = 'Ironman$519'
        receiver_address = rm
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Reset Link For Home Automation.'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        return render_template("index.html",un="mail sent")


@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method == "GET":
        return render_template("sign-up.html")
    if request.method == "POST":
        na = request.form.get("name")
        em = request.form.get("email")
        p = request.form.get("pass")
        cp = request.form.get("cpass")
        f = 0
        f = open('email.txt','r')
        s = '\n'
        l = []
        c=0
        name = em
        while(s):
            s = f.readline()
            l = s.split()
            if name in l:
                f = 1
                break
        if p == cp and f == 0:
            f1 = open('name.txt','a')
            f1.write(na+'\n')
            f1.close()
            f2 = open('email.txt','a')
            f2.write(em+'\n')
            f2.close()
            f3 = open('pass.txt','a')
            f3.write(na+',')
            f3.close()
            return render_template("index.html",un="registered sussesfully")
        else:
            return render_template("sign-up.html")



@app.route("/masterbedroom")
def masterbedroom():
    return render_template("masterbedroom.html")

@app.route("/living")
def livingroom():
    return render_template("livingroom.html")

@app.route("/kidsbedroom")
def kidsbedroom():
    return render_template("kidsbedroom.html")

@app.route("/dining")
def dining():
    return render_template("dining.html")

@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html")

if __name__ == "__main__":
    app.run(debug=True)
