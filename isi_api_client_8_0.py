import isi_api_client

import isi_sdk_8_0
import urllib3

class IsiApiClient_8_0(isi_sdk_8_0.ApiClient, isi_api_client.IsiApiClient):
    """
    isi_sdk_8_0 compatible version of a multi-thread and multi-client safe
    implementation of the ApiClient. The ApiClient that is generated by Swagger
    Codegen uses a singleton for authentication so it won't work for
    multi-thread or multi-client scenarios where each thread or client needs to
    authenticate with a different Isilon cluster. This version will work
    for that situation.
    """
    def __init__(self, host, verify_ssl):
        # unfortunately there's no way to make the verify_ssl configuration
        # work in a multi-thread/client safe way (at least not with the current
        # Swagger implementation).
        isi_sdk_8_0.configuration.verify_ssl = verify_ssl
        super(IsiApiClient_8_0, self).__init__(host=host)


    def update_params_for_auth(self, headers, querys, auth_settings):
        """
        Overrides the isi_sdk_8_0.ApiClient's version of this function by using
        self._username and self._password for BasicAuth instead of
        isi_sdk.Configuration().username and isi_sdk.Configuration().password.
        """
        headers["Authorization"] = \
                urllib3.util.make_headers(
                        basic_auth=self._username + ":" \
                                + self._password).get("authorization")
