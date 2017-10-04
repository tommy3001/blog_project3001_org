# functions to get system values:
from psutil import cpu_percent, network_io_counters
# functions to take a break:
from time import sleep
# package for email services:
import smtplib
import string
# package for web services:
from urllib import urlopen

atack = 0
counter = 0
while atack < 4:
    sleep(4)
    counter = counter + 1
    # check the cpu usage
    if cpu_percent(interval = 1) > 70:
        atack = atack + 1;
    # check the net usage
    neti1 = network_io_counters()[1]
    neto1 = network_io_counters()[0]
    sleep(1)
    neti2 = network_io_counters()[1]
    neto2 = network_io_counters()[0]
    net = ((neti2+neto2) - (neti1+neto1))/2
    if net > 400000:
        atack = atack + 1

    if counter > 20:
        atack = 0
        counter = 0
    # check the availability of the website
    try:
        if urlopen("http://www.project3001.org").getcode() != 200:
            atack = 4
    except:
            atack = 4

# write a very important email if atack is higher then 3
TO = "webmaster@project3001.org"
FROM = "postmaster@project3001.org"
SUBJECT = "We are under atack!!"
text = "Go and protect your server."
BODY = string.join((
     "From: %s" % FROM,
     "To: %s" % TO,
     "Subject: %s" % SUBJECT,
     "",
     text
     ), "\r\n")
server = smtplib.SMTP('127.0.0.1')
server.sendmail(FROM, [TO], BODY)
server.quit()
