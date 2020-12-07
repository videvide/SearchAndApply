# This function makes a new list with only unique ads
new = set()
with open('*file_path*', 'r') as fr, open('*file_path*', 'a+') as to:
    for item in fr:
        new.add(item)
    for item in new:
        to.write(item)