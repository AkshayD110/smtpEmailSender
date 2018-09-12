import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mailSender:

    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return f'{self.__class__.__name__} class in Send Mail module'

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self,msg):
        if msg:
            self._msg = msg
        else:
            raise ValueError("MailSender method called without msg object")



    def sendMail(self):
        pass