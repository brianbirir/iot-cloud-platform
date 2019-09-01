from flask import current_app
from flask_restful import Resource

class TestApi(Resource):

    def get(self):
        """Returns a test HTTP response based on HTTP request

        This is just to confirm that the API RESTful web service works on initial run.
        
        Returns:
            JSON object: A 200 HTTP status response with details of test data
        """
        try:
            return {"message": "The Flask API web service works"}, 200
        except Exception as e:
            return {"message": str(e)}, 500
