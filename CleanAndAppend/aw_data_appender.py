# We append the data to a .txt file instead of the .jl file
import json

job_list = []
job_dict = {}

with open('*file_path*') as f:
    for item in f:
        job_list.append(json.loads(item))

for item in job_list:
    mail = item['mail']
    job_dict[item['id']] = {
        'mail': mail,
        'id': item['id'],
        'title': item['title'],
        'name': item['name']
    }
    obj = json.dumps(job_dict[item['id']])
    with open('*file_path*', 'a+') as j:
        j.write(f"{obj}\n")
