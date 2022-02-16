import smtplib
import imghdr
from email.message import EmailMessage



def send_for_mail(recievers_email, subject, content, img=None)->bool:
    try:
        Sender_Email = "amritsubramanian.c@gmail.com"
        Reciever_Email = recievers_email
        Password = 'amma@@1953'
        newMessage = EmailMessage()                         
        newMessage['Subject'] = subject
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email                   
        newMessage.set_content(content) 
        if img:
            with open(img, 'rb') as f:
                image_data = f.read()
                image_type = imghdr.what(f.name)
                image_name = f.name
            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        else: pass
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)
            
        return True
    except: return False
    
if __name__=='__main__':
    pass