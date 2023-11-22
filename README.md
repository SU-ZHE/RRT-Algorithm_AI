# Research-on-autonomous-exploration-path-planning-based-on-RRT-algorithm
This is project of robotic AI

Topic：Research on autonomous exploration path planning based on RRT algorithm
Abstract：Efficient navigation for robots typically relies on predefined maps. With advancements in computing, diverse autonomous exploration methodologies have emerged, enabling robots to independently discern boundaries and strategize paths for exploring unfamiliar terrains. These boundaries delineate the demarcation between known and unknown spaces. Primarily, frontier detection harnesses image processing techniques such as edge detection, primarily confined to two-dimensional (2D) exploration. This study adopts an exploration strategy centered on multiple Rapidly-exploring Random Trees (RRT), selected for its substantial advantages in navigating uncharted territories. Furthermore, the RRT algorithm presents a versatile framework extendable to higher-dimensional spaces. Due to temporal constraints, the adopted strategy is specifically implemented within a Python environment. Moreover, this research employs local and global trees to identify boundary points, thereby optimizing robot exploration efficiency. Presently, the scope of this endeavor is constrained to single-robot scenarios, leaving the extension to multi-agent systems and three-dimensional (3D) environments for prospective investigations.

You have to intsall python version 3.10 or above

and the 'coppeliasim' version 4.4 or bove  

#install dependencies 
pip install opencv-python numpy

pip install vrep

#final job demo 
#1. Open "path  planning.ttt" and start Simulation
#2. Run the following program: 
main.py 

#Test: RRT path planning

 path_planning.py
 
#Test: RRT path pruning

path_pruning.py 

#Test: line patrol 

path_following.py
