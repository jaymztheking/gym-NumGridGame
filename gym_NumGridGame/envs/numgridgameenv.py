import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .maskablediscrete import MaskableDiscrete

import numpy as np

class NumGridGameEnv(gym.Env):
	"""
	Description:
		An empty grid except for one initial starting point inside a random cell.  The player may move up, down, left,
		or right 3 spaces or diagonal 2 spaces (e.g. up 2, then left 2 spaces from the initial cell).  The cell becomes
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
		3		Move
		4		Stay (masked as an invalid move)
		5		Move right
		6		Move up-left
		7		Move up
		8		Move up-right

	Reward:
		Reward is 1 for every successfully filled cell per move

	Starting State:
		An empty m x n grid with one filled cell that serves as the player's starting cell.

	Episode Termination:
		All moves available to the player are blocked by filled cells


	"""
	metadata = {'render.modes':['human']}

	def __init__(self):
		self.rows = 10
		self.columns = 10
		self.stepnum = 0
		self.pos = None
		self.prevpos = None
		self.state = None
		self.cells = {}
		self.possiblemoves = []

		self.action_space = MaskableDiscrete(9, np.array([True, True, True, True, False, True, True, True, True]))
		self.observation_space = spaces.Box(0, 2, shape=(self.rows, self.columns), dtype=np.int32)

		self.seed()
		self.viewer = None

	def seed(self, seed=None):
		self.np_random, seed = seeding.np_random(seed)
		return [seed]

	def step(self, action):
		reward = 1.0
		self.stepnum += 1
		self.prevpos = self.pos
		self.pos = self.getmoves()[action]
		self.state[self.prevpos[0]][self.prevpos[1]] = 1
		self.state[self.pos[0]][self.pos[1]] = 2
		self.action_space.setmask(self.getmask())
		done = len(self.action_space) == 0
		return np.array(self.state), reward, done, {}

	def reset(self):
		self.stepnum = 1
		self.pos = (np.random.randint(1,10), np.random.randint(1,10))
		self.state = [[0 for i in range(self.columns)] for j in range(self.rows)]
		self.state[self.pos[0]][self.pos[1]] = 2
		self.action_space.setmask(self.getmask())
		self.possiblemoves = self.getmoves()[self.action_space.getvalues()]
		return np.array(self.state)

	def render(self, mode='human'):
		screen_width = 800
		screen_height = 600

		cell_width = 50
		cell_height = 50

		if self.viewer is None:
			from gym.envs.classic_control import rendering
			self.viewer = rendering.Viewer(screen_width, screen_height)
			leftmargin = (screen_width-(cell_width*self.columns))/2
			topmargin = screen_height - (screen_height-(cell_height*self.rows))/2
			l, r, t, b = leftmargin, leftmargin+cell_width, topmargin, topmargin-cell_height

			for row in range(self.rows):
				for col in range(self.columns):
					self.cells[(row, col)] = rendering.FilledPolygon([(l, b), (l, t), (r, t), (r, b)])
					red, green, blue = self.getcolors(0)
					self.cells[(row, col)].set_color(red, green, blue)
					self.viewer.add_geom(self.cells[(row, col)])
					border = rendering.PolyLine([(l, b), (l, t), (r, t), (r, b), (l, b)], True)
					self.viewer.add_geom(border)
					l, r = l + cell_width, r + cell_width
				t, b = t - cell_height, b - cell_height
				l, r = leftmargin, leftmargin+cell_width

		if self.prevpos is not None:
			red, green, blue = self.getcolors(1)
			self.cells[tuple(self.prevpos)].set_color(red, green, blue)
			for i in self.possiblemoves:
				red, green, blue = self.getcolors(0)
				self.cells[tuple(i)].set_color(red, green, blue)

		red, green, blue = self.getcolors(2)
		self.cells[tuple(self.pos)].set_color(red, green, blue)

		red, green, blue = self.getcolors(3)
		self.possiblemoves = self.getmoves()[self.getmask()]
		for move in self.possiblemoves:
			self.cells[(move[0], move[1])].set_color(red, green, blue)

		return self.viewer.render(return_rgb_array=mode == 'rgb_array')

	def close(self):
		if self.viewer:
			self.viewer.close()
			self.viewer = None

	def getmoves(self):
		moves = [
			(self.pos[0] + 2, self.pos[1] - 2), #down-left
			(self.pos[0] + 3, self.pos[1]),  	#down
			(self.pos[0] + 2, self.pos[1] + 2), #down-right
			(self.pos[0], self.pos[1] - 3),		#left
			(self.pos[0], self.pos[1]),  		#stay
			(self.pos[0], self.pos[1] + 3),  	#right
			(self.pos[0] - 2, self.pos[1] - 2), #up-left
			(self.pos[0] - 3, self.pos[1]),  	#up
			(self.pos[0] - 2, self.pos[1] + 2), #up-right
		]

		return np.array(moves)

	def getmask(self):
		mask = [x[0] in range(0, self.rows) and x[1] in range(0, self.columns) and self.state[x[0]][x[1]] ==  0 \
				for x in self.getmoves()]
		return np.array(mask)

	def getcolors(self, state):
		if state == 0:
			return 1.0, 1.0, 1.0
		elif state == 1:
			return 1.0, 1.0, 0.2
		elif state == 2:
			return 1.0, .75, 0.2
		elif state == 3:
			return 0.5, 1.0, 1.0

	def getpossiblemoves(self):
		return self.getmoves()[self.getmask()]
