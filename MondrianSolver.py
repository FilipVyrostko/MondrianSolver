from Actions import next_action
from State import State


def SolveMondrian(dim: int, depth_lim: int) -> State:
    # Create initial State
    state = State(dim)
    # Get first action to take
    action = next_action(state, depth_lim)

    # While action to take, proceed
    while action:
        r, r1, r2 = action
        state.update(r, r1, r2)
        action = next_action(state, depth_lim)

    return state