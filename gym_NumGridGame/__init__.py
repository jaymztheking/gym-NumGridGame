from gym.envs.registration import register

register(
	id='NumGridGame-v0',
	entry_point='gym_NumGridGame.envs:NumGridGameEnv'
)