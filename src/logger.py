import logging
import os
from datetime import datetime
import sys

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")  # Create a 'logs' directory in the current working directory
os.makedirs(logs_path, exist_ok=True)  # Create the directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Set the default logging level to INFO
)

if __name__ == "__main__":
    logging.info("Logging started from logger.py")
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        logging.error(f"Division by zero: {e}")
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno
        logging.error(f"Error occurred in file: {file_name} at line: {line_no}")

    logging.info("Logging finished.")