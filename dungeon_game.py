import os
import random

# draw a grid
# pick random location for player, monster and exit door
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw the grid

CELLS = []
ROWS = 5
COLUMNS = 5

def create_grid(rows, columns):
	for row in range(rows):
		for column in range(columns):
			CELLS.append((column, row))


def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
	return random.sample(CELLS, 3)


def move_player(player, move):
	x, y = player

	if move == "LEFT":
		x -= 1
	elif move == "RIGHT":
		x += 1
	elif move == "UP":
		y -= 1
	elif move == "DOWN":
		y += 1

	return x, y


def get_moves(player):
	moves = ["LEFT", "RIGHT", "UP", "DOWN"]
	x, y = player

	if x == 0:
		moves.remove("LEFT")
	elif x == COLUMNS-1:
		moves.remove("RIGHT")
	if y == 0:
		moves.remove("UP")
	elif y == ROWS-1:
		moves.remove("DOWN")

	return moves


def draw_map(player):
	print(" _" * ROWS)
	tile = "|{}"

	for cell in CELLS:
		x, y = cell
		if x < ROWS-1:
			line_end = ""
			if cell == player:
				output = tile.format("X")
			else:
				output = tile.format("_")
		else:
			line_end = "\n"
			if cell == player:
				output = tile.format("X|")
			else:
				output = tile.format("_|")
		print(output, end=line_end)


def game_loop():
	player, monster, door = get_locations()
	playing = True
	
	while playing:
		clear_screen()
		draw_map(player)
		valid_moves = get_moves(player)
		print("You're currently in room {}".format(player))
		print("You can move {}".format(", ".join(valid_moves)))
		print("Enter QUIT to quit")

		move = input("> ").upper()

		if move == 'QUIT':
			print("\n ** Bye bye! **\n")
			break

		if move in valid_moves:
			player = move_player(player, move)

			if player == monster:
				print("\n ** Oh no! The monster got you! Better luck next time! ** \n")
				playing = False
			if player == door:
				print("\n ** You escaped! Congratulations! ** \n")
				playing = False

		else:
			input("\n ** Walls are hard! Don't run into them! **\n")
	else:
		if input("Play again? [Y/n]").lower() != 'n':
			game_loop()
		else:
			print("\n ** Bye bye! **\n")
		



create_grid(ROWS, COLUMNS)
clear_screen()

print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()

