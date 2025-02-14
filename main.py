from src.textsummarizer.logging import logger

from src.textsummarizer.pipeline.stage_data_ingestion_pipeline import DataIngestionpipeline

logger.info("logging is implemented")


STAGE_NAME = "Data Ingestion Stage"

try:

    logger.info("stage {STAGE_NAME} initiated")

    data_ingestion_pipeline = DataIngestionpipeline()

    data_ingestion_pipeline.initiate_data_ingestion()

    logger.info("stage {STAGE_NAME} completed")

except Exception as e:

    logger.exception(e)

    raise e
