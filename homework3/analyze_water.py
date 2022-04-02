from ast import Raise
import logging
import math
import json
import sys
from numpy import average


DECAYFAC = 0.02
THRESHOLD = 1.0

def calc_turbidity(water_samples : list, num_samples : int = 5) -> float:
    '''
    Calculates water turbidity using the num_sample average and the equation below:
        T = a0 * I90.
    
        T = Turbidity in NTU Units (0-40)
        a0 = Calibration constant
        I90 = Ninety degree detector current
    Args: 
        water_samples (list): The water sample data from turbidity_data.json.
        num_samples (int): number of samples used for the calculation. Always 5 in this case.
    Returns:
        T (float): Turbidity in NTU
    '''

    recent_turbs = [sample['calibration_constant']*sample['detector_current'] for sample in water_samples]
    
    turb = sum(recent_turbs[-5:])/num_samples #last 5 of set are most recent
    
    return turb
    

def calc_safety_time(currenturb: float) -> float:
    '''
    Calculates the min time for the water to go below the turbidity threshold through the equation:
        Ts > T0(1-d)**b
        therefore  b = log(Ts/T0)/log(1-d)   

        Ts = Turbidity threshold for safe water
        T0 = Current turbidity
        d = decay factor per hour, expressed as a decimal
        b = hours elapsed
    Args:
        T0 (float): Current turbidity
    Returns: 
        b (float): hours elapsed
    '''
    if currenturb < THRESHOLD:
        time = 0.0
    else:
        time = math.log(THRESHOLD/currenturb, (1 - DECAYFAC))
    return time

def main():
    logging.basicConfig(level=logging.INFO)
    
    with open("turbidity_data.json", "r") as f:
        water_samples = json.load(f)

    turb = calc_turbidity(water_samples['turbidity_data'])
    hrs_safe_water = calc_safety_time(turb)

    print(calc_turbidity([], 1))

    print('Average turbidity based on most recent five measurements =', turb, 'NTU')

    if turb >= THRESHOLD:
        logging.warning('Turbidity is above threshold for safe use')
    else:
        logging.info('Turbidity is below threshold for safe use')

    print('Minimum time required to return below a safe threshold =', hrs_safe_water, 'hours')
    

if __name__ == "__main__":
    main()