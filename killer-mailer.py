#!/usr/bin/python

# Import smtplib for the actual sending function
import smtplib
import argparse

# Import the email modules we'll need
from email.mime.text import MIMEText


parser = argparse.ArgumentParser(description='This is a demo script by Amey Jadiye')
parser.add_argument('-s','--subject', help='Subject',required=True)
parser.add_argument('-b','--body',help='Body', required=True)
parser.add_argument('-t','--to',help='To', required=True)
parser.add_argument('-f','--sender',help='From', required=False)
args = parser.parse_args()

msg = MIMEText(args.body)
# me == the sender's email address
# you == the recipient's email address
me="demo@any-domain-you-want.com"
if args.sender is not None:
        me=args.sender
you=args.to
msg['Subject'] = args.subject
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
