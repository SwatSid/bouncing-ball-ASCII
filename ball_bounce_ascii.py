import time

g = -9.8
u = 0
dt = 0.06
# dt = 0.001

s_o = 1.5
while True:
    
    v = u + g*dt
    s = s_o + u*dt + (g*dt**2)/2
    
    # print(s," = ",s_o," + ",u,"*",dt," + (",g,"*",dt,"**2)/2)")
    pos = int(s * 100)
    
    # print(s, pos)
    for i in range(pos):
        print(" ", end='')
    print("o")
    
    u = v
    
    if (s <= 0 and s_o >= 0):
        u = -u*0.95
        
    s_o = s
    
    time.sleep(0.01)