"""This program will test the functions in the waterflow.py program to ensure they work. 
Additionally, I replaced commonly used numbers in equations with variables.  I added a function
in waterflow.py to convert kPa to psi.  I also wrote a test function to test the kPa_to_psi
function.  I added the converted psi number to the user response for their convenience. """


from pytest import approx
import pytest
from waterflow import water_column_height, pressure_gain_from_water_height, \
    pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction,\
    pressure_loss_from_pipe, kPa_to_psi

def test_water_column_height(): 
    assert water_column_height(0.0, 0.0)== approx(0.0)
    assert water_column_height(0.0, 10.0)== approx(7.5)
    assert water_column_height(25.0, 0.0)== approx(25.0)
    assert water_column_height(48.3, 12.8)== approx(57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.00, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.000) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3)== approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0)== approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2)== approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2)== approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5)== approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

def test_kPa_to_psi():
    assert kPa_to_psi(158.7) == approx(23.017, abs= .001)
    assert kPa_to_psi(1) == approx(0.145, abs=.001)
    assert kPa_to_psi(1000) == approx(145.038, abs=.001)
    assert kPa_to_psi(0.9) == approx(0.131, abs=.001)
    assert kPa_to_psi(-100) == approx(-14.504, abs=.001)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])