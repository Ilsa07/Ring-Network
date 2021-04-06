import numpy as np
import matplotlib.pyplot as plt
import math
number_of_neurons = 50


# Modelling the Inputs
# ********************
def h_input(theta: list, theta0: float, c: float, epsilon: float) -> type(np.array):
    """
    Model of the input stimuli to each neuron, which depends on its preferred orientation
    theta and the input stimuli theta0 and the contrast and selectivity of the stimuli and neuron
    Inputs:
        theta: preferred orientation of each neuron (in radians)
        theta0: orientation of the stimuli (in radians)
        c: contrast of the stimuli
        epsilon: selectivity of the input
    Output:
        The input received by each neuron for the given orientation of the stimuli
    """
    external_input = np.array([])
    for pref_orientation in theta:
        external_input = np.append(external_input, c*(1-epsilon)+epsilon* math.cos(2*(pref_orientation-theta0)))
    # return an array of numbers for each neuron, contatining how much excitation they get from the angle
    return external_input

def activation_filter(h:list, threshold:float, beta:float) -> type(np.array):
    """
    Non-linear filtering activation function of the external inputs at the neurons
    Inputs
        h: input stimuli for each neuron
        threshold: of neuron activation
        beta: scaling constant
    Output
        The filtered input stimuli to each neuron
    """
    activations = np.array([])
    # Non-linear filtering of external inputs
    for element in h:
        if element <= threshold:
            activations = np.append(activations, 0)
        elif threshold < element and element <= (threshold+1/beta):
            activations = np.append(activations, beta*(element - threshold))
        else:
            activations = np.append(activations, 1)
    
    return activations

preferred_angles = np.linspace(-math.pi/2, math.pi/2, number_of_neurons)
h_external = h_input(preferred_angles, 0, 3, 0.1)
activations = activation_filter(list(range(-15,15)), 0, 0.1)

# Plot the preferred orientations of the neurons
plt.plot(h_external)
plt.xlabel("Neuron index")
plt.ylabel("External input in response to stimuli")
plt.title("Response of Each Neuron to Stimuli")
plt.show()

# Plot the output of the Activation Function
plt.plot(np.linspace(-15, 15, 30), activations)
plt.xlabel("Input h")
plt.ylabel("Activation Function Output")
plt.title("Visualizing the Activation Function")
plt.show()


# Modelling the Neurons
# *********************
def rate_based_neuron_model(m: list, h_external: list) -> type(np.array):
    """
    Neuron Model solved with the Euler method to putout the activation of neurons over time
    Inputs:
        m: activity of each neuron at the previous time step
        h_external: input stimulus at each neruon
    Output:
        activity: the activity of each neuron in the next time step
    """
    tau = 5
    threshold = 0
    b = 0.1
    activity = np.array([])

    for x in range(len(m)):
        activity = np.append(activity, m[x] + activation_filter(h_external, threshold, b)[x] -m[x] / tau)
    
    return activity

def unconnected_neuron_model(m_in: list, theta0: float, n_neurons: int, t_steps:int, epsilon: float, c: float):
    """
    Modelling the activation of unconnected neurons over time
    Inputs
        m_in: initial activation of the neruons
        theta0: orientation of the stimuli
        n_neurons: number of neurons
        t_steps: number of timesteps to modell for
        epsilon: selectivity of the input
        c: contrast of the stimuli
    Output
        The activation of each neuron over time
    """
    activation_over_time = []
    preferred_angles = np.linspace(-math.pi/2, math.pi/2, n_neurons)

    for t in np.linspace(1, 1, t_steps):
        h_external = h_input(preferred_angles, theta0, c, epsilon)
        m_in = rate_based_neuron_model(m_in, h_external)
        activation_over_time.append(m_in)

    return activation_over_time

simulation_1 = unconnected_neuron_model([0]*number_of_neurons, 0, number_of_neurons, 30, 0.9, 1.2)
plt.imshow(np.array(simulation_1).T)
plt.xlabel("Time")
plt.ylabel("Neuron Index")
plt.title("Visualizing the Activation of Neurons Over Time")
plt.show()


# Modelling the Connected Network
# *******************************
def connections_between_neurons(n_neurons: int, j0: int, j2: int) -> type(list):
    """
    Modelling the connections between the neurons
    Inputs
        n_neurons: the number of neurons
        j0: weights one
        j1: weight 2
    Ouptut
        A 2D array containing the weight between each neuron
    """
    # Initialise the weights as a 2D array of zeros
    weights = np.zeros((n_neurons, n_neurons))
    preferred_angles = np.linspace(-math.pi/2, math.pi/2, n_neurons)

    # Calculate the weights between the connections
    for row in range(n_neurons):
        for column in range(n_neurons):
            weights[row][column] = -j0 + j2*math.cos(2*(preferred_angles[row] -preferred_angles[column]))
    
    return weights


connections = connections_between_neurons(number_of_neurons, 86, 112)
plt.imshow(connections)
plt.xlabel("Neuron Index")
plt.ylabel("Neuron Index")
plt.title("Connection Strengths Between Neurons")
plt.show()


def connected_neuron_model(m_in: list, theta0: float, n_neurons: int, t_steps:int, epsilon: float, c: float) -> type(list):
    """
    Modelling the activation of connected neurons over time
    Inputs
        m_in: initial activation of the neruons
        theta0: orientation of the stimuli
        n_neurons: number of neurons
        t_steps: number of timesteps to modell for
        epsilon: selectivity of the input
        c: contrast of the stimuli
    Output
        The activation of each neuron over time
    """
    activation_over_time = []
    preferred_angles = np.linspace(-math.pi/2, math.pi/2, n_neurons)
    connections = np.array(connections_between_neurons(n_neurons, 86, 112))

    for t in np.linspace(1, 1, t_steps):
        h_external = np.array(h_input(preferred_angles, theta0, c, epsilon))

        # Model the connections between the neurons in the input stimuli
        h_external_with_connections = h_external + (connections.dot(m_in))
        m_in = rate_based_neuron_model(m_in, h_external_with_connections)
        activation_over_time.append(m_in)

    return activation_over_time


activity = connected_neuron_model([0]*number_of_neurons, 0, number_of_neurons, 30, 0.4, 1.2)
plt.imshow(np.array(activity).T)
plt.xlabel("Time")
plt.ylabel("Neuron Index")
plt.title("Activity of the Network Over Time")
plt.show()