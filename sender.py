import smtplib
from email import encoders
# from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


"""
in google smtp in order to use it:
1- you should enable 2 factor authentication
2- create app passcode
3- use app passcode as a password for the specified gmail
"""


def sendViaGmail(senderMail,password,recipient,subject,body):
    """

    all parameters: str
    :param senderMail: enter the sender email
    :param password: enter the passcode app as password
    :param recipient: enter receiver mail
    :param subject: enter subject
    :param body: enter you main message
    :return: true if success or error message if fail
    """
    result = 'initial result'

    try:
        mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mailServer.ehlo()
        mailServer.login(senderMail,password)
        print('authenticated successfully')

        msg = MIMEMultipart()
        msg['From'] = senderMail
        msg['To'] = recipient
        msg['Subject'] = subject

        message = body
        msg.attach(MIMEText(message, 'plain'))

        text = msg.as_string()
        mailServer.sendmail(senderMail,recipient,text)
        print('message sent')
        result = True
    except smtplib.SMTPHeloError:
        result = 'The server didn’t reply properly to the HELO greeting.'
    except smtplib.SMTPAuthenticationError:
        result = 'The server didn’t accept the username/password combination.'
    except smtplib.SMTPNotSupportedError:
        result = 'The AUTH command is not supported by the server.'
    except smtplib.SMTPException:
        result = 'No suitable authentication method was found.'
    except Exception:
        result = 'general exception'
    finally:
        if result != 'general exception':
            mailServer.quit()
        return result


def main():
    toAddress = 'nichol2@awgarstone.com'
    with open('password.txt', 'r') as f:
        password = f.read()
    with open('email.txt', 'r') as f:
        email = f.read()

    subject = 'test subject w keda'
    body = 'dih el msg body 7ottelak ay kalam for ex: loreum epseum dolar sit amit'
    return sendViaGmail(email,password,toAddress,subject,body)


if __name__ == '__main__':
    main()
