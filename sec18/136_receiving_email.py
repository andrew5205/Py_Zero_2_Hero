
# import imaplib
# import getpass
# import email

# **********************************************************************
# https://support.google.com/accounts/answer/185833?hl=en/


# Python App password

# **********************************************************************


import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass
email = getpass.getpass('Email: ')
password = getpass.getpass('App password: ')
M.login(email, password)

# print(M)                # <imaplib.IMAP4_SSL object at 0x7f80959c8790>
# # print(M.lsit())
# m = M.list()
# # print(m)
                        # # ('OK', [b'(\\HasNoChildren) "/" "INBOX"', 
                        # b'(\\HasChildren \\Noselect) "/" "[Gmail]"', 
                        # b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"', 
                        # b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"', 
                        # b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"', 
                        # b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"', 
                        # b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"', 
                        # b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"', 
                        # b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Trash"'])

# make selections
inbox = M.select('inbox')
# print(inbox)                # ('OK', [b'4'])


# typ, data = M.search(None, '')
# typ, data = M.search(None, 'From example@gmail.com')

# make search category - see attached referance
typ, data = M.search(None, 'Subject "test"')
# print(typ)              # OK
# print(data)             # [b'4']

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822')


# emaol_data
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')


# email lib
import email
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_patload(decode=True)
        print(body)







# Search Category 
# <tr>
#     <td>'BEFORE date'</td>
#     <td>
#     Returns all messages before the date. Date must be formatted as 01-Nov-2000.
#     </td>
# </tr>

#  <tr>
#     <td>'ON date'</td>
#     <td>
#     Returns all messages on the date. Date must be formatted as 01-Nov-2000.
#     </td>
# </tr>

#  <tr>
#     <td>'SINCE date'</td>
#     <td>
#     Returns all messages after the date. Date must be formatted as 01-Nov-2000.
#     </td>
# </tr>

# <tr>
#     <td>'FROM some_string '</td>
#     <td>
#     Returns all from the sender in the string. String can be an email, for example 'FROM               user@example.com' or just a string that may appear in the email, "FROM example"
#     </td>
# </tr>

# <tr>
#     <td>'TO some_string'</td>
#     <td>
#     Returns all outgoing email to the email in the string. String can be an email, for example 'FROM user@example.com' or just a string that may appear in the email, "FROM example"
#     </td>
# </tr>

# <tr>
#     <td>'CC some_string' and/or 'BCC some_string'</td>
#     <td>
#     Returns all messages in your email folder. Often there are size limits from imaplib.
#     To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be.
#     </td>
# </tr>
# <tr>
#     <td>'SUBJECT string','BODY string','TEXT "string with spaces"'</td>
#     <td>
#     Returns all messages with the subject string or the string in the body of the email. If the string you are searching for has spaces in it, wrap it in double quotes.
#     </td>
# </tr>

# <tr>
#     <td>'SEEN', 'UNSEEN'</td>
#     <td>
#     Returns all messages that have been seen or unseen. (Also known as read or unread)
#     </td>
# </tr>


#     <tr>
#     <td>'ANSWERED', 'UNANSWERED'</td>
#     <td>
#     Returns all messages that have been replied to or unreplied to. 
#     </td>
# </tr>


#     <tr>
#     <td>'DELETED', 'UNDELETED'</td>
#     <td>
#     Returns all messages that have been deleted or that have not been deleted.
#     </td>
# </tr>


# </table>

# You can also use the logical operators AND and OR to combine the above statements. Check out the full list of search keys here: http://www.4d.com/docs/CMU/CMU88864.HTM.

# Please note that some IMAP server providers for different email services will have slightly different syntax. You may need to experiment to get the results you want.






