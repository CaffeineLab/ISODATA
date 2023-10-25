"""QueryUnitRampRates -You may query for a submitted hourly ramp rate using the message described below.
To query for submitted Unit Ramp Rate Hourly data the following QueryRequest is issued:

<QueryRequest>
 <QueryUnitRampRates day="YYYY-MM-DD">
  <All/>
 <LocationName>zzz</LocationName>
 </QueryFuelPriceExceptions>
</QueryRequest>

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
