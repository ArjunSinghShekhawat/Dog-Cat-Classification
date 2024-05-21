import logging
import os
from datetime import datetime

LOG_PATH = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_PATH)
os.makedirs(log_path,exist_ok=True)

LOG_FILE = os.path.join(log_path,LOG_PATH)

logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format='[%(asctime)s: %(levelname)s: %(module)s: %(message)s]')
