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
    s = 0
    v = 5.5
    
    # Simulation conditions
    g = -9.8
    dt = 0.06
    
    pos_count = 0
    
    while True:
        # variable to facilitate printing ascii ball
        pos = int(s * 100)
        
        if pos < 0:
            pos = 0
        else:
            pos_count = 0
        
        
        display_bounce(pos)
        
        s, v = simulate_timestep(s, v, g, dt)
        
        # Time delay to keep simulation slow enuf for human eye to follow
        time.sleep(0.01)
        
        
        if pos == 0:
            pos_count += 1
            
        # Break condition
        if pos_count > 10:
            break
    
if __name__ == "__main__":
    main() 
    
