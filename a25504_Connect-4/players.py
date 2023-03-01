import random
import time
import pygame
import math


class connect4Player(object):
    def __init__(self, position, seed=0):
        self.position = position
        self.opponent = None
        self.seed = seed
        random.seed(seed)

    def play(self, env, move):
        move = [-1]


class human(connect4Player):
    def play(self, env, move):
        move[:] = [int(input("Select next move: "))]
        while True:
            if (
                int(move[0]) >= 0
                and int(move[0]) <= 6
                and env.topPosition[int(move[0])] >= 0
            ):
                break
            move[:] = [int(input("Index invalid. Select next move: "))]


class human2(connect4Player):
    def play(self, env, move):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if self.position == 1:
                        pygame.draw.circle(
                            screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS
                        )
                    else:
                        pygame.draw.circle(
                            screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS
                        )
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    move[:] = [col]
                    done = True


class randomAI(connect4Player):
    def play(self, env, move):
        possible = env.topPosition >= 0
        indices = []
        for i, p in enumerate(possible):
            if p:
                indices.append(i)
        move[:] = [random.choice(indices)]


class stupidAI(connect4Player):
    def play(self, env, move):
        possible = env.topPosition >= 0
        indices = []
        for i, p in enumerate(possible):
            if p:
                indices.append(i)
        if 3 in indices:
            move[:] = [3]
        elif 2 in indices:
            move[:] = [2]
        elif 1 in indices:
            move[:] = [1]
        elif 5 in indices:
            move[:] = [5]
        elif 6 in indices:
            move[:] = [6]
        else:
            move[:] = [0]


# class minimaxAI(connect4Player):
# 	def play(self, env, move):
# 		pass


class minimaxAI(connect4Player):
    def __init__(self, player, seed=None, depth=3):
        super().__init__(player, seed)
        self.depth = depth

    def play(self, env, move):
        best_score = -np.inf
        best_move = None
        for action in env.actions():
            score = self.minimax(env.result(action), self.depth, False)
            if score > best_score:
                best_score = score
                best_move = action
        move[:] = [best_move]

    def minimax(self, env, depth, maximizing_player):
        if depth == 0 or self.is_terminal(env):
            return self.score(env)
        if maximizing_player:
            best_score = -np.inf
            for action in env.actions():
                result = env.result(action)
                score = self.minimax(result, depth - 1, False)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = np.inf
            for action in env.actions():
                result = env.result(action)
                score = self.minimax(result, depth - 1, True)
                best_score = min(best_score, score)
            return best_score

    def score(self, env):
        if env.winner == self.player:
            return 100
        elif env.winner == 0:
            return 0
        else:
            return -100

    def is_terminal(self, env):
        return env.winner is not None or env.is_full()


# class alphaBetaAI(connect4Player):

# 	def __init__(self, position, seed=0, depth=4):
# 	    super(alphaBetaAI, self).__init__(position, seed)
# 	    self.depth = depth

# 	def play(self, env, move):
# 		possible_moves = [i for i in range(7) if env.topPosition[i] >= 0]
# 		max_score = float("-inf")
# 		best_move = random.choice(possible_moves)

# 		for move in possible_moves:
# 			score = self.alpha_beta_search(env, move, self.depth, float("-inf"), float("inf"), True)
# 			if score > max_score:
# 				max_score = score
# 				best_move = move

# 		move[:] = [best_move]

# 	def alpha_beta_search(self, env, move, depth, alpha, beta, is_max_player):
# 		env.play(move, self.position if is_max_player else self.opponent.position)

# 		if depth == 0 or env.gameOver():
# 			score = env.getScore(self.position)
# 			env.undo(move)
# 			return score

# 		possible_moves = [i for i in range(7) if env.topPosition[i] >= 0]
# 		best_score = float("-inf") if is_max_player else float("inf")

# 		for m in possible_moves:
# 			score = self.alpha_beta_search(env, m, depth - 1, alpha, beta, not is_max_player)
# 			if is_max_player:
# 				best_score = max(best_score, score)
# 				alpha = max(alpha, score)
# 			else:
# 				best_score = min(best_score, score)
# 				beta = min(beta, score)
# 			if alpha >= beta:
# 				break

# 		env.undo(move)
# 		return best_score

# improved version ,by use depth = 8
class alphaBetaAI(connect4Player):
    def __init__(self, position, seed=0, depth=8):
        super(alphaBetaAI, self).__init__(position, seed)
        self.depth = depth

    def play(self, env, move):
        possible_moves = [i for i in range(7) if env.topPosition[i] >= 0]
        max_score = float("-inf")
        best_move = random.choice(possible_moves)

        for move in possible_moves:
            score = self.alpha_beta_search(
                env, move, self.depth, float("-inf"), float("inf"), True
            )
            if score > max_score:
                max_score = score
                best_move = move

        move[:] = [best_move]

    def alpha_beta_search(self, env, move, depth, alpha, beta, is_max_player):
        env.play(move, self.position if is_max_player else self.opponent.position)

        if depth == 0 or env.gameOver():
            score = env.getScore(self.position)
            env.undo(move)
            return score

        possible_moves = [i for i in range(7) if env.topPosition[i] >= 0]

        # Heuristics to prioritize center column and edges
        if move == 3:
            score = 100
        elif move in [2, 4]:
            score = 50
        else:
            score = 0

        best_score = float("-inf") if is_max_player else float("inf")

        for m in possible_moves:
            s = self.alpha_beta_search(
                env, m, depth - 1, alpha, beta, not is_max_player
            )

            # Heuristics to prefer shorter winning sequences
            if s == 100 and depth == self.depth:
                score = 100
            elif s == -100 and depth == self.depth:
                score = -100
            elif s == 50 and score != 100:
                score = 50
            elif s == -50 and score != -100:
                score = -50

            if is_max_player:
                best_score = max(best_score, s)
                alpha = max(alpha, s)
            else:
                best_score = min(best_score, s)
                beta = min(beta, s)
            if alpha >= beta:
                break

        env.undo(move)
        return score if depth == self.depth else best_score


SQUARESIZE = 100
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
