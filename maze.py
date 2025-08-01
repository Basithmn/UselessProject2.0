import pygame
import pyautogui
import random
import sys

# Prevent pyautogui from raising an exception if you drag to a corner
pyautogui.FAILSAFE = False

CELL_SIZE = 40
BORDER = 5
FPS = 60  # Increased frame rate for better motion smoothness

MAZE_COLOR = (200, 200, 200)
WALL_COLOR = (0, 0, 0)
TRACE_COLOR = (0, 200, 0)

START_POS = (0, 0)

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
COLS = (WIDTH - 2 * BORDER) // CELL_SIZE
ROWS = (HEIGHT - 2 * BORDER) // CELL_SIZE
MAZE_WIDTH = COLS * CELL_SIZE
MAZE_HEIGHT = ROWS * CELL_SIZE
OFFSET_X = (WIDTH - MAZE_WIDTH) // 2
OFFSET_Y = (HEIGHT - MAZE_HEIGHT) // 2

FINISH_POS = (ROWS - 1, COLS - 1)

clock = pygame.time.Clock()
font_popup = pygame.font.SysFont("Arial", 60)
font_count = pygame.font.SysFont("Arial", 50)


def generate_maze():
    maze = [[1] * COLS for _ in range(ROWS)]
    visited = [[False] * COLS for _ in range(ROWS)]

    def visit(r, c):
        visited[r][c] = True
        maze[r][c] = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr * 2, c + dc * 2
            if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc]:
                maze[r + dr][c + dc] = 0
                visit(nr, nc)

    visit(0, 0)
    maze[FINISH_POS[0]][FINISH_POS[1]] = 0
    return maze


def get_center_of_cell(r, c):
    return OFFSET_X + c * CELL_SIZE + CELL_SIZE // 2, OFFSET_Y + r * CELL_SIZE + CELL_SIZE // 2


def get_cell_from_mouse(pos):
    mx, my = pos
    row = (my - OFFSET_Y) // CELL_SIZE
    col = (mx - OFFSET_X) // CELL_SIZE
    if 0 <= row < ROWS and 0 <= col < COLS:
        return row, col
    else:
        return None


def draw_maze(maze, path):
    screen.fill((255, 255, 255))
    for r in range(ROWS):
        for c in range(COLS):
            color = WALL_COLOR if maze[r][c] else MAZE_COLOR
            x = OFFSET_X + c * CELL_SIZE
            y = OFFSET_Y + r * CELL_SIZE
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    # Draw the traced path
    for (r, c) in path:
        x = OFFSET_X + c * CELL_SIZE
        y = OFFSET_Y + r * CELL_SIZE
        pygame.draw.rect(screen, TRACE_COLOR, (x + 10, y + 10, CELL_SIZE - 20, CELL_SIZE - 20))

    # Draw finish flag
    cx, cy = get_center_of_cell(*FINISH_POS)
    flag = pygame.font.SysFont("Segoe UI Emoji", CELL_SIZE).render("🏁", True, (0, 0, 0))
    screen.blit(flag, flag.get_rect(center=(cx, cy)))

    # Maze border
    pygame.draw.rect(screen, WALL_COLOR, (OFFSET_X, OFFSET_Y, MAZE_WIDTH, MAZE_HEIGHT), 1)


def draw_cursor():
    x, y = pygame.mouse.get_pos()
    try:
        emo = pygame.font.SysFont("Segoe UI Emoji", 30).render("🐌", True, (0, 0, 0))
    except Exception:
        emo = pygame.font.SysFont("Arial", 30).render("🐌", True, (0, 0, 0))
    screen.blit(emo, emo.get_rect(center=(x, y)))


def show_center_message(message, color=(0, 255, 0)):
    text = font_popup.render(message, True, color)
    screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))


def reset_to_start(path):
    """Move cursor back to start, clear traced path, reset pyautogui."""
    sx, sy = get_center_of_cell(*START_POS)
    path.clear()
    pyautogui.moveTo(sx, sy)
    return START_POS


def sample_line(prev, curr, maze, path):
    """
    Perform Bresenham-like interpolation (or DDA) between prev and curr cells,
    checking each intermediate cell for a wall. If a wall is detected, return True.
    """
    pr, pc = prev
    cr, cc = curr
    dr = cr - pr
    dc = cc - pc
    steps = max(abs(dr), abs(dc))
    if steps == 0:
        return False  # no movement

    for i in range(1, steps + 1):
        t = i / steps
        ir = pr + round(dr * t)
        ic = pc + round(dc * t)
        if not (0 <= ir < ROWS and 0 <= ic < COLS):
            return True
        if maze[ir][ic] == 1:
            return True
        # Only add to path at final cell:
    return False


def main():
    maze = generate_maze()
    path = []

    # Place snail at start
    start_x, start_y = get_center_of_cell(*START_POS)
    pyautogui.moveTo(start_x, start_y)

    prev_cell = START_POS
    finished = False
    finish_ticks = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not finished:
                # Ignore Esc until after finishing
                pass

        mouse_pos = pygame.mouse.get_pos()
        cell = get_cell_from_mouse(mouse_pos)

        if not finished:
            if cell is None or maze[cell[0]][cell[1]] == 1:
                # Either outside maze or wall
                prev_cell = reset_to_start(path)
            else:
                if cell != prev_cell:
                    if sample_line(prev_cell, cell, maze, path):
                        prev_cell = reset_to_start(path)
                        cell = prev_cell
                    else:
                        path.append(cell)
                        prev_cell = cell

            if cell == FINISH_POS:
                finished = True
                finish_ticks = pygame.time.get_ticks()

        # Drawing & display logic
        now = pygame.time.get_ticks()
        draw_maze(maze, path)
        if not finished:
            draw_cursor()
        else:
            elapsed = now - finish_ticks
            if elapsed < 1_000:
                show_center_message("🎉 Finished!")
                draw_cursor()
            elif elapsed < 10_000:
                secs_left = 10 - (elapsed // 1_000)
                countdown = font_count.render(f"Game closes in {secs_left}", True, (255, 0, 0))
                screen.blit(countdown, countdown.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)))
                draw_cursor()
            elif elapsed < 11_000:
                show_center_message("Thanks for playing!")
                draw_cursor()
            else:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()