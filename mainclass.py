import  mailSender

fromaddr="noreply@actiance.com"
toaddr="user1@actiance.com, user2@actiance.com"
subject="No Attend"
body="Please check"
mail_sender_obj = mailSender.mailSender(body, fromaddr, toaddr, subject)
mail_sender_obj.sendMail()
