import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from plbuilder import paths
from plbuilder.paths import images_path


AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = ''
SUBTITLE = ''

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = paths.HANDOUTS_BUILD_PATH
TITLE = ''
ORDER = None


def get_content():
    return [

    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

