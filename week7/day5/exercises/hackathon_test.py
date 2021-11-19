from hackathon import next_board_state
import numpy as np
if __name__ == "__main__":
    n = '\n'
    dead_state1 = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])
    expected_outcome1 = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])

    actual_outcome1 = next_board_state(dead_state1)

    if expected_outcome1.all() == actual_outcome1.all() :
        print("PASSED 1")
    else:
        print("FAILED 1!")
        print(f"Expected: {expected_outcome1}{n} Actual: {actual_outcome1}")


    start_state2 = np.array([
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ])
    expected_outcome2 = np.array([
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ])
    actual_outcome2 = next_board_state(start_state2)

    if expected_outcome2.all() == actual_outcome2.all():
        print("PASSED 2")
    else:
        print("FAILED 2!")
        print (f"Expected: {expected_outcome2}{n} Actual: {actual_outcome2}")