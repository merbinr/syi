import os

from pydantic import Field
from pydantic_settings import BaseSettings
from typing_extensions import Literal

class Config(BaseSettings):
    """
    read env variables from environment
    """

    cloud: Literal["aws", "gcp"] = Field(env="CLOUD")


def get_config() -> Config:
    """
    get config
    """
    return Config()
