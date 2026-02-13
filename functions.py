# force = mass  x acceleration
# mass = 50
# acceleration = 10
# force = mass * acceleration
# print(f"Force = {force} Newtons")   ....Normal way of doing it not very efficient 

def calc_force(m,a):
    force = m * a
    return force


# mass = int(100)
# acceleration =int(10)


# calc_force(mass,acceleration)  # This is the efficient way of doing it.


simba_force = calc_force(100,10)
josh_force = calc_force(50,10)

print(f"Emmanuel's Force = {simba_force} Newtons")
print(f"Josh's Force = {josh_force} Newtons")