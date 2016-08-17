#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from graphite_escaping import metrics_name_to_graphite, metrics_name_from_graphite


@pytest.mark.parametrize("name", [
    'abc_edf',
    'abc @edf#',
    'abc.@edf#',
    'abc_ @ e_df#',
    'a.b.c_ @ e_df#',
    'a.b.___c d _feg',
    '_ . .fda',
    '_.',
    '汉 字.汉*字'
])
def test_consistency(name):
	assert metrics_name_from_graphite(metrics_name_to_graphite(name)) == name