import os
import sys
import logging


#cutsom logging
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


#creating a directory for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True) #ensures that the directory is created if it doesn't exists


#final log
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #write logs to the file
        logging.StreamHandler(sys.stdout) #print the log in the terminal
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
