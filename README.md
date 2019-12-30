# AutomateTheBoringStuff

Welcome to the AutomateTheBoringStuff wiki!

These are some files that follow along the course "Automate the Boring stuff"

For more details visit: http://automatetheboringstuff.com/

It's awesome!



Sending Emails:
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)

conn.ehlo()
conn.starttls()


#Enter the credentials
conn.login('{USERNAME}', '{PASSWORD}')

conn.sendmail('{ADRESS_SENDER}', '{ADRESS_RECEIVER}', 'Subject: So long... \n\nDear X, \n this is a test')
{}

-> You will recive a BLANK dictionary if the email was sent correctly


conn.quit()
