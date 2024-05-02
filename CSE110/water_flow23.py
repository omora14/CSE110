from ctypes import _NamedFuncPointer


def water_column_height(tower_height, tank_height):

    weight = tank_height * 3
    height = tower_height + weight / 4 

    return height


def pressure_gain_from_water_height(height):
    
    density = 998.2 #kg/m^3
    gravity = 9.80665 #m/s^2
    pressure = (density * gravity * height) / 1000  #kPa

    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    density = 998.2
    losspipe = (-friction_factor * pipe_length * density * (fluid_velocity**2)) / (2000 * pipe_diameter)

    return losspipe
    


"""def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    densityy = 998.2 #kg/m^3.
    numerator = -friction_factor * pipe_length * densityy * (fluid_velocity**2)
    denominator = 2000 * pipe_diameter

    return numerator/denominator"""

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    
    density = 998.2 #kg/m^3
    fittings = (-.04 * density * (fluid_velocity**2) * quantity_fittings) / 2000

    return fittings


def reynolds_number(hydraulic_diameter, fluid_velocity):

    density = 998.2 #kg/m^3.
    viscosity = 0.0010016 #Pascal seconds

    reynolds = (density * hydraulic_diameter * fluid_velocity) / viscosity
    
    return reynolds
    
def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    
    density = 998.2
    fr1 = (.01 + 50/reynolds_number)
    fr2 = ((((larger_diameter)**4/smaller_diameter)) - 1)
    keeey = fr1 * fr2

    lostpressure = -(keeey * density * fluid_velocity**2) / 2000
    
    return lostpressure













PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()