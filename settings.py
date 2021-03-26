from dotenv import load_dotenv, dotenv_values

load_dotenv()


def get_parameter_by_key(key: str) -> str:
    return dotenv_values()[key]


def get_all_parameters() -> dict:
    return dotenv_values
