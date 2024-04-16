import imaplib
import email


def receiveViaGmail(account,password,criteria="ALL"):
    """

    :param account: enter listener account
    :param password: enter pass
    :param criteria: criteria for search and filtering, initial = "ALL"
    :return: 2 elements true if no exceptions and data, message error otherwise + None
    """
    imap_server = 'imap.gmail.com'
    server_port = 993

    result = 'initial result'
    messages = []
    try:
        imap = imaplib.IMAP4_SSL(imap_server,port=server_port)
        imap.login(account,password)

        print('logged in successfully')

        imap.select('Inbox')

        _, msgnums = imap.search(None,criteria)

        for msgnum in msgnums[0].split():
            _, data = imap.fetch(msgnum,"(RFC822)")

            message = email.message_from_bytes(data[0][1])
            print(f"Message number: {msgnum}")
            print(f"From: {message.get('From')}")
            print(f"To: {message.get('To')}")
            print(f"BCC: {message.get('BCC')}")
            print(f"Date: {message.get('Date')}")
            print(f"Subject: {message.get('Subject')}")

            print("Content")
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    print(part.as_string())

            messages.append(message)

        result = True
    except imaplib.IMAP4_SSL.readonly:
        result = 'This exception is raised when a writable mailbox has its status changed by the server.' \
                 ' This is a sub-class of IMAP4.error. Some other client now has write permission,' \
                 ' and the mailbox will need to be re-opened to re-obtain write permission.'
    except imaplib.IMAP4_SSL.abort:
        result = 'IMAP4 server errors cause this exception to be raised. This is a sub-class of IMAP4.error.' \
                 ' Note that closing the instance and instantiating a new one will usually allow recovery from' \
                 ' this exception.'
    except imaplib.IMAP4_SSL.error:
        result = 'Exception raised on any errors.' \
                 ' The reason for the exception is passed to the constructor as a string.'
    except Exception:
        result = 'general exception'
    finally:
        if result != 'general exception':
            imap.close()
        if result is True:
            return result,messages
        else:
            return result,None


def main():
    with open('email2.txt', 'r') as f:
        senderMail = f.read()
    with open('password.txt', 'r') as f:
        password = f.read()
    with open('email.txt', 'r') as f:
        email_address = f.read()

    criteria = f'FROM "{senderMail}"'
    return receiveViaGmail(email_address,password,criteria)


if __name__ == '__main__':
    main()
