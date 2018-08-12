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

# define function cap nhat gia tri cua site
# truyen vao sitename (name, previous_state, current_state, timer), path
# check path ton tai va la dir, check sitename khong empty
# can encode phan :// de mo duoc
# mo file theo sitename
# ghi de lai file
def update_site_list_on_disk(site_name, path):
    if site_name and os.path.exists(path) and os.path.isdir(path):
        filename = site_name["name"].replace("://", "3A2F2F")
        f = open(path + "/" + filename, "w")
        f.write("previous_state: %s\n" % site_name["previous_state"])
        f.write("current_state: %s\n" % site_name["current_state"])
        f.write("timer: %s\n" % site_name["timer"])
        f.close()
    return None

def flush_site_list_to_disk(website, path):
    if website and os.path.exists(path) and os.path.isdir(path):
        # loop qua site list
        # tao file name theo site name
        # encode file name
        # luu previous_state, current_state, timer
        for item in website:
            update_site_list_on_disk(item, path)
    return None

# get value 123 of str kieu abc: 123
def get_value(str):
    return str[str.find(":")+2:]

# param: website, path
# kiem tra website not None va path ton tai va la dir thi doc het tat ca cac file trong path
# check item neu la file thi convert 3A2F2F -> :// roi dua append website item
# mo file, duyet tung line trong file, nho strip line, lay ra previous_state, current_state, timer cua file
# append website list cac thong so doc duoc tu file
# close file
# return list website truyen vao

def load_from_disk_to_site(website, path):
    if website is not None and os.path.exists(path) and os.path.isdir(path):
        file_list = os.listdir(path)
        for fname in file_list:
            if os.path.isfile(path + "/" + fname):
                print("================")
                print(fname)
                filename = fname.replace("3A2F2F", "://")
                file = open(path + "/" + fname, "r")
                previous_state, current_state, timer = None, None, None
                for line in file:
                    line = line.strip()
                    print("line: " + line)
                    if line.find("previous_state") != -1:
                        previous_state = get_value(line)
                    if line.find("current_state") != -1:
                        current_state = get_value(line)
                    if line.find("timer") != -1:
                        timer = None if get_value(line) == 'None' else get_value(line)
                website.append({"name": filename,
                                "previous_state": previous_state,
                                "current_state": current_state,
                                "timer": timer
                                })
                file.close()
    return website

path = "/tmp/xxx"
# kiem tra xem path co ton tai va la dir khong
# neu chua co thi tao ra luon
if not os.path.exists(path):
    os.makedirs(path)
# kiem tra xem co file trong path khong
# - neu rong thi khoi tao danh sach trong mem -> flush xuong disk
website = []
if not os.listdir(path):
    print("1")
    website = init_site_list([])
    flush_site_list_to_disk(website, path)
# - khong rong thi load tu disk vao mem
else:
    print("2")
    website = load_from_disk_to_site([], path)
print("*************")
print(website)

# khoi tao timer de flush disk
flush_start_time = int(round(time.time() * 1000))
flush_timeout = 3 # 3 seconds
# dinh ky doc tu mem qua moi loop,

while True:
    print("scan service")
#   neu list trong mem rong thi load tu disk
    if website is None or not website:
        website = load_from_disk_to_site([], path)
#   neu list khong rong thi kiem tra timer flush xuong disk, reset timer
    else:
        flush_end_time = int(round(time.time() * 1000))
        if flush_end_time - flush_start_time > flush_timeout * 1000:
            print("flusing after %d" % flush_timeout)
            flush_site_list_to_disk(website, path)
            flush_start_time = int(round(time.time() * 1000))

    # phan con lai giong nhu cu
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

            if item["current_state"] != item["previous_state"]:
                print("send mail %s" % item["current_state"])
                send_mail(item["name"], item["current_state"])
                update_site_list_on_disk(item, path)
            if item["current_state"] == "down" == item["previous_state"]:
                print("send mail down after 3 mins")
                current_time = int(round(time.time() * 1000))
                print("current_time %d" % current_time)
                print("timer %d" % int(item["timer"]))
                if item["timer"] != None and current_time - int(item["timer"]) >= 3 * 1000 * 60:
                    print("send mail NOW")
                    send_mail(item["name"], item["current_state"])
                    # update timer
                    item["timer"] = int(round(time.time() * 1000))
                    update_site_list_on_disk(item, path)
# sleep 1s giua cac lan loop
    time.sleep(1)


# them systemd de quan ly - done
# dung indexof thay cho in line - done
# viet sao cho main function cang it xu ly cang tot, day vao function khac that nhieu
# tach thanh cac package, don function vao package rieng
# viet phien ban giao tiep voi sql qua raw va orm
# viet trang login, phan quyen, goi api ngoai cua django manage ip
