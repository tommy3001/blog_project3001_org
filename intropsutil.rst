.. _intropsutil:

****************************************************
-Python Packages- Part 5: Psutil
****************************************************


I wrote a small Python script to be ready for the next Mars invasion. It is running all the time on my server.
It checks only some system values like CPU and net usage and the availability of project3001.org.
If there is an overload or the address is not available, the program sends an email.
This can be a protection against  `DDoS atacks <http://en.wikipedia.org/wiki/Denial-of-service_attack>`_. (Please not me, I'm one of the good guys!!)

`Psutil <https://github.com/giampaolo/psutil>`_  is a small package with very useful system functions.
All the needed functions to check the performance of my server are inside this package.

`Smtplib <http://docs.python.org/3/library/smtplib.html>`_   is the Python package for sending emails
and the package  `Urllib <http://docs.python.org/3/library/urllib.html>`_   has some additional web functions.

.. code-block:: python
    :linenos:

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


The function `cpu_percentage` in line 16 is relative simple to use. The interval parameter is the time in seconds in which the function is
measuring the CPU usage. The function `network_io_counters` is a tuple of all send bytes for the in and out direction.
Therefore it is necessary to call the function with a small time delay and to calculate the difference to get the transmitted bytes (line 19-25).
There is a while loop inside (line 13) to be sure that there is really a problem. The loop is counting the issues.

In line 35 the program is checking the response of the website (status code 200 means the web server is available).
This is included in a try-error handler. If the page is not available, urlopen send back an error message.
In this case the atack counter is set directly to 4. Because this is a very bad issue....

I think the last part of the program is mostly self explaining. There is the emergency email prepared in
the case of some not normal behaviours of the server with the `smtplib` package.

`server = smtplib.SMTP('127.0.0.1')` is my email server and

`server.sendmail(FROM, [TO], BODY)` is the command to send the email. Nearly so easy as outlook...
