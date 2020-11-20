import smtplib
z = smtplib.SMTP("smtp.gmail.com", 587)
smail=input("Enter your email")
spwd=input("Enter your email password")
msg=input("Enter the message that you want to send")
rmail=input("Enter Reciever's email id")
z.starttls()
try:
    z.login(smail, spwd)
    z.sendmail(smail, rmail, msg)
    print("Email Sent Successfully")
except smtplib.SMTPAuthenticationError as a:
    print(a)
z.quit()