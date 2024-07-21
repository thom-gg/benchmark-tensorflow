# benchmark-tensorflow

Little tool written in Python to try different configurations of TensorFlow Machine-learning models, to see what parameters can improve the most the accuracy of the model.

![Figure_1](https://github.com/user-attachments/assets/d825b8ae-c73e-4455-8212-f265d29e0dcc)

The model uses the well-known MNIST dataset (hand written digits https://yann.lecun.com/exdb/mnist/).

# Usage 
Install python3, and add modules tensorflow and matplotlib
`pip install tensorflow matplotlib`

You can then run the benchmark.py file 
`python3 benchmark.py`

You can try different configuration, changing these paremeters:
 - number of training epochs
 - number of layers
 - number of neurons in each layer
   

Edit configuration by modifiying configurations.py:
```py
# So we see if results are different for small amount of training and big amount of training
number_of_training_epochs = [5, 11] # All configurations will be benchmarked for all number of epochs


configurations_to_try: list[Configuration] = [
        Configuration([
            Layer(10)
        ]),
        Configuration([
            Layer(50),
        ]),
        Configuration([
            Layer(100),
        ]),
        Configuration([
            Layer(10),
            Layer(10),
        ]),
        Configuration([
            Layer(50),
            Layer(50),
        ]),
        Configuration([
            Layer(100),
            Layer(100),
        ]),
        Configuration([
            Layer(10),
            Layer(10),
            Layer(10)
        ]),
]
```

The data is then displayed in a bar chart using the matplotlib library
