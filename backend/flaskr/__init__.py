import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, questions):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formated_questions = [question.format() for question in questions]
    current_questions = formated_questions[start:end]
    return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE')
      return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  def get_formated_categories():
    all_categories = Category.query.order_by(Category.id).all()
    categories = [category.format() for category in all_categories]
    return categories

  def get_categories_names():
    all_categories = Category.query.order_by(Category.id).all()
    categories = [category.type for category in all_categories]
    return categories

  def get_categories_id_types():
    all_categories = Category.query.order_by(Category.id).all()
    categories = [category.format_with_id() for category in all_categories]
    return categories

  def get_category_number_from_name(category_name):
    all_categories = Category.query.order_by(Category.id).all()
    categories_types_dic = [category.format_with_type() for category in all_categories]
    return categories_types_dic[category_name]

  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories = get_categories_names()
    #print(categories)
    return jsonify({
      'success': True,
      'categories': categories
    })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  @app.route('/questions', methods=['GET'])
  def get_questions():
    all_questions = Question.query.order_by(Question.id).all()
    paginated_questions = paginate_questions(request, all_questions)
    return jsonify({
      'success': True,
      'questions': paginated_questions,
      'total_questions': len(all_questions),
      'categories': get_categories_names(),
      'current_category': 1
    })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  @app.route('/questions', methods=['POST'])
  def add_question():
    try:
      json_request = request.get_json()
      question = json_request.get('question')
      answer = json_request.get('answer')
      category = json_request.get('category')
      difficulty = json_request.get('difficulty')
      print(category)
      newQuestion = Question(question=question, answer=answer, category=category, difficulty=difficulty)
      newQuestion.insert()
      question_id = newQuestion.id
      return jsonify({
        'success': True,
        'question_id': question_id
      })
    except:
      abort(422)

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    