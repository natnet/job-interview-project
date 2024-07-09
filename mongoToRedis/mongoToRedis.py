import time
import logging
from redisService import RedisService

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    redisService = RedisService()

    try:
        while True:
            redisService.process_events()
            time.sleep(30)
    except KeyboardInterrupt:
        logger.info("Shutting down gracefully...")

if __name__ == '__main__':
    main()