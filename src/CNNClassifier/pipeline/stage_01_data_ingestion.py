from CNNClassifier.components.stage01_data_ingestion import DataIngestion
from CNNClassifier.config import configurationManager
from CNNClassifier import logger

logger.info(f"Data Ingestion Stage01 started")
config = ConfigurationManager()
data_ingestion_config=config.get_data_ingestion_config()
data_ingestion = DataIngestion()

data_ingestion.download_file()
data_ingestion.unzip_and_clean()

logger.info(f"Data Ingestion Stage01 completed")
