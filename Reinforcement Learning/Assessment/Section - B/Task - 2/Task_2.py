### Task 2: Agent State Tracker

# Build a dictionary-based Python program that tracks a delivery agent's state across multiple time steps, simulating the state component of an RL environment.
# Requirement 1 — Create a dictionary representing the agent's state with keys: location (string), orders_delivered (integer), total_reward (float), and is_available (boolean).
# Requirement 2 — Define a function update_state(state, new_location, reward_earned) that updates the agent's location, increments orders_delivered by 1, and adds reward_earned to total_reward.
# Requirement 3 — Simulate at least four state transitions by calling update_state with different locations and reward values.
# Requirement 4 — After each update, print the complete current state in a clear, readable format.




agent_state = {
    'location': 'Depot',
    'orders_delivered': 0,
    'total_reward': 0.0,
    'is_available': True
}

def update_state(state, new_location, reward_earned):
    state['location'] = new_location
    state['orders_delivered'] += 1
    state['total_reward'] += reward_earned
    print(f"Current State: {state}")

update_state(agent_state, 'Zone A', 15.0)
update_state(agent_state, 'Zone B', 12.5)
update_state(agent_state, 'Zone C', -2.0)
update_state(agent_state, 'Depot', 10.0)