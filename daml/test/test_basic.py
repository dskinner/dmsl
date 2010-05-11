# -*- coding: utf-8 -*-
import os.path
import unittest
from _parse import parse

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.t = {
            'basic_indent': None,
            'basic_variable_indent': None,
            'tag_hashes': None,
            'multiline_text': None,}

        for k, v in self.t.items():
            # template file
            a = open(os.path.join('', k+'.daml')).readlines()
            # expected output
            b = open(os.path.join('', k+'.html')).read()
            self.t[k] = (a, b)

    def test_basic_indent(self):
        parsed, expected = self.t['basic_indent']
        parsed = parse(parsed)
        self.assertEqual(parsed.strip(), expected.strip())

    def test_basic_variable_indent(self):
        parsed, expected = self.t['basic_variable_indent']
        parsed = parse(parsed)
        self.assertEqual(parsed.strip(), expected.strip())

    def test_tag_hashes(self):
        parsed, expected = self.t['tag_hashes']
        parsed = parse(parsed)
        self.assertEqual(parsed.strip(), expected.strip())

    def test_multiline_text(self):
        parsed, expected = self.t['multiline_text']
        parsed = parse(parsed)
        self.assertEqual(parsed.strip(), expected.strip())
