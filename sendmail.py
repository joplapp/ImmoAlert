import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# AWS Config
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = 'foo'
EMAIL_HOST_PASSWORD = 'bar'
EMAIL_PORT = 587
EMAIL_SENDER = 'johannes@plapp.de'

RECEIVER = "johannes@plapp.de"

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

    msg = MIMEMultipart('alternative')
    msg['Subject'] = TEMPLATE_TITLE.format_map(obj)
    msg['From'] = EMAIL_SENDER
    msg['To'] = RECEIVER

    mime_text = MIMEText(TEMPLATE_CONTENT.format_map(obj), 'text')
    msg.attach(mime_text)

    #s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    #s.starttls()
    #s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    #s.sendmail(me, you, msg.as_string())
    #s.quit()