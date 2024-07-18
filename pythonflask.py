from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send_email', methods=['GET'])
def send_email():
    msg = Message('Python (Selenium) Assignment - Govindraj Gudle',
                  sender='your-email@example.com',
                  recipients=['tech@themedius.ai', 'hr@themedius.ai'])
    msg.body = 'Please find attached the assignment submission.'

    attachments = [
        {"path": "form_filled.png", "name": "form_filled.png", "type": "image/png"},
        {"path": "resume.pdf", "name": "govindrajscv.pdf", "type": "application/pdf"}    ]

    for attachment in attachments:
        with app.open_resource(attachment["path"]) as fp:
            msg.attach(attachment["name"], attachment["type"], fp.read())

    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)
