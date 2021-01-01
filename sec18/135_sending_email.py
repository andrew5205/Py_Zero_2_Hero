

# smtplib
# simple mail transfer protocol

# STEPS:
# 1. connection email server
# 2. confirming connection 
# 3. setting protocol 
# 4. logging 
# 5. sending message


# **********************************************************************
# Gmail:
#     'smtp.gmail.com', 587

# Yahoo:
#     smtp.mail.yahoo.com

# Outlook:
#     smtp-mail.outlook.from django.conf import settings
    
# ATT:
#     smpt.mail.att.net(port465)

# Verizon:
#     smtp.verizon.net(port465)

# Comcast:
#     smtp.comcast.com
# **********************************************************************




import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()                          # MUST elho() right after create object
# print(smtp_object.ehlo())               # (250, b'smtp.gmail.com at your service, [75.83.148.93]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
smtp_object.starttls()
# print(smtp_object.starttls())


# pasword = input('whats ur password:') # visiable

# invisiable password
import getpass
password = getpass.getpass('password will be hidden here:')


# **********************************************************************
# https://support.google.com/accounts/answer/185833?hl=en/



# Python App password

# **********************************************************************


# setup connections/ login
email = getpass.getpass('Email: ')
password = getpass.getpass('App password: ')
smtp_object.login(email, password)


from_address = email 
to_address = email

subject = input("enter subject line: ")
message = input("enter body message: ")
msg = "Subject: " + subject + '\n' + message

# sendmail()
smtp_object.sendmail(from_address, to_address, msg)

# close session
smtp_object.quit()

