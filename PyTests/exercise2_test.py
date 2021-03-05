import math
import pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless).
    """
    if carbon_14_ratio > 1 or carbon_14_ratio <= 0:
        return None
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 

def test_get_age_carbon_14_dating():
    assert math.isclose(get_age_carbon_14_dating(0.35, 8680.34, abs_tol=0.01))
    assert get_age_carbon_14_dating(0) == None
    assert get_age_carbon_14_dating(5) == None
    assert get_age_carbon_14_dating(75.42) == None
    assert get_age_carbon_14_dating(-29.1) == None
    assert get_age_carbon_14_dating(-1.5) == None
    assert get_age_carbon_14_dating(-3.45) == None
    assert get_age_carbon_14_dating(4) == None

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.

print(get_age_carbon_14_dating(0.35))