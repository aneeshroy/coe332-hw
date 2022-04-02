import pytest
import json
from ml_data_analysis import *

def test_count_classes():
    with open('Meteorite_Landings.json', 'r') as f:
        ml_data = json.load(f)
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), str) == False
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), dict) == True
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), int) == False 


def test_compute_average_mass():

    with open('Meteorite_Landings.json', 'r') as f:
        ml_data = json.load(f)

    assert isinstance(compute_average_mass(ml_data['meteorite_landings'],'mass (g)'), float) == True
    assert isinstance(compute_average_mass(ml_data['meteorite_landings'],'mass (g)'), list) != True
    assert isinstance(compute_average_mass(ml_data['meteorite_landings'],'mass (g)'), list) == False
    assert(compute_average_mass(ml_data['meteorite_landings'],'mass (g)') != 0)
    assert(compute_average_mass(ml_data['meteorite_landings'],'mass (g)') > 0)



def test_check_hemisphere():

    assert ((check_hemisphere(1,1)) == 'Northern & Eastern')
    assert ((check_hemisphere(-1,1)) == 'Southern & Eastern')
    assert ((check_hemisphere(1,-1)) == 'Northern & Western')



def pytest():

    test_count_classes()
    test_compute_average_mass()
    test_check_hemisphere()
    

if __name__ == '__pytest__':
    pytest()