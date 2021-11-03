import os

from plbuilder.builder import create_presentation_template, create_document_template
from tests.config import INIT_PROJECT_INPUT_FOLDER, SOURCES_PROJECT_INPUT_FOLDER
from tests.projutils import regenerate_project


def _generate_init_project():
    regenerate_project(INIT_PROJECT_INPUT_FOLDER)


def _generate_project_with_sources():
    regenerate_project(SOURCES_PROJECT_INPUT_FOLDER)
    os.chdir(SOURCES_PROJECT_INPUT_FOLDER)
    _generate_presentation()
    _generate_document()


def _generate_presentation():
    create_presentation_template("mypres")


def _generate_document():
    create_document_template("mydoc")


if __name__ == "__main__":
    _generate_init_project()
    _generate_project_with_sources()
