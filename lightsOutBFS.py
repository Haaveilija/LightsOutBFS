def starting_state():
    return [
    "#11#",
    "1111",
    "1111",
    "#11#"
    ]


def maze_str_to_list(maze_str):
    return maze_str.split("\n")


def maze_list_to_str(maze_list):
    return "\n".join(maze_list)


def next_states(current_state: str):
    """
    Get the list of next possible states after all possible next moves
    """
    current_state_list = maze_str_to_list(current_state)
    states = []
    for i in range(len(current_state_list[0])):
        for j in range(len(current_state_list)):
            test_state = current_state_list.copy()
            if move_is_valid(test_state, (i,j)):
                states.append(create_state(current_state_list, (i,j)))
    return states


def flip_state(state):
    """
    Change state between 1 and 0
    """
    if state == "1":
        return "0"
    elif state == "0":
        return "1"
    else:
        return "#"


def create_state(current_state: list, move_coords: tuple):
    """
    Create a new state given the previous state and 
    the coordinates of the move
    """

    x, y = move_coords
    new_state = current_state.copy()
    for i in range(len(current_state[0])):
        for j in range(len(current_state)):
            if -1 <= x-i <= 1 \
            and -1 <= y-j <= 1:
                #new_state[i][j] = flip_state(new_state[i][j])
                new_state[i] = new_state[i][:j] + flip_state(new_state[i][j]) + new_state[i][j+1:]
    return maze_list_to_str(new_state)


def move_is_valid(current_state, move_coords):
    """
    Check that a move in given coordinates is valid
    i.e. not a #-block or outside the game board
    """
    x, y = move_coords
    return 0 <= x < len(current_state[0]) \
        and 0 <= y < len(current_state) \
        and current_state[y][x] != "#"


def bfs(starting_state, end_condition):
    queue = [starting_state]
    discovered = {starting_state: None}

    while len(queue) != 0:
        current = queue.pop(0)

        if end_condition(current):
            print("Solution found")
            path = [current]
            while discovered[current] is not None:
                current = discovered[current]
                path.append(current)

            for coord in reversed(path):
                print(coord, end="\n\n")
            return
        
        for next_state in next_states(current):
            if next_state not in discovered:
                queue.append(next_state)
                discovered[next_state] = current


def puzzle_ready(state):
    """
    Check whether the puzzle is finished in its current state
    """
    final = (
    "#00#",
    "0000",
    "0000",
    "#00#")
    state_list = maze_str_to_list(state)
    for i in range(len(state_list[0])):
        for j in range(len(state_list)):
            if state_list[i][j] != final[i][j]:
                return False
    return True


def main():
    maze = maze_list_to_str(starting_state())
    bfs(maze, puzzle_ready)


if __name__ == "__main__":
    main()

