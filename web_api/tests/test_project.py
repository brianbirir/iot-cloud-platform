import uuid
import random
import unittest

from src import create_app


class ProjectTest(unittest.TestCase):
    def setUp(self):
        """create application and client"""
        self.app = create_app(config_object='config.TestingConfig')
        self.app_client = self.app.test_client()
        self._post_test_data = {
            "project_name":
            "project_{random_num}".format(random_num=random.randint(1, 1000)),
            "project_description":
            "{random_uuid}".format(random_uuid=uuid.uuid4())
        }

    def tearDown(self):
        pass

    def test_successful_project_registration(self):
        """test successful registration a new project"""
        resp = self.app_client.post('api/project', json=self._post_test_data)
        self.assertEqual(200, resp.status_code)

    def test_get_single_project_success(self):
        """test when retrieving a single project"""
        project_id = 1
        resp = self.app_client.get(
            'api/project?project_id={project_id}'.format(
                project_id=project_id))
        self.assertEqual(200, resp.status_code)

    def test_get_single_project_failure(self):
        """test when a project is missing"""
        project_id = 10000
        resp = self.app_client.get(
            'api/project?project_id={project_id}'.format(
                project_id=project_id))
        self.assertEqual(404, resp.status_code)

    def test_update_project(self):
        """test when updating a project"""
        pass

    def test_delete_project(self):
        """test when a project is deleted"""
        pass
