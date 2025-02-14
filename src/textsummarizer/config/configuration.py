from src.textsummarizer.constant import *
from src.textsummarizer.utils.common import read_yaml, create_directories
from src.textsummarizer.entity import DataIngestionConfig

#  this goes into the configuration file under config folder
class ConfigurationManager:
    def __init__( self,config_filepath = CONFIG_PATH, params_filepath = PARAMS_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

            config = self.config.data_ingestion

            # creating root directory for config.root_dir

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(

                root_dir = config.root_dir,
                source_url = config.source_url,
                local_data_file = config.local_data_file,
                unzip_dir = config.unzip_dir

            )


            return data_ingestion_config
