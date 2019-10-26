
import numpy as np

curr_state = np.array([[1,2,3],[11,22,33]])
glb_nxt = (3,2)

f = open("GAME_STATE", "w+")
f.write(str(curr_state) + "\n" +str(glb_nxt))
f.close()


