# Simple Reflex Agent for Vacuum Cleaner
# The agent decides actions based on the current condition of the room (clean or dirty).

def vacuum_cleaner_agent(location_status):
    """
    Simulates a simple reflex vacuum cleaner agent.
    
    Parameters:
        location_status (dict): A dictionary containing the status of each location (e.g., {'A': 'dirty', 'B': 'clean', 'c': 'dirty', 'd':'dirty', 'd': 'clean'})
    
    Returns:
        list: Actions taken by the agent.
    """
    actions = []
    
    for location, status in location_status.items():
        if status == 'dirty':
            actions.append(f"Clean {location}")
            location_status[location] = 'clean'  # Update status to clean after cleaning.
        else:
            actions.append(f"Move to {location}")  # No cleaning needed, just move.
    
    return actions

# Example Usage:
if __name__ == "__main__":
    # Initial status of the rooms:
    # 'A' is dirty, 'B' is clean.
    environment = {
        'A': 'dirty',
        'B': 'clean',
        'c': 'dirty',
        'd': 'dirty',
        'e': 'clean'

    }

    print("Initial Environment Status:", environment)

    # Perform actions
    actions_taken = vacuum_cleaner_agent(environment)

    print("Actions Taken:")
    for action in actions_taken:
        print(action)

    print("Final Environment Status:", environment)
