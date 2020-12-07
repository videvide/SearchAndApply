import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'


def checkEmail(email):
    if (re.search(regex, email)):
        return 'OK'
    else:
        pass


new = set()
with open('*file_path*', 'r') as f, open('*file_path*', 'a+') as t:
    for item in f:
        new.add(item)
    for item in new:
        new_item = item.replace('mailto:', '')
        split_item = new_item.split('?', 1)
        check_item = split_item[0]
        if checkEmail(check_item) == 'OK':
            t.write(f"{check_item}\n")
        else:
            pass

with open('*file_path*', 'r+') as f, open('*file_path*', 'a+') as t:
    for line in f:
        if not line.isspace():
            t.write(line)
