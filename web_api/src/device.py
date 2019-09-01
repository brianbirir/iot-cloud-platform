from datetime import datetime
from flask_restful import Resource, reqparse

from src.model import DeviceModel


class Device(Resource):
    @staticmethod
    def get_device_id_parsed_args():
        """Parses device id arg received from the HTTP request.

        Returns:
            A dictionary of the parsed request argument

        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            'device_id',
            type=int,
            help='The ID for the device is missing or wrongly formatted',
            required=True,
            location='args')
        return parser.parse_args()

    @staticmethod
    def get_device_parsed_args():
        """Parses device args received from the HTTP POST request.

        Returns:
            A dictionary of the parsed request argument

        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            'device_name',
            type=str,
            help='The name of the device is missing or wrongly formatted',
            required=True)
        parser.add_argument(
            'device_uuid',
            type=str,
            help='The uuid of the device is missing or wrongly formatted',
            required=True)
        parser.add_argument(
            'project_id',
            type=int,
            help=
            'The id of the associated project is missing or wrongly formatted',
            required=True)
        return parser.parse_args()

    @staticmethod
    def check_existing_device(device_name):
        """Returns query object of an existing project or null"""
        return DeviceModel.query.filter_by(name=device_name).first()

    def get(self):
        """Returns a device's details as HTTP response based on HTTP request

        Returns:
            JSON object: A 200 HTTP status response with details of a device

            JSON object: A 404 HTTP status response for a non-existing device

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status
            and JSON content-type response

        """
        device_id = self.get_device_id_parsed_args()

        try:
            device = DeviceModel.query.filter_by(
                id=device_id['device_id']).first()
            if device:
                response = {"device_id": device.id, "device_name": device.name}
                return response, 200
            else:
                return {"message": "The device does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    def post(self):
        """Registers a new device via POST HTTP request

        Returns:
            JSON object: A 200 HTTP status response with the name of the device

            JSON object: A 400 HTTP status response for an existing device

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and
                JSON content-type response

        """
        device_details = self.get_device_parsed_args()

        try:
            if not self.check_existing_device(device_details['device_name']):
                user = DeviceModel(
                    name=device_details['device_name'],
                    device_uuid=device_details['device_uuid'],
                    project_id=device_details['project_id'])
                user.save_to_db()
                return {
                    "message":
                    "Device {} was created".format(
                        device_details['device_name'])
                }, 200
            else:
                return {"message": "The device already exists"}, 400
        except Exception as e:
            return {"message": str(e)}, 500

    def put(self):
        """Updates details of a device via PUT HTTP request

        Returns:
            JSON object: A 200 HTTP status response with name of the updated device

            JSON object: A 404 HTTP status response for a device that does not exist

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and
            JSON content-type response

        """
        device_id = self.get_device_id_parsed_args()
        device_details = self.get_device_parsed_args()

        try:
            device = DeviceModel.query.filter_by(
                id=device_id['device_id']).first()

            if device:
                device.name = device_details['name']
                device.device_uuid = device_details['device_uuid']
                device.project_id = device_details['project_id']
                device.updated_at = datetime.utcnow()
                device.save_to_db()
                return {
                    "message":
                    "Device {} was updated".format(device_details['name'])
                }, 200
            else:
                return {"message": "The device does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    def delete(self):
        """Deletes a device via DELETE HTTP request

        Returns:
            JSON object: A 200 HTTP status response with confirmation message of the deleted device

            JSON object: A 404 HTTP status response for a device that does not exist

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and
                JSON content-type response

        """
        device_id = self.get_device_id_parsed_args()

        try:
            device = DeviceModel.query.filter_by(
                id=device_id['device_id']).first()

            if device:
                device.delete_from_db()
                return {
                    "message": "The device has been deleted successfully"
                }, 200
            else:
                return {"message": "The device does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
