line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
row = int(position[1]) - 1
column = 0
if position[0] == 'A':
    column = 0
if position[0] == 'B':
    column = 1
if position[0] == 'C':
    column = 2

map[row][column] = 'X'
print(f"{line1}\n{line2}\n{line3}")