# application entry point
from src.broker import connect_to_broker


if __name__ == '__main__':
	# run mqtt subscriber client
	connect_to_broker()
