# Trivia API Backend Documentation

## Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. 
- The backend app runs at `http://127.0.0.1:5000/`
- Authentication: This version of the application does not require authentication or API keys.
- Connect to Postgres Database by configuring the Database name, Username and Password at `models.py`

## Error Handling

Errors are returned as JSON objects in the following format:
```bash
{
    "success": False,
    "error": 404,
    "message": "Not Found"
}
```

The API will return three error types when requests fail or request data cannot be found:
- 404: Resource Not Found
- 422: Request in Unprocessable
- 405: Method is not allowed

## Endpoint Library

```
GET '/categories'
GET '/questions'
GET '/questions/search'
GET '/categories/<int:category_id>/questions'
POST '/questions'
POST '/quizzes'
DELETE '/questions/<int:question_id>'
```

#### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: JSON Object
- Sample: `curl http://127.0.0.1:5000/categories`
```
    {
      "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
      }, 
      "success": true
    }
```

#### GET '/questions'
- Fetches all questions existing in the database table "questions", total number of questions and existing categories
- Resulted list of questions are paginated in groups of 10
- Request Arguments: None
- Returns: JSON Object
- Sample: `curl http://127.0.0.1:5000/questions`
```
    {
      "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
      }, 
      "questions": [
        {
          "answer": "Apollo 13", 
          "category": 5, 
          "difficulty": 4, 
          "id": 2, 
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }
        .
        .
        .
       ], 
      "success": true, 
      "total_questions": 23
  }
```

#### GET '/questions/search'
- Fetches all questions that contains the 'searchTerm' as a substing in question text
- Request Arguments: 'searchTerm'
- Returns: JSON Object
- Sample: `curl http://127.0.0.1:5000/questions/search?searchTerm=title`
```
    {
      "questions": [
        {
          "answer": "Maya Angelou", 
          "category": 4, 
          "difficulty": 2, 
          "id": 5, 
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
          "answer": "Edward Scissorhands", 
          "category": 5, 
          "difficulty": 3, 
          "id": 6, 
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
      ], 
      "success": true, 
      "total_questions": 2
    }
```

#### GET '/categories/<int:category_id>/questions'
- Fetches questions per specific category and their count
- Questions are paginated in groups of 10
- Request Arguments: category_id
- Returns: JSON Object
- Sample: category_id=6 `curl http://127.0.0.1:5000/categories/6/questions`
```
    {
      "current_category": 6, 
      "questions": [
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
          "answer": "Uruguay", 
          "category": 6, 
          "difficulty": 4, 
          "id": 11, 
          "question": "Which country won the first ever soccer World Cup in 1930?"
        }
      ], 
      "success": true, 
      "total_questions": 2
    }
```

#### POST '/questions'
- Add a question to questions database table
- Request Arguments: 'question', 'answer', 'category', 'difficulty'
- Returns: JSON Object contains added question_id
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d "{"question": "Hydrocloric Acid chemical formula", "answer": "HCL", "category": "1", "difficulty": 3}"`
```
    {
      "question_id": 31,
      "success": true
    }
```

#### POST '/quizzes'
- Starts Trivia quiz by allowing user to select a category and then displaying random questions from that category and let user guesses the answer of each question, then displays the score
- Request Arguments: 'previous_questions' list, 'quiz_category'
- Returns: JSON Object contains question to be displayed in front-end
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d "{"previous_questions": [], "quiz_category": {"id": 1, "type": "Science"}}"`
```
    {
      "previousQuestions": [],
      "question": {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
      },
      "quizCategory": 1,
      "success": true
    }
```

#### DELETE '/questions/<int:question_id>'
- Deletes a question from questions database table
- Request Arguments: question_id
- Returns: JSON Object contains deleted question_id
- Sample: question_id=31 `curl http://127.0.0.1:5000/questions/31 -X DELETE`
```
    {
      "question_id": 31,
      "success": true
    }
```
