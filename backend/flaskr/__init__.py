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
      response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE')
      return response

  '''
  @TODO: DONE
  Create an endpoint to handle GET requests 
  for all available categories.
  '''

  def construct_categories_dic():
    all_categories = Category.query.order_by(Category.id).all()
    categories_dic = {}
    for category in all_categories:
      categories_dic[category.id]= category.type
    return categories_dic
  
  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories_dic=construct_categories_dic()
    print(categories_dic)
    return jsonify({
      'success': True,
      'categories': categories_dic
    })

  '''
  @TODO: DONE
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
      'categories': construct_categories_dic()
    })

  '''
  @TODO: DONE
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question=Question.query.get(question_id)
      question.delete()
      return jsonify({
        'success': True,
        'question_id': question_id
      })
    except:
      abort(422)

  '''
  @TODO: DONE
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
  @TODO: DONE
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_questions_based_on_category(category_id):
    current_category=Category.query.get(category_id)
    print(current_category.format())
    if current_category is None:
      abort(404)
    questions = Question.query.filter_by(category=category_id).all()
    paginated_questions = paginate_questions(request, questions)
    return jsonify({
      'success': True,
      'questions': paginated_questions,
      'total_questions': len(questions),
      'current_category': category_id
    })

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

    