import shutil

from plbuilder.init import initialize_project
from tests.config import INIT_PROJECT_INPUT_FOLDER


def _generate_init_project():
    shutil.rmtree(INIT_PROJECT_INPUT_FOLDER)
    INIT_PROJECT_INPUT_FOLDER.mkdir()
    initialize_project(INIT_PROJECT_INPUT_FOLDER)


if __name__ == "__main__":
    _generate_init_project()
