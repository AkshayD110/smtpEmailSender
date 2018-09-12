import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mailSender:

    def __init__(self, body, fromaddr, toaddr, subject):
        self.body = body
        self.fromaddr = fromaddr
        self.toaddr = toaddr
        self.subject = subject

    def __repr__(self):
        return f'{self.__class__.__name__} class in Send Mail module'

    @property
    def msg(self):
        return self._body

    @msg.setter
    def msg(self,body):
        if body:
            self._body = body
        else:
            raise ValueError("MailSender method called without msg object")

    def sendMail(self):
        message = MIMEMultipart()
        message['From'] = self.fromaddr
        message['To'] = self.toaddr
        message['Subject'] = self.subject
        message.attach(MIMEText(self.body, 'plain'))
        server = smtplib.SMTP(host='yourhost', port="yourport")
        #server.send_message(message)
        server.sendmail(self.fromaddr, self.toaddr.split(','), message.as_string())
        print("done")



