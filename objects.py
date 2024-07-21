class Layer: # add layer type property later
    def __init__(self, nb_neurons: int):
        self.nb_neurons = nb_neurons

    def toString(self):
        return "Layer("+str(self.nb_neurons)+")"

class Configuration:
    def __init__(self, layers_list: list[Layer]):
        self.layers_list = layers_list
    
    def toString(self):
        res = ""
        for layer in self.layers_list:
            res += layer.toString() + ", "
        return res
    
    # Display layer list vertically (and grouping identical layers together)
    # 1x Layer(10)
    # 2x Layer(20) etc
    def toVerticalString(self):
        res = ""
        last_layer = ""
        counter_same = 0
        for i in range(len(self.layers_list)):
            current_layer = self.layers_list[i].toString()
            if (current_layer == last_layer):
                counter_same += 1 
            else:
                if i > 0:
                    res += str(counter_same) + "x " + last_layer + "\n"
                counter_same = 1 
            last_layer = current_layer
        if counter_same > 0:
            res += str(counter_same) + "x " + last_layer
        return res