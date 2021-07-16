import time

def simulate_timestep(s_o, u, g, dt):
    v = u + g*dt
    s = s_o + u*dt + (g*dt**2)/2
    
    # Bounce condition
    if (s <= 0 and s_o >= 0):
        v = -v*0.95
        
    return s, v
    
def display_bounce(pos):
    for i in range(pos):
        print(" ", end='')
    print("o")

def main():
    
    # Initial conditions
    s_o = 0
    s = s_o
    u = 5.5
    v = u
    
    # Simulation conditions
    g = -9.8
    dt = 0.06
    
    while True:
        # variable to facilitate printing ascii ball
        pos = int(s * 100)
        
        if pos < 0:
            pos = 0
            
        display_bounce(pos)
        
        s, v = simulate_timestep(s, v, g, dt)
        
        # u = v
        
        # Bounce condition
        # if (s <= 0 and s_o >= 0):
            # u = -u*0.95
            
        # s_o = s
        
        # Time delay to keep simulation slow enuf for human eye to follow
        time.sleep(0.01)
    
if __name__ == "__main__":
    main() 
    
