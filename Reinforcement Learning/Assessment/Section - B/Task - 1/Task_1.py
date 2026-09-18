### Task 1: Delivery Reward Function

# Build a Python function that calculates and returns a reward score for a food delivery agent based on the outcome of a single delivery action.
# Requirement 1 — Define a function calculate_reward(delivery_time, is_on_time, customer_rating) that accepts three parameters.
# Requirement 2 — Award +10 points if is_on_time is True; deduct -5 points if it is False.
# Requirement 3 — Add the customer_rating (integer 1–5) directly to the reward total.
# Requirement 4 — Print the final reward with a descriptive message and test the function with at least three different input combinations showing different outcomes.



def calculate_reward(delivery_time, is_on_time, customer_rating):
    reward = 0
    
    if is_on_time:
        reward += 10
    else:
        reward -= 5
        
    reward += customer_rating
    
    print(f"Delivery Time: {delivery_time} mins | On-Time: {is_on_time} | Rating: {customer_rating} Stars -> Final Reward: {reward}")
    return reward

calculate_reward(25, True, 5)  
calculate_reward(45, False, 2) 
calculate_reward(30, True, 3)