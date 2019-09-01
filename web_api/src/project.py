from datetime import datetime
from flask_restful import Resource, reqparse

from src.model import ProjectModel


class Project(Resource):
    @staticmethod
    def get_project_id_parsed_args():
        """Parses project id arg received from the HTTP request.

        Returns:
            A dictionary of the parsed request argument

        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            'project_id',
            type=int,
            help='The ID for the project is missing or wrongly formatted',
            required=True,
            location='args')
        return parser.parse_args()

    @staticmethod
    def get_project_parsed_args():
        """Parses project args received from the HTTP POST request.

        Returns:
            A dictionary of the parsed request argument

        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            'project_name',
            type=str,
            help='The name of the project is missing or wrongly formatted',
            required=True)
        parser.add_argument(
            'project_description',
            type=str,
            help=
            'The description of the project is missing or wrongly formatted',
            required=True)
        return parser.parse_args()

    @staticmethod
    def check_existing_project(project_name):
        """Returns query object of an existing project or null"""
        return ProjectModel.query.filter_by(name=project_name).first()

    def get(self):
        """Returns a project's details as HTTP response based on HTTP request

        Returns:
            JSON object: A 200 HTTP status response with details of a user

            JSON object: A 404 HTTP status response for a non-existing user

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status
            and JSON content-type response

        """
        project_id = self.get_project_id_parsed_args()

        try:
            project = ProjectModel.query.filter_by(
                id=project_id['project_id']).first()
            if project:
                response = {
                    "project_id": project.id,
                    "project_name": project.name
                }
                return response, 200
            else:
                return {"message": "The project does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    def post(self):
        """Registers a new project via POST HTTP request

        Returns:
            JSON object: A 200 HTTP status response with the name of the project

            JSON object: A 400 HTTP status response for an existing project

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and
                JSON content-type response

        """
        project_details = self.get_project_parsed_args()

        try:
            if not self.check_existing_project(
                    project_details['project_name']):
                user = ProjectModel(
                    name=project_details['project_name'],
                    description=project_details['project_description'])
                user.save_to_db()
                return {
                    "message":
                    "Project {} was created".format(
                        project_details['project_name'])
                }, 200
            else:
                return {"message": "The project already exists"}, 400
        except Exception as e:
            return {"message": str(e)}, 500

    def put(self):
        """Updates details of a project via PUT HTTP request

        Returns:
            JSON object: A 200 HTTP status response with name of the updated project

            JSON object: A 404 HTTP status response for a project that does not exist

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and
                JSON content-type response

        """
        project_id = self.get_project_id_parsed_args()
        project_details = self.get_project_parsed_args()

        try:
            project = ProjectModel.query.filter_by(
                id=project_id['project_id']).first()

            if project:
                project.name = project_details['name']
                project.description = project_details['project_uuid']
                project.updated_at = datetime.utcnow()
                project.save_to_db()
                return {
                    "message":
                    "Project {} was updated".format(project_details['name'])
                }, 200
            else:
                return {"message": "The project does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    def delete(self):
        """Deletes a project via DELETE HTTP request

        Returns:
            JSON object: A 200 HTTP status response with confirmation message of the deleted project

            JSON object: A 404 HTTP status response for a project that does not exist

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and
                JSON content-type response

        """
        project_id = self.get_project_id_parsed_args()

        try:
            project = ProjectModel.query.filter_by(
                id=project_id['project_id']).first()

            if project:
                project.delete_from_db()
                return {
                    "message": "The project has been deleted successfully"
                }, 200
            else:
                return {"message": "The project does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
