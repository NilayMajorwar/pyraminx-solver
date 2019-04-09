# Main entry point for the PyraminxSolver project

import cli, copy, pUtils
from PyraminxSolver import PyraminxSolver
import OptimalSolver

def main():
  print("Welcome to the PyraminxSolver Project\n")

  # Load pyraminx configuration from file
  pyraminx = cli.getFromFile("pyrConfig.txt")

  # Take config input from console
  # pyraminx = cli.inputState()

  # Scramble pyraminx from file
  # pyraminx = cli.scramblePyraminx("scramble.txt")

  # Generate random scramble
  # scramble = pUtils.generateScramble(15)
  # print("Scramble: ", end='')
  # cli.printAlgo(scramble)
  # pyraminx = pUtils.scramble(scramble)
 # --------------------------------------

  pUtils.fixColors(pyraminx)
  origPyraminx = copy.deepcopy(pyraminx)

  # Optimal Solver
  # algo = OptimalSolver.solve(pyraminx)

  # Intuitive Solver
  try:
    solver = PyraminxSolver(pyraminx)
    algo = solver.solve()
    algo = pUtils.simplifyAlgo(algo)
  except:
    algo = []

  isSolved = pUtils.checkSolution(origPyraminx, algo)
  if isSolved:
    print("Solution algorithm:")
    cli.printAlgo(algo)
    print("Yeah, it works.")
  else:
    print("How DARE you give me an invalid configuration!")


if __name__ == "__main__":
  main()
