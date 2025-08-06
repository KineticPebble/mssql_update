'''
Send direct email without any authentication

2 functions:
    - send_mail
    - log_html

log html is used in send_email message body
'''

import auth
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(html: str, receiver_email: list | str, attachment: list=False) -> None:
    '''Send email to reciver email with or without attachment
    
    Parameters:
        html: The message body to be sent. Can be HTNL formated message.
        receiver_email: one or a list of email recipients
        attachment: Location of attachment or attachments. Default is False which meanns no attachment

    Returns:
        None

    '''
    smtp_server = ""
    port = 25  # For starttls

    sender_email = ""
    # password = auth.gmail_password
    if type(receiver_email) == list: receiver_email_joined = ", ".join(receiver_email)
    else: receiver_email_joined = receiver_email
    message = MIMEMultipart()
    message["Subject"] = "file test"
    message["From"] = sender_email
    message["To"] = receiver_email_joined

    context = ssl.create_default_context()

    html_part = MIMEText(html, "html")
    message.attach(html_part) 

    if attachment != False:
        for fn in attachment:
            with open(fn, "rb") as filename:
                file_part = MIMEBase("application", "octet-stream")
                file_part.set_payload(filename.read())

            encoders.encode_base64(file_part)
            fname = fn.split('\\')[-1]
            file_part.add_header(
                "Content-Disposition",
                f"attachment; filename= {fname}",
            )
            message.attach(file_part)
        
    text = message.as_string()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context) # Secure the connection
        server.ehlo()
        
        server.sendmail(sender_email, receiver_email, text)
        print("email sent")
    except Exception as e:
        print(e)
    finally:
        server.quit() 

def log_html(log: str) -> str:
    '''Convert Log file to HTML messages

    Parameters:
        log: Location of the log text file

    Returns:
        HTML body
    '''
    fh = open(log)
    html = '<p>'
    for line in fh:
        html += f"{line.strip()}<br>"
    html += "<br>"
    return html


send_email("<p>Message</p>", "email@address", 
           attachment=[r'D:\Files\Input\Logs\Validation\D2_Validation.csv', r'D:\Files\Input\Logs\Validation\Insert_Validation.csv'])
