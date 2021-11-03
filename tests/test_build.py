import os

import pytest

from plbuilder.builder import (
    create_presentation_template,
    create_document_template,
    build_all,
)
from tests.config import (
    GENERATED_PROJECT_FOLDER,
    INPUT_DOCUMENTS_FOLDER,
    GENERATED_DOCUMENTS_FOLDER,
    INPUT_SLIDES_FOLDER,
    GENERATED_SLIDES_FOLDER,
    GENERATED_HANDOUTS_FOLDER,
    INPUT_HANDOUTS_FOLDER,
)
from tests.fileutils import are_files_equal
from tests.projutils import regenerate_generated_init_project


@pytest.fixture(autouse=True)
def before_each():
    regenerate_generated_init_project()
    os.chdir(GENERATED_PROJECT_FOLDER)
    create_presentation_template("mypres")
    create_document_template("mydoc")
    yield


def test_build():
    build_all()
    assert are_files_equal(
        INPUT_DOCUMENTS_FOLDER / ".tex", GENERATED_DOCUMENTS_FOLDER / ".tex"
    )
    assert are_files_equal(
        INPUT_SLIDES_FOLDER / ".tex", GENERATED_SLIDES_FOLDER / ".tex"
    )
    assert are_files_equal(
        INPUT_HANDOUTS_FOLDER / ".tex", GENERATED_HANDOUTS_FOLDER / ".tex"
    )
