import requests  # - HTTP Request
from bs4 import BeautifulSoup  # - Web Scraping
import smtplib  # - Send Email

# ` Email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ` System date and time manipulation.
import datetime

now = datetime.datetime.now()

# ? Email Content Placeholder.

content = ""

# ? Extracting Hacker News Stories


def extractNews(url):
    print("Extracting Hacker News Stories...")
    cnt = ""  # - Placeholder to assign values to `content` variable
    cnt += "<b>Hacker News top stories : </b>\n" + "<br>" + "-" * 50 + "<br>"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    for i, tag in enumerate(
        soup.find_all("td", attrs={"class": "title", "valign": ""})
    ):
        cnt += (
            (str(i + 1) + " :: " + tag.text + "\n" + "<br>")
            if tag.text != "More"
            else ""
        )
    return cnt


cnt = extractNews("https://news.ycombinator.com/")
content += cnt
content += "<br>-----<br>"
content += "<br><br>End of Message FROM :- Shantanu G Mane"

# ` Lets send the email...

print("Composing Email...")

# $ Updating the email details

SERVER = "smtp.gmail.com"  # -'your smtp server'
PORT = 587  # - our port number
FROM = "shantanu.mane.200@gmail.com"  # - 'senders email ids'
TO = ["manesg@rknec.edu","shantanu.mane.200@outlook.com"]  # - 'clients email ids' (can be a list)
PASS = "nevergetinlaid20"  # - 'sender's email password'

msg = MIMEMultipart()

msg["Subject"] = (
    "Top News Stories of Hacker News [Automated Email]"
    + " "
    + str(now.day)
    + "-"
    + str(now.month)
    + "-"
    + str(now.year)
)
msg["From"] = FROM
msg["To"] = TO

msg.attach(MIMEText(content, "html"))

print("Initializing server...")

server = smtplib.SMTP(SERVER, PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print("Email Sent...")

server.quit()
