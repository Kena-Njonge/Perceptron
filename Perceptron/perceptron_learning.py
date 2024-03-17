#We encode the number of Inputs for the perceptron. A perceptron is a neural network with no hidden layers.

example1 = "001211001"
example2 = "010300010"
example3 = "010100100"
example4 = "100210011"
example5 = "100101001"
example6 = "001310011"
example7 = "010101001"
example8 = "001200010"

input_examples = []

for i in range(1,9):
    input_examples.append( eval("example" + str(i)))

#We initialize the weights to 1 ""
input_weights = "11111111"
input_rate = 2

#A step function returns 1 if it receives a value greater than t, here t = 0;
def step_0(i):
    return 1 if i > 0  else 0 


output= 0

def learning(examples, weights, learning_rate):
    error_number= 0
    for i in examples:
        output_i = 0
        error_i = 0
        step_input_i = 0
        for j in range(0, i.length()-1):
            step_input_i_j = int(i[j] )* int(weights[j])
            step_input_i += step_input_i_j
        output_i=step_0(step_input_i_j)
        error_i = int(i[i.length()-1]) - output_i 
        if error_i != 0:
            update_weight(i,learning_rate,input_weights,error_i)
            error_number += 1
    return error_number

def update_weight(example,rate,weights,error):
    #Here we are refrencing the example strings
    for i in range(example.length()-1):
        if example[i] != 0 :
            weights[i] += weights[i] + (rate*int(example[i])*error)


    pass


def main():
    epoch = 1
    error_number = learning(input_examples,input_weights,input_rate)
    
    while error_number!= 0 :
        epoch += 1
        error_number = learning(input_examples,input_weights,input_rate)
        print(epoch)

if __name__ == "__main__":
    main()