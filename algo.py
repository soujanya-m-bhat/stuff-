import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knapsack & Graph Coloring Visualizer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont("Arial", 24)

def knapsack(weights, values, capacity):
    n = len(weights)
    best_value = 0
    best_combination = []
    
    for i in range(1 << n):
        total_weight = total_value = 0
        combination = []
        
        for j in range(n):
            if (i >> j) & 1:
                total_weight += weights[j]
                total_value += values[j]
                combination.append(j)
        
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_combination = combination
    
    return best_value, best_combination

def welsh_powell(graph):
    n = len(graph)
    degrees = [(i, len(graph[i])) for i in range(n)]
    degrees.sort(key=lambda x: -x[1])
    
    colors = [-1] * n
    color = 0
    
    for node, _ in degrees:
        if colors[node] == -1:
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = color
            color += 1
    
    return colors

def visualize_knapsack(weights, values, capacity):
    screen.fill(WHITE)
    start_time = time.time()
    
    best_value, best_combination = knapsack(weights, values, capacity)
    
    elapsed_time = time.time() - start_time
    time_text = font.render(f"Time for Knapsack: {elapsed_time:.6f} seconds", True, BLACK)
    screen.blit(time_text, (20, 20))

    info_text = font.render(f"Best Value: {best_value}", True, GREEN)
    screen.blit(info_text, (20, 60))
    
    info_text = font.render(f"Items Selected: {best_combination}", True, GREEN)
    screen.blit(info_text, (20, 100))
    
    pygame.display.update()

def visualize_graph_coloring(graph):
    screen.fill(WHITE)
    start_time = time.time()

    colors = welsh_powell(graph)
    
    elapsed_time = time.time() - start_time
    time_text = font.render(f"Time for Welsh-Powell: {elapsed_time:.6f} seconds", True, BLACK)
    screen.blit(time_text, (20, 20))

    node_radius = 20
    node_positions = [(random.randint(100, 700), random.randint(100, 500)) for _ in range(len(graph))]
    
    for i, (x, y) in enumerate(node_positions):
        pygame.draw.circle(screen, (colors[i] * 100, 0, 255 - colors[i] * 100), (x, y), node_radius)
        node_text = font.render(f"{i}", True, WHITE)
        screen.blit(node_text, (x - 5, y - 5))
    
    for i in range(len(graph)):
        for neighbor in graph[i]:
            pygame.draw.line(screen, BLACK, node_positions[i], node_positions[neighbor], 2)
    
    pygame.display.update()

def main():
    running = True
    in_menu = True
    while running:
        if in_menu:
            screen.fill(WHITE)
            menu_text = font.render("1: Knapsack Problem | 2: Graph Coloring | Q: Quit", True, BLACK)
            screen.blit(menu_text, (20, 20))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Knapsack problem selected")
                    weights = [random.randint(5, 20) for _ in range(5)]
                    values = [random.randint(10, 100) for _ in range(5)]
                    capacity = 50
                    visualize_knapsack(weights, values, capacity)
                    in_menu = False
                elif event.key == pygame.K_2:
                    print("Graph coloring selected")
                    graph = [
                        [1, 2],
                        [0, 2],
                        [0, 1, 3],
                        [2, 4],
                        [3]
                    ]
                    visualize_graph_coloring(graph)
                    in_menu = False
                elif event.key == pygame.K_q:
                    running = False

        if not in_menu:
            # Pause for a moment after the visualization to allow user to see the result
            pygame.time.wait(2000)  # Wait 2 seconds (2000 ms)
            in_menu = True  # Return to the menu after the pause

    pygame.quit()

if __name__ == "__main__":
    main()
