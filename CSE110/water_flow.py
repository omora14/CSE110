def water_column_height(tower_height, tank_height):
    w = tank_height
    t = tower_height
    h = t + 3*w/4
    return h


def pressure_gain_from_water_height(height):
    rho = 998.2
    g = 9.80665
    P = rho*g*height/1000
    return P


def pressure_loss_from_pipe(pipe_diameter, pipe_length, flow_rate, viscosity):
    rho = 998.2
    A = 3.14159*(pipe_diameter/2)**2
    v = flow_rate / A
    Re = pipe_diameter * v / viscosity
    f = 64/Re if Re < 2300 else 0.3164 / Re**(1/4)
    dp = f * pipe_length * rho * v**2 / (2 * pipe_diameter)
    return dp


def pressure_loss_from_fittings(n_fittings, pipe_diameter, flow_rate):
    K = 0.5
    v = flow_rate / (3.14159*(pipe_diameter/2)**2)
    dp = K*n_fittings*(v**2)/2
    return dp


def reynolds_number(pipe_diameter, flow_rate, viscosity):
    v = flow_rate / (3.14159*(pipe_diameter/2)**2)
    Re = pipe_diameter * v / viscosity
    return Re


def pressure_loss_from_pipe_reduction(pipe_diameter1, pipe_diameter2, pipe_length, flow_rate, viscosity):
    A1 = 3.14159*(pipe_diameter1/2)**2
    A2 = 3.14159*(pipe_diameter2/2)**2
    v1 = flow_rate / A1
    Re1 = pipe_diameter1 * v1 / viscosity
    f1 = 64/Re1 if Re1 < 2300 else 0.3164 / Re1**(1/4)
    v2 = flow_rate / A2
    Re2 = pipe_diameter2 * v2 / viscosity
    f2 = 64/Re2 if Re2 < 2300 else 0.3164 / Re2**(1/4)
    dp = f1 * pipe_length * v1**2 / (2 * pipe_diameter1) + f2 * pipe_length * v2**2 / (2 * pipe_diameter2)
    return dp

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
    viscosity = 1.002e-6  # Viscosity of water at 20°C
    reynolds = reynolds_number(diameter, velocity, viscosity)
    loss = pressure_loss_from_pipe(diameter, length1, velocity, viscosity)
    pressure += loss

    loss = pressure_loss_from_fittings(quantity_angles, diameter, velocity)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, HDPE_SDR11_INNER_DIAMETER, length1, velocity, viscosity)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, velocity, viscosity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
