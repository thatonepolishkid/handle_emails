import imaplib
import email
from email.header import decode_header
import re

period = '.'
pattern = r'((?<!\S)[_]*[w]*[\d]*[\W]*)'

username = input('Please input your Username: ') #I will need to create some form of security so that this is encrypted

password = input('Please input your password: ') #I will need to create some form of security so that this is encrypted

email_folder = (input('Please select the folder you wish to have emails deleted from: ')).upper() #for my use case it will be 'Inbox' first

emails_to_not_delete = input('Please input a portion of the emails that you do not want to be deleted here: ') #for my use case it will be ([\w]*@red-thread.com)

email_host = input('Please input your email provider: ').strip()

email_provider_imap = f'imap.{email_host.lstrip(pattern).lstrip(period)}'

print(email_provider_imap)

imap = imaplib.IMAP4_SSL(email_provider_imap)

login = imap.login(username, password)

imap.select(email_folder)

emails_to_not_delete = imap.search(None, 'FROM', (f'{emails_to_not_delete}'))

delete_emails = imap.search(None, 'BEFORE, "09-MAY-2023"')

for letter in emails_to_not_delete:
    imap.uid('COPY', letter, 'Archive')
    imap.uid('STORE', letter, '+FLAGS', '(\Deleted)')

for mail in delete_emails:
    imap.store(mail, '+FLAGS', '\\Deleted')


#imap.expunge()

imap.close()

imap.logout()