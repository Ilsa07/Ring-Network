# Ring Network

This project contains two different ring network models, one which takes the connections between neurons into account and a simplified version which does not. Ring networks are used to model a group of neurons in the visual cortex, which have disctinct preferred edge orientations to which they respond with a maximal firing rate. 

### Neuron Inputs

![neuron_input](https://latex.codecogs.com/gif.latex?h_i%5E%7Bext%7D%28%5Ctheta_0%29%3Dc%5B%281-%5Cepsilon%29%20&plus;%20%5Cepsilon%20cos%282%28%5Ctheta_i%20-%20%5Ctheta_0%29%29%5D)

### Input Filtering

### Neuron Model

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
