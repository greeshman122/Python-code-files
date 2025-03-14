class ExpressionSolver:
    def __init__(self, expression):
        # Constructor to initialize the expression
        self.expression = expression

    def solve(self):
        try:
            # Evaluates the expression using Python's eval() function
            result = eval(self.expression)
            return result
        except Exception as e:
            # Handle invalid expressions
            return f"Error: Invalid expression. Details: {e}"


# Main function
def main():
    # Accept the expression from the user
    expression = input("Enter an arithmetic expression to solve (e.g., 3 + 5 * 2): ")
    
    # Create an object of the ExpressionSolver class
    solver = ExpressionSolver(expression)
    
    # Solve the expression and display the result
    result = solver.solve()
    print(f"The result of the expression '{expression}' is: {result}")


if __name__ == "__main__":
    main()
