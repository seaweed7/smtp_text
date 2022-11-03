import smtplib

## functions to use gmail SMTP servers to programmatically send an email or text
## you will need to enable 2FA in your gmail account to allow a program to login for you
## input your number phone number + @phoneproviderdomain to send a text to your phone via email
##   example: 1234567890@txt.att.net

#function for sending text message using gmail servers
def send_text(message, pnum):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    from_email = [your email]

    #phone carrier SMS domains
    #Verizon: @vtext.com
    #AT&T: @txt.att.net
    #Cricket: @sms.mycricket.com
    #Sprint: @messaging.sprintpcs.com
    #T-Mobile: @tmomail.net
    #Virgin Moble: @vmobl.com

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    s.starttls()
    s.login([email account], [app password])

    s.sendmail(from_email, pnum, message)

    s.quit()
    s.close()


def send_email(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    from_email = [sender]
    to_email = [destination]

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    s.starttls()
    s.login([your email], [app password])
    s.sendmail(from_email, to_email, message)
    s.quit()
