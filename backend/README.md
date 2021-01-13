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

####GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: JSON Object
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
