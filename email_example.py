import smtplib
import ssl
import credentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def example():
    company_name = "Law Office of A & B Example"
    print("Thank you for calling the Law office of A and B")
    # Information that we need to gather for the client
    caller_name = str.title(input("What is the caller's name? "))
    caller_phone = str(input("What is the caller's phone? "))
    caller_email = str(input("What is the caller's email? "))
    current_client = str.capitalize(input("Are you a current client? Yes or No "))
    if current_client == "Yes":
        attorney = str.capitalize(input("Who is the attorney assigned to your case? A or B "))
        case_number = str.upper(input("What is your case #? "))
        county = str.title(input("What county is your case in? "))
        next_court_date = str(input("When is your next court date? "))
        message1 = str(input("What is the message? "))
    else:
        type_legal_case = str.capitalize(input("What type of legal case are you calling about? "))
        been_filed = str.capitalize(input("Has the case already been filed? Yes or No "))
        if been_filed == "Yes":
            county = str(input("What county was the case filed in? "))
            next_court_date = str(input("When is your next court date? If no court date type 'NA' "))
        client_source = str(input("How did you hear about the firm? "))
        message1 = str(input("What is the message "))
        if current_client == "No":
            attorney = "Potential Client"
        if been_filed == "No":
            county = "NA"
            next_court_date = "NA"

    # Email Information Starts Here
    sender_email = credentials.username
    receiver_email = "email@domainname.com"
    # Sender Email Password
    password = credentials.password

    message = MIMEMultipart("alternative")
    message["Subject"] = f"{company_name} Phone Call - {attorney}"
    message["From"] = sender_email
    message["To"] = receiver_email

    if current_client == "Yes":
        # Create HTML version of message

        # Current client
        html = f"""\
        <html>
        <div><i>This message was crafted automatically.</i></div>
        <div><br></div>
        <div><b>Name: </b>{caller_name}</div>
        <div><br></div>
        <div><b>Phone Number: </b>{caller_phone}</div>
        <div><br></div>
        <div><b>Email: </b>{caller_email}</div>
        <div><br></div>
        <div><b>Current client? </b>{current_client}</div>
        <div><br></div>
        <div><i>*If Current client*</i></div>
        <div><b>Who is the attorney assigned to your case? </b>{attorney}</div>
        <div><br></div>
        <div><b>What case are you calling about? </b>{case_number}</div>
        <div><br></div>
        <div><b>What county is your case in? </b>{county}</div>
        <div><br></div>
        <div><b>Next court date: </b>{next_court_date}</div>
        <div><br></div>
        <div><b>Message: </b> {message1}</div>
        <div><br></div>
        <div><div>Thank you,<br></div>
        <div>Your Name</div>
        <div>Ph:<a href="tel:(210)%20555-5555" value="+12105555555" target="_blank">210-555-5555</a><br></div>
        <div><a href="https://www.google.com/" target="_blank" data-saferedirecturl="https://www.google.com/">www.google.com</a></div></div></div>
        </html>
        """
    else:
        # Potential Client and case has been filed
        html = f"""\
        <html>
        <div><i>This message was crafted automatically.</i></div>
        <div><br></div>
        <div><b>Name: </b>{caller_name}</div>
        <div><br></div>
        <div><b>Phone Number: </b>{caller_phone}</div>
        <div><br></div>
        <div><b>Email: </b>{caller_email}</div>
        <div><br></div>
        <div><b>Current client? </b>{current_client}</div>
        <div><br></div>
        <div><i>*If New/Potential Client*</i></div>
        <div><b>What type of legal case are you calling about? </b>{type_legal_case}</div>
        <div><br></div>
        <div><b>Has the case already been filed? </b>{been_filed}</div>
        <div><br></div>
        <div><b>What county will the case be filed in? </b>{county}</div>
        <div><br></div>
        <div><b>Next court date: </b>{next_court_date}</div>
        <div><br></div>
        <div><b>How did you hear about the firm? </b>{client_source}
        <div><br></div>
        <div><b>Message: </b> {message1}</div>
        <div><br></div>
        <div><div>Thank you,<br></div>
        <div>Your Name</div>
        <div>Ph:<a href="tel:(210)%20555-5555" value="+12105555555" target="_blank">210-555-5555</a><br></div>
        <div><a href="https://www.google.com/" target="_blank" data-saferedirecturl="https://www.google.com/">www.google.com</a></div></div></div>
        </html>
         """
    # Turn these into html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
