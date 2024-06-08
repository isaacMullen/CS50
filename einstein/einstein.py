user_mass = int(input('please enter a mass, in (kg): '))

def conserveEnergy(mass):
    return mass * (300000000 ** 2)
    
jules = conserveEnergy(user_mass)

print (jules)
