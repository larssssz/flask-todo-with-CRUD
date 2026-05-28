import unittest
import json
from app import app, db, Todo


class APITestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True

        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    # =========================
    # CREATE TASK TEST
    # =========================
    def test_create_task(self):
        response = self.client.post(
            '/api/tasks',
            data=json.dumps({
                'title': 'Study Flask'
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

    # =========================
    # READ TASKS TEST
    # =========================
    def test_get_tasks(self):
        response = self.client.get('/api/tasks')

        self.assertEqual(response.status_code, 200)

    # =========================
    # UPDATE TASK TEST
    # =========================
    def test_update_task(self):

        with app.app_context():
            task = Todo(
                title='Old Task',
                complete=False
            )

            db.session.add(task)
            db.session.commit()

            task_id = task.id

        response = self.client.put(
            f'/api/tasks/{task_id}',
            data=json.dumps({
                'title': 'Updated Task',
                'complete': True
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    # =========================
    # DELETE TASK TEST
    # =========================
    def test_delete_task(self):

        with app.app_context():
            task = Todo(
                title='Delete Me',
                complete=False
            )

            db.session.add(task)
            db.session.commit()

            task_id = task.id

        response = self.client.delete(
            f'/api/tasks/{task_id}'
        )

        self.assertEqual(response.status_code, 200)

    # =========================
    # NEGATIVE TEST
    # =========================
    def test_task_not_found(self):

        response = self.client.put(
            '/api/tasks/999',
            data=json.dumps({
                'title': 'Nothing'
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()