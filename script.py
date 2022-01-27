import subprocess
from pathlib import Path
import os
import logging

# setup paths to data
data = Path(os.getenv('DATA_PATH', '/data'))

inputs = data / 'inputs'

outputs = data / 'outputs'

outputs.mkdir(exist_ok=True)

logger = logging.getLogger('tools-zip')
logger.setLevel(logging.INFO)
fh = logging.FileHandler(outputs / 'tools-zip.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

dir_to_zip = os.getenv('ARCHIVE_PATH')

logger.info('Running zip process')

subprocess.call(['zip',
                 '-r', '/data/outputs/data.zip',    # destination
                 dir_to_zip,                       # input
                 ])

logger.info('Zip completed')
