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

#emails_to_not_delete = input('Please input a portion of the emails that you do not want to be deleted here: ') #for my use case it will be ([\w]*@red-thread.com)

email_host = input('Please input your email provider: ').strip()

email_provider_imap = f'imap.{email_host.lstrip(pattern).lstrip(period)}'

imap = imaplib.IMAP4_SSL(email_provider_imap)

login = imap.login(username, password)

imap.select(email_folder)




def delete_emails_loops(user, creds):
    for _ in range(26):
        _, delete_emails_ids = imap.search(None, '1000:2000')
        delete_emails_ids = delete_emails_ids[0].split(b' ')
        for msg_id in delete_emails_ids:
                imap.store(msg_id, '+FLAGS', '\\Deleted')
                print('Marking for deletion: ', msg_id)
                imap.expunge()
                imap.logout()
                imap.login(user, creds)

delete_emails_loops(username, password)





def select_emails(emails_to_delete):
    emails_to_delete = emails_to_delete[0].split(b' ')
    #emails_to_keep = emails_to_keep[0].split(b' ')
    for msg_id in emails_to_delete:
        imap.store(msg_id, '+FLAGS', '\\Deleted')
        print('Marking for deletion: ', msg_id)
'''for msg_id in emails_to_keep: imap.store(msg_id, '-FLAGS', '\\Deleted')'''



# TODO Rename this here and in `email_del_cycle`
def extracted_from_email_del_cycle_8(msg_id):
    imap.store(msg_id, '+FLAGS', '\\Deleted')
    imap.logout()
    print('Logging out.')
    time.sleep(5)
    print('Sleeping the cycle for ')
    imap.login(username, password)
    print('Logging in!')

def email_del_cycle(mail_to_delete):
    if mail_to_delete == False:
            print('Theres no emails here?!')
    while mail_to_delete == True:
        for msg_id in mail_to_delete:
            extracted_from_email_del_cycle_8(msg_id)




imap.close()

imap.logout()