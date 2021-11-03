import os

import pytest

from plbuilder.builder import create_presentation_template, create_document_template
from tests.config import (
    GENERATED_PROJECT_FOLDER,
    INPUT_PRESENTATION_FOLDER,
    GENERATED_PRESENTATION_FOLDER,
    INPUT_DOCUMENT_FOLDER,
    GENERATED_DOCUMENT_FOLDER,
)
from tests.dirutils import are_dir_trees_equal
from tests.projutils import regenerate_generated_init_project


@pytest.fixture(autouse=True)
def before_each():
    regenerate_generated_init_project()
    os.chdir(GENERATED_PROJECT_FOLDER)
    yield


def test_create_presentation():
    create_presentation_template("mypres")
    assert are_dir_trees_equal(INPUT_PRESENTATION_FOLDER, GENERATED_PRESENTATION_FOLDER)


def test_create_document():
    create_document_template("mydoc")
    assert are_dir_trees_equal(INPUT_DOCUMENT_FOLDER, GENERATED_DOCUMENT_FOLDER)
