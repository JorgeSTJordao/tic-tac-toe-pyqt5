import requests


class WordApi:
    """
    Api class
    """

    def __init__(self):
        self.url = "https://random-word-api.herokuapp.com/word?number=10"

    def get_words(self):
        """
        get ten words from the api

        :return: An array of strings representing which words were selected
        """

        words = requests.get(self.url)

        return words.json()
