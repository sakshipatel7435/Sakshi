### Task 4: Simple RL Environment Simulator

# Build a console-based Python simulation that models the full agent-environment interaction loop for a delivery scenario, combining state tracking, action selection, and reward accumulation into a single class-based program.
# Requirement 1 - Define a DeliveryEnvironment class with attributes: current_state (a dictionary with at least location and pending_orders), total_reward, and step_count.
# Requirement 2 - Implement a step(action) method that updates the state based on the action taken, computes and returns a reward value, and prints the new state and reward after each step.
# Requirement 3 - Define at least three distinct actions with different state-transition effects and reward values (e.g. deliver_order, wait, navigate_to_zone).
# Requirement 4 - Run a loop that executes a predefined sequence of five or more actions, prints the result of each step, and displays the final total reward and total step count at the end.




class DeliveryEnvironment:
    def __init__(self):
        self.current_state = {
            "location": "Restaurant Hub",
            "pending_orders": 3
        }
        self.total_reward = 0.0
        self.step_count = 0

    def step(self, action):
        self.step_count += 1
        reward = 0
        
        if action == "deliver_order":
            if self.current_state["pending_orders"] > 0:
                self.current_state["pending_orders"] -= 1
                self.current_state["location"] = "Customer Location"
                reward = 15.0
            else:
                reward = -5.0 
        elif action == "navigate_to_zone":
            self.current_state["location"] = "High-Demand Zone"
            reward = 2.0
        elif action == "wait":
            reward = -1.0
        else:
            reward = -10.0 

        self.total_reward += reward
        
        print(f"Step {self.step_count} | Action: {action:<18} | Reward: {reward:>5.1f} | State: {self.current_state}")
        return self.current_state, reward

env = DeliveryEnvironment()
sequence_of_actions = [
    "navigate_to_zone",
    "deliver_order",
    "wait",
    "navigate_to_zone",
    "deliver_order"
]

for act in sequence_of_actions:
    env.step(act)

print(f"\nSimulation Finished! Total Steps: {env.step_count} | Final Total Reward: {env.total_reward}")