# lay danh sach cac project visibility dung gitlab api
# doc json file tra ve
# lay ra phan tu id
# noi vao gitlab_api_url la ra project
# thay doi visibility cua project qua api
import urllib.request
#https://stackoverflow.com/questions/34740288/importerror-no-module-named-urllib2-python-3/34740459
import json

token = input("Enter your token: ")
domain = input("Enter your domain: ")
gitlab_api_url = "https://%s/api/v4" % domain
print("token = %s and url = %s" % (token, gitlab_api_url))
try:
    response = urllib.request.urlopen("%s/%s" % (gitlab_api_url,"projects?visibility=public") )
except urllib.error.URLError as e:
    print("exception url")
except urllib.error.HTTPError as e:
    print("exception http")
except Exception as e:
    print("general exception")
else:
    html = response.read()
string_data = html.decode('utf8').replace("'", '"')
#print(string_data)
json_data = json.loads(string_data)
total = 0
for item in json_data:
    total += 1
    id = item['id']
    # change visibility
    link = "projects/%d?visibility=private" % id
    full_link = "%s/%s" % (gitlab_api_url, link)
    print(full_link)

    try:
        request = urllib.request.Request(full_link, method="PUT")
        request.add_header('Private-Token', token)
        response = urllib.request.urlopen(request)
    except Exception as e:
        print("general exception")
        print(e)
    else:
        html = response.read()

print("total = %d" % total)
