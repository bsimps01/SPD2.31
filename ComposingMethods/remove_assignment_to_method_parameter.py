# Remove assignment to method parameter.
class Distance:
    def __init__(self, distance_value, unit):
        self.unit = unit
        self.distance_value = distance_value
class Mass:
    def __init__(self, mass_value, unit):
        self.mass_value = mass_value
        self.unit = unit
def calculate_kinetic_energy(mass, light_year_distance, time):
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit        
            in_km = distance.distance_value * 9.461e12
            light_year_distance = Distance(in_km, "km") 
        else:
            print ("unit is Unknown")
            return
    speed = light_year_distance.distance_value/time # [km per sec]
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            kg_value = mass.mass_value * 1.98892e30 # [kg]
            mass = Mass(kg_value, 'kg')
        else:
            print ("unit is Unknown")
            return    
        
    kinetic_energy = 0.5 * mass.mass_value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))