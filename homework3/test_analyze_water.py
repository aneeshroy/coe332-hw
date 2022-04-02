import pytest 
import math
from analyze_water import calc_turbidity, calc_safety_time

def test_calc_turbidity():
    assert type(calc_turbidity([{
     "datetime": "2022-02-01 00:00",
     "sample_volume": 1.19,
     "calibration_constant": 1.022,
     "detector_current": 1.137,
    }], 1)) == float

    assert calc_turbidity([{
     "datetime": "2022-02-01 00:00",
     "sample_volume": 1.19,
     "calibration_constant": 1.022,
     "detector_current": 1.137,
    }], 1) == 1.137 * 1.022

    with pytest.raises(KeyError):
        calc_turbidity([{
     "datetime": "2022-02-01 00:00",
     "sample_volume": 1.5,
     "calibration_constant": 1.09,
     "analyzed_by": "C. Milligan"
    }], 1) # no detector current

    with pytest.raises(ZeroDivisionError):
        calc_turbidity([], 1) 



def test_calc_safety_time():

    assert type(calc_safety_time(.8)) == float
    assert type(calc_safety_time(2)) == float
    assert calc_safety_time(.8) == 0
    assert calc_safety_time(2) == math.log(1/2)/math.log(.98)

    with pytest.raises(TypeError):
        calc_safety_time('error')