from GUI import GUI
from HAL import HAL
# Enter sequential code!

i = 0
while True:
    # Enter iterative code!
    x, y, z, az = 0, 0, 1, 0
    vx,vy,vz,az = 0, 0, 1, 0
    
    HAL.set_cmd_pos(x, y, z, az)
    HAL.set_cmd_vel(vx, vy, vz, az)
    print('%d i:' % (i))
    i = i + 1