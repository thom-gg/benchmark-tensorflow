import model
import configurations
import matplotlib.pyplot as plt


results = []
max_accuracy = 0
min_accuracy = 1

for nb_epochs in configurations.number_of_training_epochs:
    for config in configurations.configurations_to_try:
        (accuracy, duration) = model.create_and_evaluate_model(config, nb_epochs)
        results.append( (accuracy, duration) )
        if accuracy > max_accuracy:
            max_accuracy = accuracy 
        if accuracy < min_accuracy:
            min_accuracy = accuracy


bar_names = []
bar_values = []

i = 0
for nb_epochs in configurations.number_of_training_epochs:
    for config in configurations.configurations_to_try:
        (accuracy, duration) = results[i]
        bar_names.append(str(nb_epochs) + " epochs\n" + config.toVerticalString())
        bar_values.append(float("{:.5f}".format(accuracy)))
        print("Training for " + str(nb_epochs) + " epochs with " + config.toString() + " accuracy="+ str(accuracy)+ ", duration=" +str(duration))
        i+=1




fig, ax = plt.subplots()

bars = ax.bar(bar_names, bar_values)

plt.subplots_adjust(bottom=0.25)
ax.set_ylim(min_accuracy - 0.01, max_accuracy + 0.01)
ax.set_ylabel('accuracy')
ax.set_title('Model accuracy change when adding / modifying hidden layers')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), ha='center', va='bottom')


plt.show()