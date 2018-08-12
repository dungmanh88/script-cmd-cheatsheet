import smtplib
# - gui mail:
#   - khai bao danh sach nhan mail nhu param, co gia tri mac dinh
#   - khai bao ten site bi down/up truye vao nhu param
#   - khai bao state treuyen vao nhu param
#   - khai bao username, passwd, smtp mail server nhu local var
#   - khai bao subject, message text template nhu local var
#   - send mail dung cac thong tin username passwd smtp server, title, text message, received mail
# Must: Allowing less secure apps to access your account
def send_mail(site_name, state, mail_list=["dungnm@nal.vn"]):
    username="nal.test1234@gmail.com"
    password="^AJew4a:"
    mail_server="smtp.gmail.com"
    body="Site %s is %s" % (site_name, state)
    from_addr = username
    to_addr = ", ".join(mail_list)
    subject="[Notification] %s is %s" % (site_name, state)
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (from_addr, to_addr, subject, body)

    try:
        server = smtplib.SMTP_SSL(mail_server, 465)
        server.ehlo()
        server.login(username, password)
        server.sendmail(from_addr, mail_list, message)
        server.close()
        print('Email sent!')
    except Exception as e:
        print(e)
        print('Something went wrong...')
