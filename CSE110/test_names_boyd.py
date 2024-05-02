from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Boyd", "Poblete") == "Poblete; Boyd" 
    assert make_full_name("Sheena", "Ignacio") == "Ignacio; Sheena" 
    assert make_full_name("Jim", "Poblete") == "Poblete; Jim"
    assert make_full_name("", "") == "; "



def test_extract_family_name():
    assert extract_family_name("Poblete; Boyd") == "Poblete"
    assert extract_family_name("Ignacio; Sheena" ) == "Ignacio"
    assert extract_family_name("Poblete; Jim" ) == "Poblete"
    assert make_full_name("", "") == "; "

def test_extract_given_name():
    assert extract_given_name("Poblete; Boyd") == "Boyd"
    assert extract_given_name("Ignacio; Sheena") == "Sheena"
    assert make_full_name("", "") == "; "


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
    