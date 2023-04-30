from pathlib import Path


def get_base_directory():
    # path = Path('data/files/voices').mkdir(parents=True, exist_ok=True)
    path = Path('data/files/voices')

    return Path(__file__).absolute().parent.parent
