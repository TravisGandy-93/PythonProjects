"""Tower of Hanoi algorithm implementation."""
def hanoi_solver(n):
    """Function to solve the Tower of Hanoi problem and return the states."""
    # Set up rods: rod 0 = start, rod 1 = auxiliary, rod 2 = target
    rods = [list(range(n, 0, -1)), [], []]
    states = [f"{rods[0]} {rods[1]} {rods[2]}"]

    def record_state():
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(disks, rod0, rod1, rod2):
        if disks == 0:
            return
        move_disks(disks - 1, rod0, rod2, rod1)

        # move one top-most disk from rod0 to rod2
        disk = rods[rod0].pop()
        rods[rod2].append(disk)
        record_state()

        move_disks(disks - 1, rod1, rod0, rod2)

    if n <= 0:
        return "[] [] []"

    move_disks(n, 0, 1, 2)
    return "\n".join(states)

print(hanoi_solver(2))
print(hanoi_solver(4))
print(hanoi_solver(5))
