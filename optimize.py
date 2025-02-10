from pulp import LpMaximize, LpProblem, LpVariable, value

# Define the model
model = LpProblem(name="profit-maximization", sense=LpMaximize)

# Define decision variables
A = LpVariable(name="Product_A", lowBound=0, cat="Continuous")
B = LpVariable(name="Product_B", lowBound=0, cat="Continuous")

# Objective function (maximize profit)
model += 40 * A + 50 * B, "Total_Profit"

# Constraints
model += 2 * A + 4 * B <= 40, "Machine_Hours_Constraint"
model += 3 * A + 2 * B <= 30, "Labor_Hours_Constraint"
model += A + B <= 15, "Raw_Materials_Constraint"

# Solve the model
model.solve()

# Print results
print(f"Optimal production of Product A: {A.varValue} units")
print(f"Optimal production of Product B: {B.varValue} units")
print(f"Maximum Profit: ${value(model.objective)}")
