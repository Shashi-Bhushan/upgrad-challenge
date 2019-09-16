#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Shashi Bhushan <sbhushan1@outlook.com>

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from util.customlogger import log_error


class RequestHandler:
    def __init__(self, url):
        self.url = url

        self.response_content = self.get_response()

    def get_response(self):
        """
           Attempts to get the content at `url` by making an HTTP GET request.
           If the content-type of response is some kind of HTML/XML, return the content as BS object, otherwise return None.
       """
        try:
            with closing(get(self.url, stream=True)) as response:
                if self.is_valid_response(response):
                    return BeautifulSoup(response.content, 'html.parser')
                else:
                    log_error('Invalid response during requests to {0}'.format(self.url))
                    return None
        except RequestException as cause:
            log_error('Error during requests to {0} : {1}'.format(self.url, str(cause)))
            return None

    @staticmethod
    def is_valid_response(response):
        """
            Returns True if the response is HTML and has status 200, False otherwise.
        """
        content_type = response.headers['Content-Type'].lower()

        return response.status_code == 200 and content_type is not None and content_type.find('html') > -1
