# sourcery skip: use-fstring-for-formatting
import imaplib
import email
import email.utils
from email.header import decode_header
import getpass
import time


period = '.'
pattern = r'((?<!\S)[_]*[w]*[\d]*[\W]*)'

username = input('Please input your Username: ') #I will need to create some form of security so that this is encrypted

password = getpass.getpass() #I will need to create some form of security so that this is encrypted

email_folder = (input('Please select the folder you wish to have emails deleted from: ')).upper() #for my use case it will be 'Inbox' first

email_host = input('Please input your email provider: ').strip()

email_provider_imap = f'imap.{email_host.lstrip(pattern).lstrip(period)}'





def delete_these(user, creds, email_provider):
    x = 0
    while x < 26:
        imap = imaplib.IMAP4_SSL(email_provider)
        imap.login(user, creds)
        print('logged in!')
        imap.select(email_folder)
        _, emails_to_delete = imap.search(None, 'BEFORE "01-JAN-2023"')

        emails_to_delete = emails_to_delete[0].split()
        
        for mail in emails_to_delete:
            imap.store(mail, '+FLAGS', '\\Deleted')
            print('Deleting emails marked for deletion: ', mail)
        print('Loop complete!')
        imap.expunge()
        imap.close()
        imap.logout()
        print('Logged out!')
        time.sleep(3)
        x += 1

delete_these(username, password, email_provider_imap)



