import filecmp
import shutil

from plbuilder.init import initialize_project
from tests.config import GENERATED_INIT_PROJECT_FOLDER, INIT_PROJECT_INPUT_FOLDER
from tests.dirutils import are_dir_trees_equal


def _reset_generated_init_project():
    if GENERATED_INIT_PROJECT_FOLDER.exists():
        shutil.rmtree(GENERATED_INIT_PROJECT_FOLDER)
    GENERATED_INIT_PROJECT_FOLDER.mkdir()


def test_init_project_when_empty():
    _reset_generated_init_project()
    initialize_project(GENERATED_INIT_PROJECT_FOLDER)
    assert are_dir_trees_equal(GENERATED_INIT_PROJECT_FOLDER, INIT_PROJECT_INPUT_FOLDER)
