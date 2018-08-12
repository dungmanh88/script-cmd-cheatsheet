import urllib.request
import time
import os
import my_module

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
    website = my_module.init_site_list([])
    my_module.flush_site_list_to_disk(website, path)
# - khong rong thi load tu disk vao mem
else:
    print("2")
    website = my_module.load_from_disk_to_site([], path)
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
        website = my_module.load_from_disk_to_site([], path)
#   neu list khong rong thi kiem tra timer flush xuong disk, reset timer
    else:
        flush_end_time = int(round(time.time() * 1000))
        if flush_end_time - flush_start_time > flush_timeout * 1000:
            print("flusing after %d" % flush_timeout)
            my_module.flush_site_list_to_disk(website, path)
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
                my_module.send_mail(item["name"], item["current_state"])
                my_module.update_site_list_on_disk(item, path)
            if item["current_state"] == "down" == item["previous_state"]:
                print("send mail down after 3 mins")
                current_time = int(round(time.time() * 1000))
                print("current_time %d" % current_time)
                print("timer %d" % int(item["timer"]))
                if item["timer"] != None and current_time - int(item["timer"]) >= 3 * 1000 * 60:
                    print("send mail NOW")
                    my_module.send_mail(item["name"], item["current_state"])
                    # update timer
                    item["timer"] = int(round(time.time() * 1000))
                    my_module.update_site_list_on_disk(item, path)
# sleep 1s giua cac lan loop
    time.sleep(1)


# them systemd de quan ly - done
# dung indexof thay cho in line - done
# viet sao cho main function cang it xu ly cang tot, day vao function khac that nhieu
# tach thanh cac package, don function vao package rieng
# viet phien ban giao tiep voi sql qua raw va orm
# viet trang login, phan quyen, goi api ngoai cua django manage ip
