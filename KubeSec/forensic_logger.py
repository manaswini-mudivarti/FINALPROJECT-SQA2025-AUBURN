import logging  # Import Python's built-in logging module for generating logs

# Function to initialize and configure a logger for forensic logging
def get_logger():
    # Create or retrieve a logger named "ForensicLogger"
    logger = logging.getLogger("ForensicLogger")

    # Set the logging level to INFO, meaning it will capture INFO and more severe messages
    logger.setLevel(logging.INFO)

    # Check if the logger already has handlers to avoid duplicate logs
    if not logger.handlers:
        # Create a file handler that logs messages to 'forensics.log'
        fh = logging.FileHandler("forensics.log")

        # Define a log message format including timestamp, log level, and message
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Attach the formatter to the file handler
        fh.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(fh)

    # Return the configured logger for use elsewhere in the code
    return logger
