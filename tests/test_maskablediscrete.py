import numpy as np
import unittest
from gym_NumGridGame.envs.maskablediscrete import MaskableDiscrete

class TestMaskableDiscrete(unittest.TestCase):

	def setUp(self):
		self.space1 = MaskableDiscrete(5, [True, False, False, True, True])
		self.space2 = MaskableDiscrete(3)

	def test_getvalues(self):
		self.assertIsInstance(self.space1.getvalues(), np.ndarray)
		self.assertSequenceEqual(np.array([0, 3, 4]).tolist(), self.space1.getvalues().tolist())
		self.assertSequenceEqual(np.arange(0,3).tolist(), self.space2.getvalues().tolist())


if __name__ == '__main__':
	unittest.main()

