print("------- Multi-Number Calculator -------")
print("Available operations:")
print("add, subtract, multiply, divide, power,\nsquare, cube, average, maximum, minimum")
print("Type 'exit' to stop the calculator")
print("----------------------------------------")

while True:
    operation = input("\nEnter operation: ").lower()

    if operation == "exit":
        print("Calculator closed.")
        break

    #  for operations that need more than one numbers
    if operation in ["add", "subtract", "multiply", "divide", "power",
                     "average", "maximum", "minimum"]:
        nums = input("Enter numbers separated by space: ").split()
        nums = [float(n) for n in nums]

    # operations needing one number
    elif operation in ["square", "cube"]:
        num = float(input("Enter the number: "))

    else:
        print("Invalid operation!")
        continue

    if operation == "add":
        result = 0
        for n in nums:
            result += n
        print("Result:", result)

    elif operation == "subtract":
        result = nums[0]
        for n in nums[1:]:
            result -= n
        print("Result:", result)

    elif operation == "multiply":
        result = 1
        for n in nums:
            result *= n
        print("Result:", result)

    elif operation == "divide":
        result = nums[0]
        for n in nums[1:]:
            if n == 0:
                result = "Error! Division by zero."
                break
            result /= n
        print("Result:", result)

    elif operation == "power":
        result = nums[0]
        for n in nums[1:]:
            result = result ** n
        print("Result:", result)

    elif operation == "square":
        print("Result:", num * num)

    elif operation == "cube":
        print("Result:", num * num * num)

    elif operation == "average":
        total = 0
        for n in nums:
            total += n
        print("Result:", total / len(nums))

    elif operation == "maximum":
        max_value = nums[0]
        for n in nums:
            if n > max_value:
                max_value = n
        print("Result:", max_value)

    elif operation == "minimum":
        min_value = nums[0]
        for n in nums:
            if n < min_value:
                min_value = n
        print("Result:", min_value)

    else:
        print("Invalid operation!")
