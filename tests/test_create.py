import os

import pytest

from plbuilder.creator import create_template
from tests.config import (
    GENERATED_PROJECT_FOLDER,
    INPUT_PRESENTATION_SOURCES_FOLDER,
    GENERATED_PRESENTATION_SOURCES_FOLDER,
    INPUT_DOCUMENT_SOURCES_FOLDER,
    GENERATED_DOCUMENT_SOURCES_FOLDER,
)
from tests.dirutils import are_dir_trees_equal
from tests.projutils import regenerate_generated_init_project


@pytest.fixture(autouse=True)
def before_each():
    regenerate_generated_init_project()
    os.chdir(GENERATED_PROJECT_FOLDER)
    yield


def test_create_presentation():
    create_template("presentation", "My Presentation")
    assert are_dir_trees_equal(
        INPUT_PRESENTATION_SOURCES_FOLDER, GENERATED_PRESENTATION_SOURCES_FOLDER
    )


def test_create_document():
    create_template("document", "My Document")
    assert are_dir_trees_equal(
        INPUT_DOCUMENT_SOURCES_FOLDER, GENERATED_DOCUMENT_SOURCES_FOLDER
    )


# TODO: add tests for overriding templates, custom templates