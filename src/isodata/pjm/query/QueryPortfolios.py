"""QueryPortfolios - This message format is used to query for Portfolios. The query can request all portfolios owned
by the participant or only those portfolios specifically named.

"""
# pylint:disable=duplicate-code
from ...pjm import constants as C
from ...pjm.helper import gen_xml


def prepare(token, **kwargs):
    """prepare and return all the components of the requests call."""

    xml, content_length = gen_xml(with_filters="<All/>", **kwargs)

    return {
        'xml': xml,
        'headers': {
            **C.PJM_BASE_HEADERS,
            'Cookie': 'pjmauth=' + token,
            'Content-length':  content_length
        },
        'url': C.PJM_EMKT_URL_QUERY
    }
