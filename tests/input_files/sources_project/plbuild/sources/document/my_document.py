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


TITLE = "My Document"
ORDER = None


def get_content() -> PyexlatexItems:
    return [

    ]

OUTPUT_NAME = TITLE

OUTPUT_LOCATION = paths.DOCUMENTS_BUILD_PATH

def get_outputs() -> List[BuildConfig]:
    document = pl.Document(get_content(), title=TITLE, authors=AUTHORS)
    options = BuildOptions(output_folder=OUTPUT_LOCATION, file_name=OUTPUT_NAME)
    return [BuildConfig(model=document, options=options)]