import logging
from datetime import datetime

# Cấu hình logging
logging.basicConfig(filename='service-logging/logging.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logging.info('info')
