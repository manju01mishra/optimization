# Import necessary libraries
from pulp import LpMaximize, LpProblem, LpVariable

# Define the problem
problem = LpProblem("Maximize_Profit", LpMaximize)

# Define decision variables
x1 = LpVariable('x1', lowBound=0, cat='Continuous')  # Product A
x2 = LpVariable('x2', lowBound=0, cat='Continuous')  # Product B

# Objective function
problem += 10 * x1 + 15 * x2, "Total_Profit"

# Constraints
problem += 4 * x1 + 3 * x2 <= 160, "Time_Constraint"
problem += 2 * x1 + 3 * x2 <= 120, "Raw_Material_Constraint"

# Solve the problem
problem.solve()

# Get the solution
x1_solution = x1.varValue
x2_solution = x2.varValue
max_profit = problem.objective.value()

# Display the results
print(f"Optimal number of Product A to produce: {x1_solution}")
print(f"Optimal number of Product B to produce: {x2_solution}")
print(f"Maximum Profit: ${max_profit}")
