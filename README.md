# knapsack problem and graph coloring visualizer

this project demonstrates two well-known algorithms: the knapsack problem (brute force and dynamic programming) and graph coloring (using a greedy algorithm). both algorithms are visualized through a simple interactive interface built using python.

## features

- **knapsack problem**:
  - brute force solution (exponential time complexity).
  - dynamic programming solution (polynomial time complexity).
  - visualizes how the knapsack problem works by testing different input sizes and showing time taken.

- **graph coloring**:
  - greedy algorithm to assign colors to a graph (ensuring adjacent nodes don't share the same color).
  - visualizes the graph and the coloring process.

- **time complexity comparison**:
  - visualizes how the running time of both algorithms changes with input size.
  - shows graphs comparing brute force vs dynamic programming for the knapsack problem and graph coloring for different sizes of vertices.

## setup and installation

1. make sure you have python installed (preferably python 3.7 or higher).
2. install the required libraries using pip:
   ```bash
   pip install matplotlib pygame

running the project

download or clone this repository.
navigate to the project folder in your terminal.
run the script:
python knapsack_graph_coloring.py
the interactive interface will open. follow the on-screen instructions:
press '1' to test the knapsack problem.
press '2' to test the graph coloring algorithm.
press 'q' to quit the program.
how it works

the knapsack problem is a classic problem where you have to pick items with given weights and values to maximize the total value without exceeding a weight limit. two algorithms are tested: brute force and dynamic programming.
graph coloring involves assigning colors to graph vertices such that no two adjacent vertices have the same color. the greedy algorithm is used here, where vertices are assigned colors one by one in a simple way.
time complexity

the brute force approach for the knapsack problem has exponential time complexity 
O
(
2
n
)
O(2 
n
 ).
the dynamic programming approach for knapsack problem has polynomial time complexity
O
(
n
⋅
W
)
O(n⋅W), where 
n
n is the number of items and 
W
W is the capacity.
the graph coloring algorithm has time complexity 
O
(
V
2
)
O(V 
2
 ), where 
V
V is the number of vertices in the graph.
visualizations

the program uses pygame to provide an interactive interface.
you can watch the knapsack algorithm run, test different inputs, and see how the time complexity scales.
the graph coloring algorithm will display how it assigns colors to vertices while ensuring no adjacent vertices have the same color.
contributions

feel free to fork this repository and submit pull requests if you have improvements or ideas to add!

license

this project is open-source and available under the MIT License.
