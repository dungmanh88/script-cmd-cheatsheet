import os
import my_module
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
                        previous_state = my_module.get_value(line)
                    if line.find("current_state") != -1:
                        current_state = my_module.get_value(line)
                    if line.find("timer") != -1:
                        timer = None if my_module.get_value(line) == 'None' else my_module.get_value(line)
                website.append({"name": filename,
                                "previous_state": previous_state,
                                "current_state": current_state,
                                "timer": timer
                                })
                file.close()
    return website
