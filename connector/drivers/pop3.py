import poplib
import email
from html.parser import HTMLParser
from django.conf import settings


class OtpParserOrbitMulti(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.is_otp = False
        self.otp = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # if tag == "div" and attrs.get("class") == "otp":
        if tag == "h3":
            self.is_otp = True

    def handle_data(self, data):
        if self.is_otp:
            self.otp = data
            self.is_otp = False


class OtpParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.is_otp = False
        self.otp = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # if tag == "div" and attrs.get("class") == "otp":
        if tag == "p" and attrs.get("class") == "token":
            self.is_otp = True

    def handle_data(self, data):
        if self.is_otp:
            self.otp = data
            self.is_otp = False


def delete_all_email(
    email_address: str = settings.DSC_EMAIL_ADDRESS,
    email_password: str = settings.DSC_EMAIL_PASSWORD,
    email_host: str = settings.DSC_EMAIL_HOST,
) -> None:
    pop_connect = poplib.POP3_SSL(email_host)
    # pop_connect.user(settings.DSC_EMAIL_ADDRESS)
    # pop_connect.pass_(settings.DSC_EMAIL_PASSWORD)
    pop_connect.user(email_address)
    pop_connect.pass_(email_password)

    num_messages = len(pop_connect.list()[1])
    print("Found number of email:", num_messages)

    for i in range(num_messages):
        print("Delete email number: ", i)
        pop_connect.dele(i + 1)

    pop_connect.quit()


def get_otp_code(
    email_address: str = settings.DSC_EMAIL_ADDRESS,
    email_password: str = settings.DSC_EMAIL_PASSWORD,
) -> str:
    pop_connect = poplib.POP3_SSL(settings.DSC_EMAIL_HOST)
    # pop_connect.user(settings.DSC_EMAIL_ADDRESS)
    # pop_connect.pass_(settings.DSC_EMAIL_PASSWORD)
    pop_connect.user(email_address)
    pop_connect.pass_(email_password)

    num_messages = len(pop_connect.list()[1])

    otp_code = ""

    for i in range(num_messages):
        raw_email = b"\n".join(pop_connect.retr(i + 1)[1])
        parsed_email = email.message_from_bytes(raw_email)
        # print(parsed_email.keys())

        # Delete email
        pop_connect.dele(i + 1)

        if parsed_email["Subject"] == "Code Verification":
            print("Get Email:", parsed_email["Subject"])
            for part in parsed_email.walk():
                if part.get_content_type():
                    body = part.get_payload(decode=True)
                    otp_parser = OtpParser()
                    otp_parser.feed(body.decode())
                    otp_code = otp_parser.otp

    pop_connect.quit()

    return otp_code


def get_otp_code_orbit_multi(
    email_address: str = settings.ORBIT_MULTI_EMAIL_ADDRESS,
    email_password: str = settings.ORBIT_MULTI_EMAIL_PASSWORD,
) -> str:
    pop_connect = poplib.POP3_SSL(settings.ORBIT_MULTI_EMAIL_HOST)
    # pop_connect.user(settings.DSC_EMAIL_ADDRESS)
    # pop_connect.pass_(settings.DSC_EMAIL_PASSWORD)
    pop_connect.user(email_address)
    pop_connect.pass_(email_password)

    num_messages = len(pop_connect.list()[1])

    otp_code = ""

    for i in range(num_messages):
        raw_email = b"\n".join(pop_connect.retr(i + 1)[1])
        parsed_email = email.message_from_bytes(raw_email)
        # print(parsed_email.keys())

        # Delete email
        pop_connect.dele(i + 1)

        if parsed_email["Subject"] == "Code Verification":
            print("Get Email:", parsed_email["Subject"])
            for part in parsed_email.walk():
                if part.get_content_type():
                    body = part.get_payload(decode=True)
                    otp_parser = OtpParserOrbitMulti()
                    otp_parser.feed(body.decode())
                    otp_code = otp_parser.otp

    pop_connect.quit()

    return otp_code
