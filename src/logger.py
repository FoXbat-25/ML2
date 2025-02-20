import logging
from datetime import datetime
import os

log_file=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_file_dir=os.path.join(os.getcwd(), 'logs')
os.makedirs(log_file_dir, exist_ok=True)
log_file_path=os.path.join(log_file_dir, log_file)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger(__name__)