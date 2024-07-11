import time
import logging
from redisService import RedisService
import yaml

def main():

    with open('/config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
        num_of_sec_sleep = config['time']['num_of_sec_sleep']

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    redisService = RedisService()

    try:
        while True:
            redisService.process_events()
            time.sleep(num_of_sec_sleep)
    except KeyboardInterrupt:
        logger.info("Shutting down gracefully...")

if __name__ == '__main__':
    main()