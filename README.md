# Cowards and Heroes

Welcome to **Cowards and Heroes**, a text-based adventure game where players create characters, explore a map, engage in combat, and collect loot. The goal is to survive, defeat enemies, and progress through levels.

## Features

### Character Creation
- Players can create a custom character by choosing a name, race, and allocating stat points.
- Races include Orc, Elf, Wood Elf, Dark Elf, Dragonborn, Dwarf, Human, and Goblin, each with unique base stats.
- Stats include Strength, Intelligence, Charisma, Dexterity, and Constitution.

### Map Exploration
- Navigate a 10x10 grid map using `w`, `a`, `s`, and `d` keys.
- Encounter enemies (`1`), loot chests (`2`), and level completion (`3`) as you explore.
- Players can flee combat using a smaller escape map.

### Combat System
- Engage in turn-based combat with enemies.
- Use weapons from your inventory or potions to heal during combat.
- Combat outcomes are determined by dice rolls.

### Inventory Management
- Collect weapons and potions from loot chests.
- View and manage your inventory during gameplay.

### Save and Load
- Save your progress automatically during gameplay.
- Load previous characters from `past_char.txt`.

## How to Run

### Prerequisites
- Python 3.x installed on your system.
- Install the `rich` library for enhanced terminal output:
  ```sh
  pip install rich
  ```

### Running the Game
1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Run the game using:
   ```sh
   python main.py
   ```

### File Structure
- `main.py`: Entry point for the game.
- `make_character.py`: Handles character creation.
- `map.py`: Manages map exploration and movement.
- `inventory.py`: Handles inventory and loot management.
- `char_funcs.py`: Contains utility functions for dice rolls, combat, and saving/loading.
- `chara_det.json`: Stores the current character's stats.
- `past_char.txt`: Stores saved characters.
- `save.txt`: Logs game progress.

## Current Limitations
- Combat is limited to basic attack and flee options.
- Map exploration does not include visual representation of the grid.
- Inventory management is basic and lacks advanced features like item removal.

## Future Improvements
- Add more detailed combat mechanics, such as special abilities.
- Enhance map exploration with visual representation.
- Expand inventory management to include item crafting or trading.

Enjoy your adventure in **Cowards and Heroes**!