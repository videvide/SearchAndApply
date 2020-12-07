import os
import smtplib
from email.message import EmailMessage
import json
import imghdr

i = 0
# add your own resumes here:
resumes = ['CV-SWE.pdf', 'CV-ENG.pdf']
test_receiver = os.environ.get('test_receiver')
used_list = os.environ.get('used_list')
af_list = os.environ.get('af_list')
aw_list = os.environ.get('aw_list')


def SendMail(item, sender, password, receiver):
    if 'namn' in item.keys():
        namn_split = item['namn'].split(' ', 1)
        namn_str = namn_split[0]
        namn = namn_str.replace(',', '')
    else:
        pass
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = f"Gällande: {item['title']}"
    if 'namn' in item.keys():
        msg.set_content(
            f"Hej {namn}!\n\nHärmed ansöker jag till tjänsten.\n\n"
            "Om denna matchningen inte är perfekt kanske det finns en mer passande sådan.\n\n"
            "Återkoppla gärna för vidare samtal.\n\n"
            "Tack på förhand!\n\n"
            "Med vänliga hälsningar,\n\n"
            "Vide")
    else:
        msg.set_content(
            f"Hej!\n\nHärmed ansöker jag till tjänsten.\n\n"
            "Om matchningen inte är perfekt kanske det finns en mer passande sådan.\n\n"
            "Återkoppla gärna för vidare samtal.\n\n"
            "Tack på förhand!\n\n"
            "Med vänliga hälsningar,\n\n"
            "Vide")
    for resume in resumes:
        with open(resume, 'rb') as pdf:
            file_data = pdf.read()
            file_name = pdf.name
        msg.add_attachment(file_data,
                           maintype='application',
                           subtype='octet-stream',
                           filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(sender, password)
            smtp.send_message(msg)
            used = json.dumps(item)
            # add item to already used list!
            with open(used_list, 'a+') as u:
                u.write(f"{used}\n")
        except:
            return


######################################################
###   OBS ---> 5 * 100 = max 500st mail/dag. <---  ###
######################################################


def SetSender(sender, password):
    # with open(af_list, 'r') as sendlist, open(used_list, 'r') as u:
    with open(aw_list, 'r') as sendlist, open(used_list, 'r') as usedlist:
        for line in sendlist:
            if line not in usedlist:
                item = json.loads(line)
                # receiver = item['mail']
                SendMail(item, sender, password, test_receiver)
                return


while i < 100:
    sender = os.environ.get('mail1_email')
    password = os.environ.get('mail1_pass')
    SetSender(sender, password)
    i += 1
while i < 200:
    sender = os.environ.get('mail2_email')
    password = os.environ.get('mail2_pass')
    SetSender(sender, password)
    i += 1
while i < 300:
    sender = os.environ.get('mail3_email')
    password = os.environ.get('mail3_pass')
    SetSender(sender, password)
    i += 1
while i < 400:
    sender = os.environ.get('mail4_email')
    password = os.environ.get('mail4_pass')
    SetSender(sender, password)
    i += 1
while i < 500:
    sender = os.environ.get('mail5_email')
    password = os.environ.get('mail5_pass')
    SetSender(sender, password)
    i += 1
