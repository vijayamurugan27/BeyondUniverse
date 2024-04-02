import logging

# Configure logging to write to both log.txt and log2.txt files
logging.basicConfig(level=logging.DEBUG, filename='log.txt', filemode='a', format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Create a handler for the second log file
handler = logging.FileHandler('log2.txt')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Log a message using the custom logger
logger.info("This is a custom logger.")
