from pydantic import BaseModel, model_validator
from typing import Literal, Optional
import yaml


class LoggingConfig(BaseModel):
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class DataCollectionConfig(BaseModel):
    store_collected_data: bool
    path: Optional[str] = None
    data_format: Optional[Literal["sqlite"]] = None

    @model_validator(mode="after")
    def validate_path_and_data_format(cls, values):
        store_collected_data = values.store_collected_data
        path = values.path
        data_format = values.data_format

        if store_collected_data:
            if not path:
                raise ValueError(
                    "`data_collection.path` is required when `store_collected_data` is True."
                )
            if not data_format:
                raise ValueError(
                    "`data_collection.data_format` is required when `store_collected_data` is True."
                )
            if not path.startswith("s3://"):
                raise ValueError(
                    "`data_collection.path` must start with 's3://' when `store_collected_data` is True."
                )
        return values


class AppConfig(BaseModel):
    logging: LoggingConfig
    data_collection: DataCollectionConfig


def load_config(file_path: str) -> AppConfig:
    with open(file_path, "r") as file:
        config_data = yaml.safe_load(file)
    return AppConfig(**config_data)
