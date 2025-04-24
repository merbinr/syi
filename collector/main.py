import os
from src.config import get_config


def main():
    config = get_config()
    if config.cloud == "aws":
        pass
    elif config.cloud == "gcp":
        pass



if __name__ == "__main__":
    main()
