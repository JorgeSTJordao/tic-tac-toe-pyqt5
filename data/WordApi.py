import requests


class WordApi:
    """
    Api class
    """

    def __init__(self, url):
        self.url = url

    def request(self):
        """
        request ten words from api

        :return: An array of strings representing which words were selected
        """

        words = requests.get(self.url)
        return words.json()

