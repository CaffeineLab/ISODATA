"""QueryAllScheduleRestriction - To request all schedule restriction associated with a unit location or the locations of a portfolio,
execute the following query request.
<QueryRequest>
 <QueryAllScheduleRestriction day="yyyy-mm-dd" available="xxx" >
 <All/>
 <LocationName>xxx</LocationName>
 <PortfolioName>xxx</PortfolioName>
 </QueryAllScheduleRestriction>
</QueryRequest>
"""
# pylint:disable=duplicate-code
from ...pjm import constants as C
from ...pjm.helper import gen_xml


def prepare(token, **kwargs):
    """prepare and return all the components of the requests call."""

    xml, content_length = gen_xml(with_filters='<All/>', **kwargs)

    return {
        'xml': xml,
        'headers': {
            **C.PJM_BASE_HEADERS,
            'Cookie': 'pjmauth=' + token,
            'Content-length':  content_length
        },
        'url': C.PJM_EMKT_URL_QUERY
    }
