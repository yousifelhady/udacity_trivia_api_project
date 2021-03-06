# Udacitrivia

This project enables you to do the following:
1. Add a question with specific category and difficulty
2. Display all questions in the Home page or List page
3. Get questions per category if you clicked on any category at Home page
4. Search for specific word in any question, all matched questions shall be displayed in search result regardlress of their category
5. Delete a question using the 'bin' button under each displayed question
6. Show question answer by clicking on 'Show Answer'
7. Play the trivia game which is:
    - Choose one category to get questions from, or Choose 'All' to get questions from any category
    - A question shall be displayed and you have to guess the answer
    - Submit the answers
    - The quiz composed of 5 questions and after you submitted all the answers, a final score appears for you
    - After finishing the quiz 5 questions and got the score, you can play again!

## Pre-requisites to run the project

1. Python 3.7 should be installed at your machine
2. Clone the project's repo
3. Navigate to `'/backend'` and install all project's dependencies by running this command at your CMD:
```bash
  pip install -r requirements.txt
```
##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight postgres database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

4. In order to run the application, type these commands at your CMD:
```bash
  set FLASK_APP=flaskr
  set FLASK_ENV=development
  flask run
```
  Where:
  - Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
  - Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.
  - Application runs on 'http://127.0.0.1:5000/' by default

5. In order to run the website and visualize it, navigate to `'/frontend'` and type these commands at your CMD:
```bash
  npm install
  npm start
```
  The website frontend runs on 'http://localhost:3000/' and it opens immediately as 'React App' at your browser

6. Make sure to connect to the postgres database by configuring it in `'/backend/models.py'`


## Tests

In order to run tests, navigate to `'/backend'` and run the following commands at the CMD:
```bash
  dropdb trivia_test
  createdb trivia_test
  psql trivia_test < trivia.psql
  python test_flaskr.py
```
  
Note: If this is your first time to run tests, you don't have to execute the 'dropdb' command

All tests are implemented in test_flask.py and should be maintained and updated if any changes occured in the backend endpoints handlers to make sure that the application is behaving correctly


## API Reference

Please check the 'README' file included in `'/backend'` folder for reference


## Authors

Software Engineer: Yousif Elhady


## Acknowledgements

Thanks to all my mentors and colleagues at Udacity Web development nano-degree program
