###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from forms import ContactForm
import pandas as pd
from flask_mail import Mail, Message


###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'dev fao football app'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jacklee61404@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])

def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        #res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        msg = Message(subject, sender = 'jacklee61404@gmail.com', recipients = ['jacklee61404@gmail.com'])
        msg.body = message
        mail.send(msg)
        return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)

###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True)
