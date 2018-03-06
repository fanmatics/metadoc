# -*- coding: utf-8 -*-
import os
import datetime

import unittest
from unittest.mock import patch
from metadoc.domain import Domaintools

class MetadocDomaintoolsTest(unittest.TestCase):

  def setUp(self):
    article_path = "tests/fixtures/theintercept.com/laura-ingraham-lifezette.html"
    self.title = "Some Fake News Publishers Just Happen to Be Donald Trump’s Cronies"
    self.url = "https://theintercept.com/2016/11/26/laura-ingraham-lifezette/"
    self.date_registered = datetime.datetime(2008, 10, 1, 0, 0)
    self.domaintools = Domaintools(url=self.url)

    with open(article_path, 'r') as article:
      self.article_html=article.read()

  def test_init(self):
    assert self.domaintools.url == self.url
    assert self.domaintools.domain == "theintercept.com"

  @patch('metadoc.domain.domaintools.whois_date_registered')
  def test_get_all_local(self, _mocked_func):
    _mocked_func.return_value = self.date_registered
    self.domaintools.get_all()#self.loop)
    assert self.domaintools.date_registered == self.date_registered

    credibility_resp = {
      "is_blacklisted": False,
      "fake_confidence": "0.00"
    }

    assert self.domaintools.credibility == credibility_resp
    assert self.domaintools.date_registered == self.date_registered

  def test_get_all_remote(self):
    self.domaintools.get_all()
    assert self.domaintools.date_registered is not self.date_registered

  def test_new_domain(self):
    today = datetime.datetime.now()
    self.domaintools.date_registered = today
    self.domaintools.check_credibility()
    self.domaintools.recalculate_fake_confidence()

    assert self.domaintools.credibility["fake_confidence"] == 0.2

