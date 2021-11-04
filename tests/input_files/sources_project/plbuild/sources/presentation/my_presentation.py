from typing import List, Dict, Any

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from pyexlatex.typing import PyexlatexItems

from plbuilder import paths
from plbuilder.paths import images_path
from plbuilder.builder import BuildConfig, BuildOptions

AUTHORS = ['']
SHORT_AUTHOR = ''


TITLE = "My Presentation"
ORDER = None


def get_content() -> PyexlatexItems:
    return [

    ]

OUTPUT_NAME = TITLE

SHORT_TITLE = ''
SUBTITLE = ''

INSTITUTIONS = [
    ['Some Institution', 'Some Department'],
]
SHORT_INSTITUTION = 'Inst'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = paths.HANDOUTS_BUILD_PATH

def _get_common_kwargs() -> Dict[str, Any]:
    return dict(title=TITLE, authors=AUTHORS)


def _get_slides() -> lp.Presentation:
    return lp.Presentation(get_content(), **_get_common_kwargs())


def _get_handouts() -> lp.Presentation:
    return lp.Presentation(get_content(), **_get_common_kwargs(), handouts=True)


def get_outputs() -> List[BuildConfig]:
    slides_options = BuildOptions(output_folder=OUTPUT_LOCATION, file_name=OUTPUT_NAME)
    handouts_options = BuildOptions(
        output_folder=HANDOUTS_OUTPUT_LOCATION, file_name=OUTPUT_NAME
    )
    return [
        BuildConfig(model=_get_slides(), options=slides_options),
        BuildConfig(model=_get_handouts(), options=handouts_options),
    ]