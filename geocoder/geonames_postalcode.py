from __future__ import absolute_import

from geocoder.geonames import GeonamesQuery, GeonamesResult

class GeonamesPostalCodeResult(GeonamesResult):

    @property
    def place_name(self):
        return self.raw.get('placeName', "")



class GeonamesPostalCode(GeonamesQuery):
    """ PostalCode:
        http://api.geonames.org/postalCodeLookupJSON?postalcode=6600&country=AT&username=demo
    """

    provider = 'geonames'
    method = 'postalcode'
    _RESULT_CLASS = GeonamesPostalCodeResult

    _URL = 'http://api.geonames.org/postalCodeLookupJSON'

    def _build_params(self, location, provider_key, **kwargs):
        """Will be overridden according to the targetted web service"""
        return {
            'postalcode': location,
            'country': kwargs.get('country'),
            'username': provider_key,
        }

    def _adapt_results(self, json_response):
        # extract the array of JSON objects
        return json_response['postalcodes']
