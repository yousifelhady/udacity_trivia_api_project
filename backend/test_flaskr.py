import os
import unittest
import json
import random
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('Yousif', 'yousif', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'What is the formula of Hydrochloric Acid?',
            'answer': 'HCL',
            'category': '1',
            'difficulty': 3
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertTrue(res_data['categories'])

    def test_get_questions(self):
        res = self.client().get('/questions')
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertTrue(res_data['questions'])
        self.assertTrue(res_data['total_questions'])
        self.assertTrue(res_data['categories'])

    def test_delete_questions(self):
        all_questions = Question.query.all()
        all_questions_ids = [question.id for question in all_questions]
        question_id = random.choice(all_questions_ids)

        res = self.client().delete('/questions/{}'.format(question_id))
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertEqual(res_data['question_id'], question_id)

    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)
        res_data = json.loads(res.data)
        added_question = Question.query.order_by(Question.id.desc()).first()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertEqual(res_data['question_id'], added_question.id)

    def test_search_question(self):
        search_term = 'title'
        res = self.client().get('/questions/search', query_string={'searchTerm': search_term})
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertTrue(res_data['questions'])
        self.assertTrue(res_data['total_questions'], len(res_data['questions']))

    def test_search_question_no_match(self):
        search_term = 'blabla'
        res = self.client().get('/questions/search', query_string={'searchTerm': search_term})
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertEqual(res_data['questions'], [])
        self.assertEqual(res_data['total_questions'], 0)

    def test_get_questions_per_category(self):
        category_id = 1
        res = self.client().get('/categories/{}/questions'.format(category_id))
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertTrue(res_data['questions'])
        self.assertTrue(res_data['total_questions'])
        self.assertEqual(res_data['current_category'], category_id)

    def test_play_quiz(self):
        res = self.client().post('/quizzes', 
        json={'previous_questions': [], 
        'quiz_category': {'id': 1, 'type': 'Science'}})
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['success'], True)
        self.assertTrue(res_data['question'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()