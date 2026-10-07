import logging
import logging.config

from config.setting import ROOT_PATH

CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {
            "class": "logging.Formatter",
            "format": "[%(asctime)s] #%(levelname)-9s %(module)s:%(lineno)-3d - MESSAGE: %(message)s",
            "datefmt": "%Y-%m-%d - %H:%M:%S"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "custom",
            "stream": "ext://sys.stdout"
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "custom",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "custom",
            "filename": f"{ROOT_PATH}/logs/info.log",
            "encoding": "utf8",
            "maxBytes": 1048575,
            "backupCount": 3
        }
    },
    "loggers": {
        "tests": {
            "level": "DEBUG",
            "propagate": False,
            "handlers": [
                "stderr",
                "file"
            ]
        }
    },
    "root": {
        "level": "WARNING",
        "propagate": False,
        "handlers": [
            "stderr",
            "stdout",
            "file"
        ]
    }
}

logging.config.dictConfig(CONFIG)


def get_logger(name: str):
    return logging.getLogger(name)
