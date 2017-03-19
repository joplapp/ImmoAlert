import smtplib
from credentials import Credentials
from config import Config

from email.mime.text import MIMEText

# AWS Config
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = Credentials.user
EMAIL_HOST_PASSWORD = Credentials.password
EMAIL_PORT = 587
EMAIL_SENDER = 'johannes@plapp.de'

RECEIVER = Config.receiver

TEMPLATE_TITLE="""
    NEU - {rent}, {rooms} mit {area}, in {address}: {title}
"""

TEMPLATE_CONTENT="""
    Hi,
    es kam gerade eine neue Wohnung auf ImmoScout!

    {title}
    Miete: {rent}
    Fläche: {rooms} mit {area}
    Ort: {address}
    {link}

    Go for it!

    -- Dein ImmoScout-Scout

    Diese mail wurde von ImmoAlert gesendet. Wenn du solche mails nicht mehr erhalten willst,
    sende einfach ein Bild mit deiner neuen Wohnung an johannes@plapp.de.
"""

def sendMail(post):

    # parse class to obj -- this is obviously ugly
    obj = {
        'title': post.title,
        'rent': post.rent,
        'area': post.area,
        'rooms': post.rooms,
        'address': post.address,
        'link': post.link
    }

    msg = MIMEText(TEMPLATE_CONTENT.format_map(obj))

    msg['Subject'] = TEMPLATE_TITLE.format_map(obj)
    msg['From'] = EMAIL_SENDER
    msg['To'] = RECEIVER

    s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    s.starttls()
    s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    s.sendmail(EMAIL_SENDER, RECEIVER, msg.as_string())
    s.quit()