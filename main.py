import logging
import json
import time
import os

logging.basicConfig(level=logging.INFO, filename='info.log', format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
config = json.load(open('config.json'))

def setup_folder():
    if not os.path.exists('backups'):
        os.makedirs('backups')

def do_backup():
    command = f"bw export --output backups/export-{time.strftime('%Y-%m-%d_%H-%M-%S')}.json --format json --session {config.get('session')}"
    output = os.popen(command).read()
    logging.info(output)

def main():
    setup_folder()
    while True:
        do_backup()
        time.sleep(config.get('interval'))