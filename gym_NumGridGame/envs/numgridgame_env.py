import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

class NumGridGameEnv(gym.Env):
	'''
	Description:
		An empty grid except for one initial starting point inside a random cell.  The player may move up, down, left,
		or right 3 spaces or diagonal 2 spaces (e.g. up 2, then left 2 spaces from the initial cell.  The cell becomes
		filled.  This continues until the player runs out of possible moves for the current cell position.  The
		objective is to fill all cells before exhausting all possible moves.

	Observation:
		Type: Box(m x n)
		Array of cells in the grid where m is the user-specified number of rows and n is the user-specified number of
		columns.  The value in the array corresponds to one of 3 states:
		Num		State Description
		0		Cell is empty
		1		Cell is filled
		2		Cell is current player location

	Actions:
		Type: Discrete(9)
		Num		Action
		0		Move down-left
		1		Move down
		2		Move down-right
		3		Move left
		4		Move right
		5		Move up-left
		6		Move up
		7		Move up-right

	Reward:
		Reward is 1 for every successfully filled cell per move

	Starting State:
		An empty m x n grid with one filled cell that serves as the player's starting cell.

	Episode Termination:
		All moves available to the player are blocked by filled cells


	'''
	metadata = {'render.modes':['human']}

	def __init__(self):
		self.rows = 10
		self.columns = 10
		self.state = None

		self.action_space = spaces.Discrete(8)
		self.observation_space = spaces.Box(0, 2, shape=(10,10), dtype=np.int32)

	def step(self, action):
		reward = 1
		done = False
		return np.array(self.state), reward, done, {}

	def reset(self):
		self.state = [[0 for i in self.rows] for j in self.rows]
		return np.array(self.state)

	def render(self, mode='human'):
		pass

	def close(self):
		pass


