from src.textsummarizer.logging import logger

from src.textsummarizer.pipeline.stage_data_ingestion_pipeline import DataIngestionpipeline
from src.textsummarizer.pipeline.stage_data_processing_pipeline import DataTransformationpipeline
from src.textsummarizer.pipeline.stage_model_trainer_pipeline import ModelTrainerpipeline

from src.textsummarizer.pipeline.stage_model_evaluation_pipeline import ModelEvaluationpipeline

logger.info("logging is implemented")


STAGE_NAME = "Data Ingestion Stage"

try:

    logger.info("stage { STAGE_NAME } initiated")

    data_ingestion_pipeline = DataIngestionpipeline()

    data_ingestion_pipeline.initiate_data_ingestion()

    logger.info("stage { STAGE_NAME } completed")

except Exception as e:

    logger.exception(e)

    raise e

STAGE_NAME = "Data Transformation Stage"

try:

    logger.info("stage {STAGE_NAME} initiated")

    data_processing_pipeline = DataTransformationpipeline()

    data_processing_pipeline.initiate_data_transformation()

    logger.info("stage {STAGE_NAME} completed")

except Exception as e:

    logger.exception(e)

    raise e


STAGE_NAME = "Model Trainer Stage"

try:

    logger.info("stage { STAGE_NAME } initiated")

    data_processing_pipeline = ModelTrainerpipeline()

    # data_processing_pipeline.initiate_model_trainer()

    logger.info("stage { STAGE_NAME } completed")

except Exception as e:

    logger.exception(e)

    raise e

STAGE_NAME = "Model Evaluation Stage"


try:

    logger.info("stage { STAGE_NAME } initiated")

    model_evalaution_pipeline = ModelEvaluationpipeline()

    model_evalaution_pipeline.initiate_model_evaluate()

    logger.info("stage { STAGE_NAME } completed")

except Exception as e:

    logger.exception(e)

    raise e
