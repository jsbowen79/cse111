"""This program will test all functions from the names.py and address.py programs."""

#Import modules 
from names import make_full_name, extract_family_name, extract_given_name
from address import extract_state, extract_city, extract_zipcode  
import pytest

# Test the names.py functions.

def test_make_full_name(): 
    #Tests the make_full_name function with a variety of names. 
    assert make_full_name("Al", "Roe") == "Roe; Al"
    assert make_full_name("Josephina", "Perslonocalovich") == "Perslonocalovich; Josephina"
    assert make_full_name("John-Paul", "Williamson") == "Williamson; John-Paul"
    assert make_full_name("Mary", "Web-Foster") == "Web-Foster; Mary"
    assert make_full_name("Mary-Ann", "Web-Foster") == "Web-Foster; Mary-Ann"

def test_extract_family_name():
    #Tests the extract_family_name function with a variety of names. 
    assert extract_family_name( "Roe; Al",) == "Roe"
    assert extract_family_name("Perslonocalovich; Josephina") == "Perslonocalovich"
    assert extract_family_name("Williamson; John-Paul") == "Williamson"
    assert extract_family_name("Web-Foster; Mary") == "Web-Foster"
    assert extract_family_name("Web-Foster; Mary-Ann") == "Web-Foster"

def test_extract_given_name():
    #Tests the extract_given_name function with a variety of names. 
    assert extract_given_name( "Roe; Al",) == "Al"
    assert extract_given_name("Perslonocalovich; Josephina") == "Josephina"
    assert extract_given_name("Williamson; John-Paul") == "John-Paul"
    assert extract_given_name("Web-Foster; Mary") == "Mary"
    assert extract_given_name("Web-Foster; Mary-Ann") == "Mary-Ann"

# Test the address.py functions. 

def test_extract_city():
    # Tests the extract_city function to ensure the city is extracted.
    assert extract_city("11767 Idalia Street, Commerce City, Colorado 80022") == "Commerce City" 
    assert extract_city("11767 Idalia Street, Commerce City, Colorado 80022-12568") == "Commerce City"
    assert extract_city("11767 Idalia Rose Blvd W, Commerce City, Colorado 80022") == "Commerce City"
    assert extract_city("11767 Idalia Street, Commerce, Colorado 80022") == "Commerce"
    assert extract_city("11767 Idalia Street, 4Long Island City, Colorado 80022") == "4Long Island City"

def test_extract_state():
    assert extract_state("11767 Idalia Street, Commerce City, NH 80022") == "NH" 
    assert extract_state("11767 Idalia Street, Commerce City, NM 80022-12568") == "NM"
    assert extract_state("11767 Idalia Rose Blvd W, Commerce City, CO 80022") == "CO"
    assert extract_state("11767 Idalia Street, Commerce, CO 80022") == "CO"
    assert extract_state("11767 Idalia Street, Long Island City, 3C 80022") == "3C"

def test_extract_zipcode():
    assert extract_zipcode("11767 Idalia Street, New Hampsire, Colorado 80022") == "80022" 
    assert extract_zipcode("11767 Idalia Street, Commerce,  New Hampshire 80022-12568") == "80022-12568"
    assert extract_zipcode("11767 Idalia Rose Blvd W, Commerce, Colorado 80022") == "80022"
    assert extract_zipcode("11767 Idalia Street, Commerce, Colorado 95121") == "95121"
    assert extract_zipcode("11767 Idalia, Long Island City, Colorado a80022") == "a80022"

pytest.main(["-v", "--tb=line", "-rN", __file__])