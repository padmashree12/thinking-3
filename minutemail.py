import requests
from endpoints import NEW_EMAIL, MESSAGE_AFTER, MESSAGE_COUNT


class Mail(object):
    """
    Python wrapper for 10minutemail.com
    """

    def __init__(self):
        self.session = requests.session()
        self.message_count = 0
        self.messages = []
        resp = self.session.get(NEW_EMAIL, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

        })
        print(resp.text)
        self.mail = resp.json()['address']

    def get_mail(self):
        """
        :return: Mail of the current instance
        """
        return self.mail

    def get_message(self):
        """
        :return: list of messages stored in this instance
        """
        return self.messages

    def fetch_message(self):
        """
        Fetches for new messages which are not present in the instance
        :return: List of messages stored in the instance
        """
        res = self.session.get(MESSAGE_AFTER + str(self.message_count), headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }).json()
        self.message_count += len(res)
        self.messages += res
        return self.messages

    def new_message(self):
        """
        Check whether there are new messages or not
        :return: bool
        """
        return self.session.get(MESSAGE_COUNT, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }).json()['messageCount'] != self.message_count

    def __str__(self):
        return self.mail


if __name__ == "__main__":
    import time
    mail = Mail()
    print(mail.get_mail())
    while True:
        time.sleep(2)
