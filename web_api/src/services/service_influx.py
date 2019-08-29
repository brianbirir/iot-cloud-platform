"""Middleware that interacts with InfluxDB database

- Checks if requested database exists
- Retrieves data points from database based on criteria
"""
from influxdb import InfluxDBClient, exceptions

from src.utils import logger as app_logger
from config import Config


class QueryBuilder:
    """Builds query statement for the query function"""

    def __init__(self, measurement="", period="time >= '2019-01-01'",
                 limit=25):
        self._limit = limit
        self._measurement = measurement
        self._period = period

    def _select_clause(self):
        return "select * from {0}".format(self._measurement)

    def _where_clause(self):
        return " where {0}".format(self._period)

    def _limit_clause(self):
        return " limit {0}".format(self._limit)

    def generate_query(self):
        return self._select_clause() + self._where_clause(
        ) + self._limit_clause()


class InfluxService:
    """Provides an interface for connecting to InfluxDB"""
    cnf = Config()
    qb = QueryBuilder()
    db_client = InfluxDBClient(
        host=cnf.INFLUX_HOST,
        port=cnf.INFLUX_PORT,
        username=cnf.INFLUX_USER,
        password=cnf.INFLUX_PASSWORD)

    def __init__(self):
        self._measurement = InfluxService.cnf.INFLUX_DB_MEASUREMENT

    @staticmethod
    def check_db():
        """Check if database exists"""
        # get all databases
        all_dbs_list = InfluxService.db_client.get_list_database()

        # check if current database exists and if return warning message
        if InfluxService.cnf.INFLUX_DB not in [
                str(x['name']) for x in all_dbs_list
        ]:
            try:
                app_logger.warning("Database {0} does not exist".format(
                    InfluxService.cnf.INFLUX_DB))
            except exceptions.InfluxDBClientError as e:
                app_logger.error(str(e))
            except exceptions.InfluxDBServerError as e1:
                app_logger.error(str(e1))
        else:
            try:
                app_logger.info("Using db {0}".format(
                    InfluxService.cnf.INFLUX_DB))
                InfluxService.db_client.switch_database(
                    InfluxService.cnf.INFLUX_DB)
            except exceptions.InfluxDBClientError as e:
                app_logger.error(str(e))
            except exceptions.InfluxDBServerError as e1:
                app_logger.error(str(e1))

    @staticmethod
    def ping_db():
        """Check if db service is running"""
        return InfluxService.db_client.ping()

    def query_data(self):
        """Retrieve data points from database"""
        try:
            self.check_db()
            qr = QueryBuilder(measurement=self._measurement)
            rs = InfluxService.db_client.query(query=qr.generate_query())
            return list(rs.get_points())
        except Exception as e:
            app_logger.error(str(e))


if __name__ == "__main__":
    influx_service = InfluxService()
    print(influx_service.query_data())
