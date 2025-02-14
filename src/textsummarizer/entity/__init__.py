from dataclasses import dataclass
from pathlib import Path

# types of data to be ingested
@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_url : Path
    local_data_file: Path
    unzip_dir: Path