### Task 3: Action-Reward Episode Logger

# Build a Python program that simulates one episode of a delivery RL agent executing a fixed sequence of actions and logs the cumulative reward at every step.
# Requirement 1 — Define a list of possible actions: ['accept_order', 'reject_order', 'request_directions', 'mark_delivered'].
# Requirement 2 — Assign a fixed reward to each action using a dictionary: accept_order = +2, reject_order = -1, request_directions = 0, mark_delivered = +10.
# Requirement 3 — Simulate an episode by iterating through a predefined sequence of at least six actions, computing and accumulating the reward at each step
# Requirement 4 — Print each step showing the action taken, the reward received at that step, and the running cumulative reward. Print the total episode reward at the end.




actions_list = ['accept_order', 'reject_order', 'request_directions', 'mark_delivered']
action_rewards = {
    'accept_order': 2,
    'reject_order': -1,
    'request_directions': 0,
    'mark_delivered': 10
}

episode_actions = [
    'accept_order',
    'request_directions',
    'mark_delivered',
    'accept_order',
    'reject_order',
    'mark_delivered'
]

cumulative_reward = 0

for step_num, action in enumerate(episode_actions, 1):
    reward = action_rewards[action]
    cumulative_reward += reward
    print(f"Step {step_num}: Action = {action} | Reward = {reward} | Cumulative Reward = {cumulative_reward}")

print(f"\nTotal Episode Reward: {cumulative_reward}")