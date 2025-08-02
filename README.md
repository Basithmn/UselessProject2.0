<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# Snail Maze Escape 🎯


## Basic Details
### Team Name: Incognito


### Team Members
- Team Lead: Abdul Basith M N - RIT Kottayam
- Member 2: Geethul Krishna G D - RIT Kottayam

### Project Description
This playful maze game uses Pygame to render a grid‑based labyrinth. You guide a snail emoji 🐌 cursor via the mouse (telekinesis not required), trying to reach the finish without clipping the walls. Fail, and PyAutoGUI audibly (but imperceptibly) snaps you back to start.

### The Problem (that doesn't exist)
Speed‑runners want a snail‑controlled maze where walled pathways feel instant and ominous… because moving slowly at high stakes is ironically dramatic.

### The Solution (that nobody asked for)
Enter Snail Maze Escape — a full‑screen maze generator with 🐌 emoji cursor and wall‑penalty resets. Touch a wall and you instantly teleport back to the start. It’s gratuitously snail-paced and spectacularly unnecessary.

## Technical Details
### Technologies/Components Used
For Software:
- Languages: Python 3.13.3
- Frameworks: Pygame (2.0+), PyAutoGUI  
- Libraries: `random`, `sys`  
- Tools: Full‑screen mouse interactions
  
### Implementation
For Software:
# Installation
[commands]

# Run
[commands]

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
+----------------------+  
| generate_maze()      |  
|  ↳ dfs + carve dirs  |  
+----------+-----------+  
           | maze array  
+----------------------+      +---------------+     +------------------+  
| main event loop      |      | input handler |     | rendering logic  |  
|  ↳ get mouse pos     | ↔–→   "🐌" snail      |     paint cells/🐌/flag  |  
|  ↳ collision sample_line() |   reset via    |     shrink wrap path         |  
+----------------------+      | prev ← start  |     +------------------+  
                              +---------------+  


# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- Abdul Basith M N: UI / interaction & PyAutoGUI integration
- Geethul Krishna G D: Maze‑generation core & collision detection

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



