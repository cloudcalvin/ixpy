import pytest
from parser_ldf import parser


def test_pasrer():

    value = parser()

    assert value == True


