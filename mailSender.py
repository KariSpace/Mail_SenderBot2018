import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def email_sender(name, email, subject, type):
    with open(str(type) + ".txt", 'r') as file:
        html = file.read().replace('\n', '').format(code=str(name))
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    message = Mail(
        from_email="",
        to_emails=email,
        subject=subject,
        html_content=html)
    try:
        response = sg.send(message)
        print(response.status_code)
        '''
        print(response.body)
        print(response.headers)
        '''
        return 0
        
    except Exception as error:
        print(str(error))
        return error


print(email_sender('kari', '', 'try it', 1))
