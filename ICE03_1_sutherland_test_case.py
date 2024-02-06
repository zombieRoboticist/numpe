# test case for ICE03_1:  Sutherland

from sutherland import calc_viscosity
temperature = 293.0    # Kelvin
viscosity = calc_viscosity(temperature)
string  = f'Viscosity at T = {temperature:.1f}'
string += f' [K] is {viscosity:.3e} [kg/m.s]'
print(string)