"""Endpoint module for sensors' data"""
from flask_restful import Resource, reqparse

from src.services.service_influx import InfluxService


class SensorData(Resource):

    inf = InfluxService()

    def get(self):
        """Returns a device's data as HTTP response based on HTTP request

        Returns:
            JSON object: A 200 HTTP status response with data for a device

            JSON object: A 404 HTTP status response for a non-existing data

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status
            and JSON content-type response

        """
        try:
            resp_data = SensorData.inf.query_data()
            if resp_data:
                return resp_data, 200
            else:
                return {"message": "The device does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
