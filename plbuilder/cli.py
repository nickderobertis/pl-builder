from typing import Optional
import fire
import shutil
import os

from pyexlatex.logic.output.api.formats import OutputFormats

from plbuilder.config import CREATED_DIRECTORY

from plbuilder.builder import (
    build_all,
    build_by_file_path,
    create_presentation_template,
    create_document_template
)
from plbuilder.autoreloader import autobuild
from plbuilder.init import initialize_project


def build(file_path: Optional[str] = None, output_format: Optional[OutputFormats] = None):
    """
    Create slides and handout PDFs from plbuilder pyexlatex templates.
    Passing no arguments will build all templates.

    :param file_path: path of template from which to build PDFs
    :param output_format: the file type of the output, currently 'pdf' and 'html' are supported.
        If not passed, will fall back to the setting of DEFAULT_OUTPUT_FORMAT in the file. If that
        is not passed, will default to 'pdf'
    :return: None
    """
    if file_path is None:
        build_all(desired_output_format=output_format)
    else:
        build_by_file_path(file_path, desired_output_format=output_format)


def create(doc_type: str, name: str):
    """
    Creates a slide template using the passed name

    :param doc_type: 'presentation' or 'document'
    :param name: Display name, will be standardized to snakecase and lowercase for use in the file name
    :return:
    """
    doc_type = doc_type.lower().strip()
    if doc_type == 'presentation':
        create_presentation_template(name)
    elif doc_type == 'document':
        create_document_template(name)
    else:
        raise ValueError(f'must pass document or presentation as first argument, got {doc_type}')


def init():
    """
    Creates a plbuilder project in the current directory


    :return:
    """
    initialize_project()




def main():
    return fire.Fire({
        'build': build,
        'create': create,
        'init': init,
        'autobuild': autobuild
    })

if __name__ == '__main__':
    main()
