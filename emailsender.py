from email.message import EmailMessage
import ssl, smtplib



email_sender = 'asadzadatabriz@gmail.com'
email_password = 'yourpassword'

email_reviever = 'vokkitarza@gufum.com' #you can get a temp email account from temp-mail.org website

subject = "You will be able to do what you want"
body = """

Don't forget, you can! Never Give Up!

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reviever
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as  smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_reviever,em.as_string())