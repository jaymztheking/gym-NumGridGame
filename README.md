# gym-NumGridGame

This is an Open AI gym environment that simulates a turn-based number
game.  The game begins with a 10 by 10 grid of empty spaces.  The player
then spawns in a random cell.  The player can move 3 spaces up, down,
left or right within the bounds of the grid.  Alternatively, the player 
can move in any of the 4 diagonal directions by moving 2 spaces left or 
right and then 2 spaces up or down.  Once the player moves, the original 
location is considered filled and the game repeats.  The player may not 
move to a filled space. The game is over once the player cannot legally 
move to a space. The end goal is to fill all 100 spaces before the game 
ends.

## MaskableDiscrete

This package also contains a custom implementation of
`gym.spaces.Discrete`.  This version is a numpy array of integers
between 0 and n just like the original with the additional functionality
of masking.  The user can initialize the space with a numpy array of
type bool and of size n and the resulting space will be a subset of
integers between 0 and n based on the contents of the numpy boolean
array.

Example:
```
>space = MaskableDiscrete(5, [True, False, False, True, True])
>print(space.getvalues())
[0 3 4]
```

