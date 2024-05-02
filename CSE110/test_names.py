from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full_name():
   
    assert make_full_name("Owen", "Morales") == "Morales; Owen"
    assert make_full_name("Paola", "Morales") == "Morales; Paola"
    assert make_full_name("Alex", "Morales") == "Morales; Alex"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
   
    assert extract_family_name("Morales; Owen") == "Morales"
    assert extract_family_name("Morales; Paola") == "Morales"
    assert extract_family_name("Morales; Alex") == "Morales"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
   
    assert extract_given_name("Morales; Owen") == "Owen"
    assert extract_given_name("Morales; Paola") == "Paola"
    assert extract_given_name("Morales; Alex") == "Alex"
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])