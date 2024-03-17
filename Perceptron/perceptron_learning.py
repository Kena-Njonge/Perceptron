# We encode the number of Inputs for the perceptron. A perceptron is a neural network with no hidden layers.
example1 = "001211001"
example2 = "010300010"
example3 = "010100100"
example4 = "100210011"
example5 = "100101001"
example6 = "001310011"
example7 = "010101001"
example8 = "001200010"

input_examples = []

for i in range(1, 9):
    input_examples.append(eval("example" + str(i)))

# We initialize the weights to 1 ""
input_weights = [1, 1, 1, 1, 1, 1, 1, 1]  # Initialize as a list
input_rate = 2


# A step function returns 1 if it receives a value greater than t, here t = 0;
def step_0(i):
    return 1 if i > 0 else 0


def learning(examples, weights, learning_rate):
    error_number = 0
    for i in examples:
        output_i = 0
        error_i = 0
        step_input_i = 0
        for j in range(len(i) - 1):  # Changed to len(i)
            step_input_i_j = int(i[j]) * int(weights[j])
            step_input_i += step_input_i_j
        output_i = step_0(step_input_i)  # Changed to step_input_i
        error_i = int(i[-1]) - output_i  # Changed to i[-1] to access the last element
        if error_i != 0:
            update_weight(i, learning_rate, input_weights, error_i)
            error_number += 1
    return error_number


def update_weight(example, rate, weights, error):
    for i in range(len(example) - 1):  # Changed to len(example)
        if example[i] != '0':  # Changed to '0' as strings are being processed
            weights[i] = weights[i] + rate * int(example[i]) * error


def main():
    epoch = 1
    error_number = learning(input_examples, input_weights, input_rate)
    print(input_weights)
    while error_number != 0:
        epoch += 1
        error_number = learning(input_examples, input_weights, input_rate)
        print(epoch)
        print(input_weights)


if __name__ == "__main__":
    main()
