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

# - https://codehabitude.com/2013/12/24/python-objects-mutable-vs-immutable/
# - Do not put a mutable object as the default value of a function parameter. Immutable types are perfectly safe
def update_website(site, website=None):
    if website is None:
        website = []
    print(type(website))
    website.append(site)
    return website


# - khai bao mot danh sach website: ten site + previous status site + current status site, mac dinh up, up + timer: timer dem khi thay current site down
website=[]

# dua dan cac site vao kem metadata cua site nhu previous_state, current_state, timer
update_website({
    "name": "https://xin-staging.nal.vn",
    "previous_state": "up",
    "current_state": "up",
    "timer": None
}, website)

update_website({
    "name": "http://ptss-stg07.nal.vn",
    "previous_state": "up",
    "current_state": "up",
    "timer": None
}, website)

update_website({
    "name": "http://admin-tools.nal.vn",
    "previous_state": "up",
    "current_state": "up",
    "timer": None
}, website)

print(website)
print("======")
# loop true
# - loop qua danh sach website
while True:
    print("scan service")
    for item in website:
        site_name = item["name"]
        print("site: %s" % site_name)
        status_code=None
    #   - check http response qua tung site, gan previous la current, site nao >500 hoac co loi ket noi (status code None)
    #     danh dau current site down, note  2 trang thai previous + current vao danh sach
        try:
            response = urllib.request.urlopen(site_name)
        except urllib.error.URLError as e:
            print("exception url")
            status_code = e.code
        except urllib.error.HTTPError as e:
            print("exception http")
            status_code = e.code
        except Exception as e:
            print("general exception")
        else:
            status_code = response.code
        print(status_code)
        item["previous_state"] = item["current_state"]
        if status_code is None or status_code >= 500:
    #   - current site down
    #   - previous up va current site down thi ghi thoi diem hien tai, tinh bang ms (so moc 1970) -> day la thoi diem ma bat dau down
            item["current_state"] = "down"
            if item["previous_state"] == "up" and item["current_state"] == "down":
                item["timer"] = int(round(time.time() * 1000))
    #   - current site up
    #   - reset timer
        else:
            item["current_state"] = "up"
            item["timer"] = None
    # - loop qua danh sach site lan nua
    print("mail notify")
    for item in website:
#   - site current la down, previous la up thi gui mail thong bao down
#   - site current la up, previous la down thi gui thong bao up
#   -> current state != previous state
#   - site previous down, current down thi lay thoi diem hien tai tinh nang ms (so moc 1970)
#   - tinh khoang thoi gian tu timer, qua >= 3 phut thi gui mail tiep con khong thi ignore (de tranh tran mail)

        if item["current_state"] != item["previous_state"] == "up":
            print("send mail %s" % item["current_state"])
            send_mail(item["name"], item["current_state"])
        if item["current_state"] == "down" and item["previous_state"] == "down":
            print("send mail down after 3 mins")
            current_time = int(round(time.time() * 1000))
            print("current_time %d" % current_time)
            print("timer %d" % item["timer"])
            if item["timer"] != None and current_time - item["timer"] >= 3 * 1000 * 60:
                print("send mail NOW")
                send_mail(item["name"], item["current_state"])
                # update timer
                item["timer"] = int(round(time.time() * 1000))
# sleep 1s giua cac lan loop
    time.sleep(1)

# upgrade:
# dung function de giai quyet mutable object
# follow theo location 302
# dung file de luu trang thai site
# dung sqlite de luu trang thai site
# dung mysql de luu trang thai site
# dung django lap trinh site quan ly resource
