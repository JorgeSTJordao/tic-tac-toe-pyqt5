[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

<h1 align="center">Create a Hangman with Python</h1>
<hr>

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
```

# 🚀 Next Steps 

- For the interface we can improve create a website using Flask framwork
- We can create levels for the game (Easy level is for small and common words, Medium Level is for big words, and Hard Level for big or small words that are not common) | ⚠️ For this project is only english words |
