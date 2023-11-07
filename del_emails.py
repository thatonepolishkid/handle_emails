import imaplib
import email
from email.header import decode_header
import re

period = '.'
username = input('Please input your Username: ') #I will need to create some form of security so that this is encrypted

password = input('Please input your password: ') #I will need to create some form of security so that this is encrypted

email_folder = (input('Please select the folder you wish to have emails deleted from: ')).upper() #for my use case it will be 'Inbox' first

pattern = input('Please input a portion of the emails that you do not want to be deleted here: ') #for my use case it will be ([\w]*@red-thread.com)

email_host = input('Please input your email provider: ').strip()

email_provider_imap = f'imap.{email_host.lstrip(pattern).lstrip(period)}'

imap = imaplib.IMAP4_SSL(email_provider_imap)

login = imap.login(username, password)

imap.select(email_folder)

status, messages = imap.search(None, 'BEFORE "09-SEPT-2023')

for mail in messages:
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            
            subject = decode_header(msg["subject"])[0][0]
            
            if isinstance(subject, bytes):
                subject = subject.decode()
            print("Deleting", subject)
    imap.store(mail, "+FLAGS", "\\dELETED")
    
imap.expunge()

imap.close()

imap.logout()