import gym

env = gym.make('CartPole-v1')

a = env.reset()
print(len(a))