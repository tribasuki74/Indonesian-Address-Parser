import pytest

from Indonesian_Address_Parser import Indonesian_Address_Parser



def test_getByDistrictAndUrban():
    CONSTNUM = 1
    indonesianParser = Indonesian_Address_Parser()
    result = indonesianParser.getKodePos({"district": "Alang-Alang Lebar", "urban": "Srijaya"})
    num = len(list(result))

    # test
    assert CONSTNUM == num

def test_getByUrban():
    CONSTNUM = 4
    indonesianParser = Indonesian_Address_Parser()
    result = indonesianParser.getKodePos({"urban": "Srijaya"})
    num = len(list(result))

    # test
    assert CONSTNUM == num



