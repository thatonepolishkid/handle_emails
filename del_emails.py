#Import necessary modules.
import imaplib
import getpass
import time

#Gets users input.

username = input('Please input your Username: ') 


#Gets users password - For most services this will need to be done through app passwords, which need to be enabled.

password = getpass.getpass() 


#Lets the user decide which folder to select emails from.
#for my use case it will be 'Inbox' first

email_folder = (input('Please select the folder you wish to have emails deleted from: ')).upper() 


#Allows the user to choose which email provider they use

email_host = input('Please input your email provider: ').strip()


#Makes a call to the email service based on users input.

email_provider_imap = f'imap.{email_host.strip()}'




#A function that will mark and delete emails, Will loop 25 times. I did it this way because Imaplib only allows access to 1000 emails at a time per login. 

def delete_these(user, creds, email_provider):
    x = 0
    while x < 26:
        #Creates the imap4 class with SSL 
        imap = imaplib.IMAP4_SSL(email_provider)

        #Logs the user in 
        imap.login(user, creds)
        print('logged in!')
        
        #From user input will select the folder containing the Emails to be deleted.
        imap.select(email_folder)

        #Gets emails from the inbox and stores them as user id's, Identifies emails from before Janurary 1st 2023
        _, emails_to_delete = imap.search(None, 'BEFORE "01-JAN-2023"')
        
        #Declares emails_to_delete as a list that can be itterated through by splitting Email id's
        emails_to_delete = emails_to_delete[0].split()
        
        #This for loop iterates through and marks the emails for deletion
        for mail in emails_to_delete:
            imap.store(mail, '+FLAGS', '\\Deleted')
            print('Deleting emails marked for deletion: ', mail)
        print('Loop complete!')
        #Removes the Emails
        imap.expunge()

        #Closes the email
        imap.close()

        #Logs the user out to avoid raising an error from trying to use imap.search() multiple times.
        imap.logout()
        print('Logged out!')

        #Sleeps the function for a 10 seconds
        time.sleep(10)

        #Increases x by 1 so that there is no accidental infinite loop
        x += 1

#calls the function for execution
delete_these(username, password, email_provider_imap)



