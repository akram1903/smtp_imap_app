import unittest
import sender
import receiver

with open('password.txt', 'r') as f:
    password = f.read()
with open('email.txt', 'r') as f:
    email = f.read()
with open('email2.txt', 'r') as f:
    email2 = f.read()

subject = 'test subject w keda'
body = 'dih el msg body 7ottelak ay kalam for ex: loreum epseum dolar sit amit'


class MyTestCase(unittest.TestCase):

    def test_sender_failings(self):
        cases = [sender.sendViaGmail('','','','',''),
                 sender.sendViaGmail('',password,email2,subject,body),
                 sender.sendViaGmail(email,'',email2,subject,body),
                 sender.sendViaGmail(email,password,'',subject,body),]

        self.assertNotIn(True,cases)

    def test_sender_success(self):
        self.assertTrue(
                 sender.sendViaGmail(email,password,email2,subject,body))
    def test_receiver(self):
        self.assertTrue(receiver.receiveViaGmail(email,password,'FROM a5asgpt.us@gmail.com'))


if __name__ == '__main__':
    unittest.main()
