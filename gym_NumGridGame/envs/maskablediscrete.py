from gym.spaces import Discrete
import numpy as np

class MaskableDiscrete(Discrete):

	def __init__(self, n, mask=None):
		"""
		Description:
			This is a custom space that is a subclass of the Discrete class from OpenAI Gym Spaces.  For the most part
			this is the same basic implementation of Discrete with the added functionality of masking.  A numpy array
			of booleans is stored in the object along with the existing Discrete attributes.  This allows for subsets
			of integers to be sampled in environments instead of all integers (e.g. sample [0,1,5] instead
			of [0,1,2,3,4,5])

		Attributes
		n: upper bound of the integer range (lower bound is assumed to be 0

		mask: numpy array of booleans, with array size of n

		"""
		super().__init__(n)
		if mask is None or (len(mask) != n):
			self.mask = np.array([True for i in range(n)])
		else:
			self.mask = mask

	def sample(self):
		values = self.getvalues()
		return values[self.np_random.randint(len(values))]

	def contains(self, x):
		if isinstance(x, int):
			as_int = x
		elif isinstance(x, (np.generic, np.ndarray)) and (x.dtype.char in np.typecodes['AllInteger'] and x.shape == ()):
			as_int = int(x)
		else:
			return False

		return as_int in self.getvalues()

	def __repr__(self):
		return "MaskableDiscrete(%d)" %self.n

	def __eq__(self, other):
		return isinstance(other, MaskableDiscrete) and self.n == other.n and self.mask == other.mask

	def getvalues(self):
		#Return a subset of 0..n range that has a True value in the corresponding mask
		return np.arange(0,self.n)[self.mask]

	def setmask(self, mask):
		if len(mask) != self.n:
			raise IndexError('Mask of length %d cannot be set for MaskableDiscrete of size %d' % (len(mask), self.n))
		elif not(isinstance(mask, np.ndarray)):
			raise TypeError('Mask must be a numpy array')
		elif mask.dtype != 'bool':
			raise TypeError('Mask was of dtype %s, must be of dtype bool' % mask.dtype)
		else:
			self.mask = mask

	def __len__(self):
		return len(self.getvalues())
