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
