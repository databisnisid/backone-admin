import poplib
import email
from html.parser import HTMLParser
from django.conf import settings


class OtpParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.is_otp = False
        self.otp = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'div' and attrs.get('class') == 'otp':
            self.is_otp = True

    def handle_data(self, data):
        if self.is_otp:
            self.otp = data
            self.is_otp = False


def delete_all_email() -> None:
    pop_connect = poplib.POP3_SSL(settings.DSC_EMAIL_HOST)
    pop_connect.user(settings.DSC_EMAIL_ADDRESS)
    pop_connect.pass_(settings.DSC_EMAIL_PASSWORD)

    num_messages = len(pop_connect.list()[1])
    print("Found number of email:", num_messages)

    for i in range(num_messages):
        print("Delete email number: ", i)
        pop_connect.dele(i+1)


def get_otp_code() -> str:
    pop_connect = poplib.POP3_SSL(settings.DSC_EMAIL_HOST)
    pop_connect.user(settings.DSC_EMAIL_ADDRESS)
    pop_connect.pass_(settings.DSC_EMAIL_PASSWORD)

    num_messages = len(pop_connect.list()[1])

    otp_code = ""

    for i in range(num_messages):
        raw_email  = b"\n".join(pop_connect.retr(i+1)[1])
        parsed_email = email.message_from_bytes(raw_email)
        #print(parsed_email.keys())

        # Delete email
        pop_connect.dele(i+1)

        if parsed_email['Subject'] == 'Code Verification':
            print('Get Email:', parsed_email['Subject'])
            for part in parsed_email.walk():
                if part.get_content_type():
                    body = part.get_payload(decode=True)
                    otp_parser = OtpParser()
                    otp_parser.feed(body.decode())
                    otp_code = otp_parser.otp

    pop_connect.quit()

    return otp_code

