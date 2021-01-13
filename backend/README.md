# Trivia API Backend Documentation

## Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. 
- The backend app runs at `http://127.0.0.1:5000/`
- Authentication: This version of the application does not require authentication or API keys.
- Connect to Postgres Database by configuring the Database name, Username and Password at `models.py'

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



REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```
