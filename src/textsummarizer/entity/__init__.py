from dataclasses import dataclass
from pathlib import Path

# types of data to be ingested
@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_url : Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    tokenizer_name : Path

@dataclass
class ModelTrainerConfig:

    root_dir : Path
    data_path : Path
    model_name : Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
