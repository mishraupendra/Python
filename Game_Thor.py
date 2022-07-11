light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:

    direction = ''
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if light_x > initial_tx:
        initial_tx += 1
        direction += 'E'
    elif light_x < initial_tx:
        initial_tx -= 1
        direction += 'W'

    if light_y > initial_ty:
        initial_ty += 1
        direction += 'S'
    elif light_y < initial_ty:
        initial_ty -= 1
        direction += 'N'

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction)
