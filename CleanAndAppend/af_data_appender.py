# This is where the information from platsbanken is further 'cleaned'.
# Because of the ad-structures we need to first collect either contact or apply mail.
# Then we choose one of them and put inside the final data which is used to send emails.
# All 'new' info is added to a .txt file instead of .jl
import json

job_list = []
job_dict = {}

with open('*file_path*', 'r') as f:
    for item in f:
        job_list.append(json.loads(item))

for item in job_list:
    if item['contact-mail'] and item['apply-mail']:
        annons_id = str(item['id'])
        id_clean = annons_id.replace('Annons-Id: ', '')
        mail = item['contact-mail']
        mail_clean = mail.replace('mailto:', '')
        job_dict[id_clean] = {
            'mail': mail_clean,
            'id': id_clean,
            'title': item['title'],
        }
        if item['name'] is not None:
            job_dict[id_clean]['name'] = item['name']
        obj = json.dumps(job_dict[id_clean])
        with open('*file_path*', 'a+') as j:
            j.write(f'{obj}\n')
    elif item['apply-mail']:
        annons_id = str(item['id'])
        id_clean = annons_id.replace('Annons-Id: ', '')
        mail = item['apply-mail']
        mail_clean = mail.replace('mailto:', '')
        job_dict[id_clean] = {
            'mail': mail_clean,
            'id': id_clean,
            'title': item['title'],
        }
        if item['name'] is not None:
            job_dict[id_clean]['name'] = item['name']
        obj = json.dumps(job_dict[id_clean])
        with open('*file_path*', 'a+') as j:
            j.write(f'{obj}\n')
    elif item['contact-mail']:
        annons_id = str(item['id'])
        id_clean = annons_id.replace("Annons-Id: ", '')
        mail = item['contact-mail']
        mail_clean = mail.replace('mailto:', '')
        job_dict[id_clean] = {
            'mail': mail_clean,
            'id': id_clean,
            'title': item['title'],
        }
        if item['name'] is not None:
            job_dict[id_clean]['name'] = item['name']
        obj = json.dumps(job_dict[id_clean])
        with open('*file_path*', 'a+') as j:
            j.write(f'{obj}\n')
