from gym_NumGridGame.envs.numgridgameenv import NumGridGameEnv
from gym.envs.classic_control import CartPoleEnv
from time import sleep

a = NumGridGameEnv()
#a = CartPoleEnv()
a.reset()

done = False
while done == False:
	a.render(mode='human')
	sleep(2)
	action = a.action_space.sample()
	state, reward, done, _ = a.step(action)
a.close()




