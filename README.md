<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# Snail Maze Escape 🎯


## Basic Details
### Team Name: Incognito


### Team Members
- Team Lead: Abdul Basith M N - RIT Kottayam
- Member 2: Geethul Krishna G D - RIT Kottayam

### Project Description
This fullscreen Pygame maze game uses PyAutoGUI to tug your snail emoji 🐌 cursor back to the start upon any wall collision. Navigate the labyrinth by mouse, reach the 🏁 finish flag, and trigger the 10‑second exit countdown. Purposefully low‑speed, high drama.

### The Problem (that doesn't exist)
Maze games reward strategy—too useful. Here, each micro‑mistake results in immediate reset. It’s a gamified metaphor for snail-paced frustration.

### The Solution (that nobody asked for)
A snail maze with snappy reset punishment—reckless collision detection via line‑sampling, full‑screen rendering, emoji-driven UI, and countdown closure. Built under time constraints, with zero concern for practical use.

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
git clone https://github.com/your‑username/useless‑snail‑maze
cd useless‑snail‑maze
pip install pygame pyautogui

# Run
python main.py

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



