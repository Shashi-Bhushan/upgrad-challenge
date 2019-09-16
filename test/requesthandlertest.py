#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Shashi Bhushan <sbhushan1@outlook.com>

from unittest import TestCase

from util import RequestHandler


class TestRequestHandler(TestCase):
    def setUp(self):
        url = 'https://www.prokabaddi.com/teams/bengaluru-bulls-profile-1'

        self.request_handler = RequestHandler(url)

    def test_response_valid(self):
        self.assertIsNotNone(self.request_handler.response_content)
