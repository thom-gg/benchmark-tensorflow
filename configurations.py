from objects import Configuration, Layer


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