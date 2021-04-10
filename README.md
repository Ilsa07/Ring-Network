# Ring Network

This project contains two different ring network models, one which takes the connections between neurons into account and a simplified version which does not. Ring networks are used to model a group of neurons in the visual cortex, which have disctinct preferred edge orientations to which they respond to with a maximal firing rate. 

### Neuron Inputs
The inputs of the neurons depend on the orientation of the visual stimuli. The magnitude of the inputs is proportional, for a given neuron, to the difference between ints preferred orientation and the orientation of the stimuli, and is described by the equation below.

![neuron_input](https://latex.codecogs.com/gif.latex?h_i%5E%7Bext%7D%28%5Ctheta_0%29%3Dc%5B%281-%5Cepsilon%29%20&plus;%20%5Cepsilon%20cos%282%28%5Ctheta_i%20-%20%5Ctheta_0%29%29%5D)

### Input Filtering
The inputs to the neurons are non-linearly filtered given an activation function g. The function is defined by:

![input_filtering](https://latex.codecogs.com/gif.latex?g%28h%29%3D%20%5Cbegin%7Bcases%7D%200%20%26%20%5Ctext%7Bif%20%7D%20h%20%5Cleq%20T%5C%5C%20%5Cbeta%28h-T%29%20%26%20%5Ctext%7Bif%20%7D%20T%20%3C%20h%20%5Cleq%20T%20&plus;%201/%20%5Cbeta%5C%5C%201%20%26%20%5Ctext%7Bif%20%7D%20h%20%3E%20T%20&plus;%201/%5Cbeta%20%5Cend%7Bcases%7D)

### Neuron Model
The rate based neuron model used in this simulation is descibed by the equation below and is used with the Euler method.

![neuron_model](https://latex.codecogs.com/gif.latex?%5Ctau%20%5Cfrac%7Bdm_i%7D%7Bdt%7D%3D-m_i&plus;g%28h_i%29)

### Connections Model
The connections between neurons depend on their preferred orientations in the following way, where J0 and J2 are connection weights:

![connections_model](https://latex.codecogs.com/gif.latex?J_i_j%3D-J_0&plus;J_2cos%282%28%5Ctheta_i-%5Ctheta_j%29%29)

With the recurrent connections implemented between the neurons, the input to the neurons becomes:

![connected_inputs](https://latex.codecogs.com/gif.latex?h_i%28%5Ctheta_0%29%3D%5Csum_%7Bj%3D1%7D%5E%7B%5Cj%3DN%7D%20J_i_j%20m_j%20&plus;%20h_i%5E%7Bext%7D%28%5Ctheta_0%29)

## Getting Started
1. Clone the project and create a virtual environment
2. Install the required packages in the virtual environment
   ```
   pip3 install -r requirements.txt
   ```
