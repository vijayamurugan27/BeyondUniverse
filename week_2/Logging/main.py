import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

def sort_characters(input_str):
    if not isinstance(input_str, str):
        logger.error('Input is not a valid string.')
        return None
    
    if not input_str:
        logger.warning('Input string is empty.')
        return input_str
    
    sorted_str = ''.join(sorted(input_str))
    logger.info(f'Sorted characters: {sorted_str}')
    return sorted_str

def main():
    logger.debug('Starting the program')
    
    # Simulate DEBUG level message
    logger.debug('This is a debug message')
    
    # Simulate INFO level message
    logger.info('This is an info message')
    
    # Simulate WARNING level message
    logger.warning('This is a warning message')
    
    # Simulate ERROR level message
    logger.error('This is an error message')
    
    # Simulate CRITICAL level message
    logger.critical('This is a critical message')
    
    # Simulate INFO level message with sorting characters
    input_str = input('Enter a string to sort characters: ')
    sorted_str = sort_characters(input_str)

    if sorted_str is not None:
        logger.info(f'Sorted string: {sorted_str}')

    logger.debug('End of the program')

if __name__ == "__main__":
    main()
