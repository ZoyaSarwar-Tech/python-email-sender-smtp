import smtplib
from email.message import EmailMessage
sender_email = "zoya@gmail.com"
sender_password = "your_app_password"
message = EmailMessage()
receivers=["zoyasarwar@gmail.com","iamareej@gmail.com","xyz@gmail.com"]
subject = "Python Email Project"
message="""
Hello,
This email was sent using Python.
Thank You!
"""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)
for email in receivers:
    em=EmailMessage()
    em["From"] = sender_email
    em["To"] = email
    em["Subject"] = subject
    em.set_content(message)
    server.send_message(em)
    print(f"Email was sent to {email}")
server.quit()
print("All emails were sent successfully!")
