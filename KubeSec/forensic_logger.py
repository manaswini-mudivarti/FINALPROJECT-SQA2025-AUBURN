import logging

def get_logger():
    logger = logging.getLogger("ForensicLogger")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        fh = logging.FileHandler("forensics.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    
    return logger
