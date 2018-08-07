import urllib.request
import time
import smtplib
import time
import os

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


# define mot init function se khoi tao 1 so site theo list cua dict
#   - param: list rong
#   - return list day du cac site trong qua trinh khoi tao
# define mot function se flush list cua dict xuong file, filename la sitename voi encode protocol://
#   - param: list khong rong, vi tri thu muc flush
#   - return None
# define mot function se doc thu muc xac dinh load toan bo file name do vao memory de thuc hien loop va xu ly
#   - param: vi tri thu muc flush, list rong
#   - return list day du site lay tu folder chi dinh
def init_site_list(website=[]):
    if not website:
        website.append({
            "name": "https://xin-staging.nal.vn",
            "previous_state": "up",
            "current_state": "up",
            "timer": None
        })

        website.append({
            "name": "https://ptss-stg07.nal.vn",
            "previous_state": "up",
            "current_state": "up",
            "timer": None
        })

        website.append({
            "name": "http://admin-tools.nal.vn",
            "previous_state": "up",
            "current_state": "up",
            "timer": None
        })

    return website

def flush_site_list_to_disk(website, path):
    if website and os.path.exists(path) and os.path.isdir(path):
        # loop qua site list
        # tao file name theo site name
        # encode file name
        for item in website:
            print(path + "/" + item["name"])
            filename = item["name"].replace("://", "3A2F2F")
            f = open(path + "/" + filename, "w")
            f.write("the day is the last day\n")
            f.close()
    return None

website = init_site_list([])
flush_site_list_to_disk(website, "/tmp/xxx")
