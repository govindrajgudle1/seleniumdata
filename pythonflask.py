from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
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
                  recipients=['tech@themedius.ai'],
                  cc=['hr@themedius.ai'])
    
    msg.body = """\
Dear Team,

Please find attached the following items for the assignment submission:
1. Screenshot of the form filled via code.
2. Source code - https://github.com/govindrajgudle1/seleniumdata.git
3. Brief documentation of my approach.
4. My resume.
5. Links to past projects/work samples.
6. Confirming my availability to work full-time (10 am to 7 pm) for the next 3-6 months.

Thank you.

Best regards,
Govindraj Gudle

GitHub Repository: https://github.com/govindrajgudle1/seleniumdata.git
"""

    # Attach files
    attachments = [
        {"path": "form_filled.png", "name": "form_filled.png", "type": "image/png"},
        {"path": "govindrajscv.pdf", "name": "Govindraj_Gudle_Resume.pdf", "type": "application/pdf"},
        {"path": "documentation.pdf", "name": "documentaion", "type": "text/markdown"}
        # Add more attachments if needed
    ]

    for attachment in attachments:
        with app.open_resource(attachment["path"]) as fp:
            msg.attach(attachment["name"], attachment["type"], fp.read())

    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)
