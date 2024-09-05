[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

<h1 align="center"> Create a Hangman with Python</h1>

# :star: Aim Of The Project

Learn how to create a simple hangman game using Python and Object-Oriented Programming

# 📚 Table Of Contents

|      Layers     |                         Objective                          |
| :----------------: | :---------------------------------------------------: |
|    WordApi   |    It's an API where we get all the words we can use in our program   |
|    Databasewords   |    It's where a word is going to be chosen    |
|   Hangman  |  It's where all the logic of game happens  |
|   Interface  |  It's where the user can interact and see your results  |

<hr>

```python
  #Explained how to get data from the API

  #Ten words just
  url = "https://random-word-api.herokuapp.com/word?number=10"

  import requests

  words = requests.get(url)
  words_list = words.json()

  print(words_lists)

  >>> Out: [word0, word1, word(n - 1)]
```

# 🚀 Next Steps 

- Create a website using Flask framework and Bootstrap
- Treat exceptions

<h3>⚠️ For this project is only english words </h3>
