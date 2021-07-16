import time

g = -9.8
u = 0
dt = 0.06

s_o = 1.5

def simulate_timestep(s_o, u, g, dt):
    v = u + g*dt
    s = s_o + u*dt + (g*dt**2)/2
    
    return s, v
    
def display_bounce(pos):
    for i in range(pos):
        print(" ", end='')
    print("o")
    
while True:
    
    s, v = simulate_timestep(s_o, u, g, dt)
    
    # variable to facilitate printing ascii ball
    pos = int(s * 100)
    
    if pos < 0:
        pos = 0
        
    display_bounce(pos)
    
    u = v
    
    # Bounce condition
    if (s <= 0 and s_o >= 0):
        u = -u*0.95
        
    s_o = s
    
    time.sleep(0.01)