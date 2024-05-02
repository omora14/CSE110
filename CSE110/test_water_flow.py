import pytest
import water_flow

def test_water_column_height():
    assert round(water_flow.water_column_height(20, 10), 2) == 27.5
    assert round(water_flow.water_column_height(30, 5), 2) ==33.75
    assert round(water_flow.water_column_height(15, 20), 2) == 30.0

def test_pressure_gain_from_water_height():
    assert round(water_flow.pressure_gain_from_water_height(10), 2) == 97.89
    assert round(water_flow.pressure_gain_from_water_height(20), 2) == 195.78
    assert round(water_flow.pressure_gain_from_water_height(30), 2) == 293.67

def test_pressure_loss_from_pipe():
    assert round(water_flow.pressure_loss_from_pipe(0.1, 10, 0.05, 1.002e-6), 2) == 22668.97
    assert round(water_flow.pressure_loss_from_pipe(0.2, 20, 0.1, 1.002e-6), 2) == 5667.24
    assert round(water_flow.pressure_loss_from_pipe(0.3, 30, 0.15, 1.002e-6), 2) == 2518.77

def test_pressure_loss_from_fittings():
    assert round(water_flow.pressure_loss_from_fittings(2, 0.1, 0.05), 2) == 20.26
    assert round(water_flow.pressure_loss_from_fittings(4, 0.2, 0.1), 2) == 10.13
    assert round(water_flow.pressure_loss_from_fittings(6, 0.3, 0.15), 2) == 6.75

def test_reynolds_number():
    assert round(water_flow.reynolds_number(0.1, 0.05, 1.002e-6), 2) == 635349.61
    assert round(water_flow.reynolds_number(0.2, 0.1, 1.002e-6), 2) == 635349.61
    assert round(water_flow.reynolds_number(0.3, 0.15, 1.002e-6), 2) == 635349.61

def test_pressure_loss_from_pipe_reduction():
    assert round(water_flow.pressure_loss_from_pipe_reduction(0.2, 0.1, 10, 0.05, 1.002e-6), 2) == 23.55
    assert round(water_flow.pressure_loss_from_pipe_reduction(0.3, 0.2, 20, 0.1, 1.002e-6), 2) == 6.5
    assert round(water_flow.pressure_loss_from_pipe_reduction(0.4, 0.3, 30, 0.15, 1.002e-6), 2) == 3.17
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])