import numpy as np

class Grid:

	def __init__():
		self.width = 10
		self.height = 10
		self.step = 0

	def start(self, initcoords):
		self.contents = [[0 for i in range(self.width)] for j in range(self.height)]
		self.step = 1
		self.contents[initcoords[0]][initcoords[1]] = self.step
		self.loc = initcoords

	def getcontents(self):
		return self.contents

	def getcurcoords(self):
		return self.loc

	def getstep(self):
		return self.step

	def getmovecoords(self):
		downleft = (self.loc[0]+2, self.loc[1]-2)
		down = (self.loc[0]+3, self.loc[1])
		downright = (self.loc[0]+2, self.loc[1]+2)
		left = (self.loc[0], self.loc[1]-3)
		stay = (self.loc[0], self.loc[1])
		right = (self.loc[0], self.loc[1]+3)
		upleft = (self.loc[0]-2, self.loc[1]-2)
		up = (self.loc[0]-3, self.loc[1])
		upright = (self.loc[0]-2, self.loc[1]+2)
		return [downleft, down, downright, left, stay, right, upleft, up, upright]

	def move(self, movetype):
		self.makemove(self.getmovecoords()[movetype])

	def makemove(self, coords):
		if self.validatemove(coords):
			self.step += 1
			self.contents[self.loc[0]][self.loc[1]] = 1
			self.contents[coords[0]][coords[1]] = 2
			self.loc = coords


	def validatemove(self, coords):
		#Check if cell in range
		if coords[0] not in range(0, self.height) or coords[1] not in range(0, self.width):
			return False

		# Check if cell already filled
		elif self.contents[coords[0]][coords[1]] > 0:
			return False

		else:
			return True

	def getpossiblemoves(self):
		moves = [self.validatemove(move) for move in self.getmovecoords()]
		return moves





