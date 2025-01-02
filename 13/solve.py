from ortools.linear_solver import pywraplp

puzzles = open("13/input.txt").read().split("\n\n")


def count_tokens(puzzles, add=0):
    token_count = 0
    for puzzle in puzzles:
        button_a, button_b, prize = puzzle.split("\n")

        button_a_x, button_a_y = button_a.split(":")[1].split(",")
        button_b_x, button_b_y = button_b.split(":")[1].split(",")
        prize_x, prize_y = prize.split(":")[1].split(",")

        button_a_x = int(button_a_x.split("X")[1])
        button_a_y = int(button_a_y.split("Y")[1])
        button_b_x = int(button_b_x.split("X")[1])
        button_b_y = int(button_b_y.split("Y")[1])
        prize_x = int(prize_x.split("X")[1][1:])
        prize_y = int(prize_y.split("Y")[1][1:])
        prize_x += add
        prize_y += add
        solver = pywraplp.Solver.CreateSolver("SCIP")
        a = solver.IntVar(0, add * 10000, "a")
        b = solver.IntVar(0, add * 10000, "b")

        solver.Add(button_a_x * a + button_b_x * b == prize_x)
        solver.Add(button_a_y * a + button_b_y * b == prize_y)

        objective = solver.Objective()
        objective.SetCoefficient(a, 3)
        objective.SetCoefficient(b, 1)
        objective.SetMinimization()

        result = solver.Solve()

        if result == pywraplp.Solver.OPTIMAL:
            token_count += a.solution_value() * 3
            token_count += b.solution_value()

    return int(token_count)


# part 1
print(count_tokens(puzzles))

# part 2
print(count_tokens(puzzles, add=10000000000000))
