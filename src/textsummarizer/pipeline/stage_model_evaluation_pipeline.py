from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.model_evaluation import ModelEvalaution
from src.textsummarizer.logging import logger


class ModelEvaluationpipeline:


    def __init__(self):

        pass
    def initiate_model_evaluate(self):

        config = ConfigurationManager()

        model_evaluate_config = config.get_model_evaluation_config()

        model_evaluate = ModelEvalaution(config=model_evaluate_config)

        model_evaluate.evaluate_model()


