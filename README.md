<a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Seal_of_Guam.svg/256px-Seal_of_Guam.svg.png" alt="Seal of Guam by Andrew Duhan / CC0" title="Guaiya" align="right" height="120"/>
</a>

Guaiya Means Love
======================
Hybrid VN-RPG with an anti-colonial story and puzzle mechanic. 

## Contents

- [Installation](#installation)
- [Edit and Run Code](#edit-and-run-code)
- [Build RenPy Game](#build-renpy-game)
- [Pull Requests](#pull-requests)

## Installation
Adapted from [u/Tormuse on Tormuses' guide](https://www.reddit.com/r/DDLCMods/comments/fgprfu/tormuses_guide_march_2020/) 

To set up your dev environment for Guaiya, first you will need to install RenPy, the VN engine that we use to run and build .rpy VN game code. 

Install [Ren'Py](https://www.renpy.org/latest.html) in a folder of your choice and run it. Go into preferences and set a projects directory. (A folder where your Guaiya RenPy projects are going to go; it can always be changed later) You'll need a text editor that can edit .RPY files. Open RenPy and you should land on the RenPy Launcher screen.  Navigate to your projects folder and then to your Guaiya project folder; it should show up in Ren'Py's main menu on the left under "Projects." Make sure the selected project - the "Active Project" is the one containing your local copy of Guaiya and all its files.

Hit "Run" to make sure RenPy is able to compile and run the game in a non-published mode. A game window should appear with the start screen for Guaiya. Most common errors will be displayed via the in-game console OR in the RenPy screen itself.

## Edit and Run Code
The game begins running sequentially from script.rpy, where other files can run but always come back to script.rpy when waiting for the next instruction or player input. Try adding in code there first as you learn common RenPy commands and scripting. RenPy uses a type of Python that is easy to write things like 

```
c "Hello, my name is Clara" 
```
But of course the variable `c` needs to be defined earlier in script.rpy. Can you find where I have already defined `c` ? See if you can get Clara to say something in Guaiya by adding the above line of code right after `start:` block in script.py. Save your local changes, and hit "Run" in the RenPy Launcher screen to start up the game. Did Clara greet you? 

See [The RenPy Documention](https://www.renpy.org/doc/html/language_basics.html#) to learn scripting ! 

## Build RenPy Game

Inside the RenPy Launcher screen, make sure your project is the Active Project in the upper right hand corner. In the right hand panel, select "Build Distributions." RenPy will scan the project and alert you for any compilation errors. Select whether the build is for Mac, PC, etc. and then hit "Build." 

## Pull Requests
Please test your code and document how the code was tested. PRs will be merged into master only if the game a) builds successfully and b) does not break through a manual play-through of the effected conversation trees and levels. Please, please document how testing was done! For example, if commenting out certain levels or chapters made testing the code easier, this process should be documented in under the heading "Testing Steps" in the PR. 
