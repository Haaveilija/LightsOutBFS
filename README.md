# LightsOutBFS

I run into a [Lights Out -puzzle](https://en.wikipedia.org/wiki/Lights_Out_(game)) while playing a [Minecraft puzzle map](https://www.curseforge.com/minecraft/worlds/diversity-3) and thought I could apply [BFS](https://en.wikipedia.org/wiki/Breadth-first_search) on it as I had just seen BFS being used on [this video on YouTube](https://www.youtube.com/watch?v=umszOeerdsU).

I used the same basic structure for BFS as was shown in the video, but had to make some changes due to the differences in the nature of the problems. In the video the problem was Theseus trying to find his way out of a labyrinth, but in my case there was no hero moving around. Still, there were different states and making a move at specific coordinates made it possible to move between the states.

The code allows expanding the game board to different sizes as long as the board is rectangular (i.e. each row has equal length and each column has equal height). Currently changing the size of the game board has to be done manually. On the game board, a "#" resembles an unplayable wall, 1 resembles a light on and 0 resembles a light off. In order to change the layout of the board, you have to edit the board inside the function `starting_state` and the `final` state inside the function `puzzle_ready`. I might end up creating a more practical way of creating and changing the game board, but that is in the future if I have a fitting burst of motivation and time :D.

In BFS each state is saved as a string since lists cannot be used as dictionary keys. Transforming these strings into game board lists and back to strings can be done using functions `maze_list_to_str` and `maze_str_to_list`.

Later on, another useful feature to implement would be to show exactly which button on the board is pressed, since right now the code outputs only each state from the beginning to the completion, and figuring out which button to press in order to move forward on this correct route is left for the user to deduce.
