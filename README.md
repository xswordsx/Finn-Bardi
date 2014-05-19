Project for FMI's course on Python
====
Project type
-----
The project will be a classic [JRPG](http://en.wikipedia.org/wiki/Japanese_role-playing_game).

That being said, you will take control over the main character in the story. The game will have a few modes, including:

* Local World
* Whole World
* Battle phase
* Main menu
* Battle menu

The Local map will feature an array of Tiles which can be passable or non-passable. Any passable tile can have an NPC on it *(future concepts may need NPC being placed on unpassable tiles)*.

The Player is the heart of the game. He will be able to interact with NPCs & explore the world. He will have an inventory & stats *(such as health, mana, expirience, etc.)*. The interactions will be handled by menus and the arrow keys.

The states of the game will be controlled by a state-machine *(it will basicly be a type of stack)*.

The rendering of the game will be handled by pygame, as well as the collision detection (it has a *decent* collision detection).

While more research needs to be done, the battle phase will be a not-so-complex interaction of menus, monsters and the player. Prioriry of attacks and battle formues are yet to be conjured.

The world-map (global map) will be created by tiling together smaller local-maps *(I hope)*.

Next Milestone Goals
-----

* [ ] Playing (local) map
* [ ] Player outlines
* [ ] Load / Save functionality

Features
-----
* Load / Save game
* Map generation
* Combat
* **Player stuff**
  * Stats
  * Inventory


Project Dependencies
------
* [Python 3.3](https://www.python.org/) *(or later)*
* [Pygame](http://www.pygame.org/news.html)

License
------
The project *currently* falls under [GNU General Public License *(version 2)*](http://choosealicense.com/licenses/gpl-v2/)
* [License to use Python](https://docs.python.org/3/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python)
* [License to use Pygame](http://www.pygame.org/LGPL)
