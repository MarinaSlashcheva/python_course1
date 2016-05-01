from scipy.ndimage import imread
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics.classification import accuracy_score

accuracy = (10, 20, 40, 80, 100, 150, 200, 300, 400, 500, 1000)
algorithms = (RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier)

# function to get images from directory as matrix with shape of (n, 10000)
def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (10000, )
        images.append(x)
    images = np.array(images)
    return images

pizza = get_images("pizza")
watch = get_images("watch")
np.random.shuffle(pizza)
np.random.shuffle(watch)

print(pizza.shape)
print(watch.shape)

# 185 pizzas and 185 watches as training data
train_pizza = pizza[:185, ]
train_watch = watch[:185, ]

# other images are validation data
validate_pizza = pizza[185:, ]
validate_watch = watch[185:, ]

train = np.concatenate((train_pizza, train_watch))
validate = np.concatenate((validate_pizza, validate_watch))

# true classes 1 for pizza image and 0 for watch image
train_y = np.concatenate((np.ones(185), np.zeros(185)))
validate_y = np.concatenate((np.ones(38), np.zeros(38)))

results = open('scores.txt', 'w')
results.write('n_estimators' + '\t')
for i in accuracy:
    results.write(str(i) + '\t')
results.write('\n')

for classifier in algorithms:
    results.write(classifier.__name__ + '\t')
    for score in accuracy:
        algorithm = classifier(n_estimators=score)
        algorithm = algorithm.fit(train, train_y)

        predicted_y = algorithm.predict(validate)
        acc_score = accuracy_score(validate_y, predicted_y)
        results.write(str(acc_score) + '\t')
        print('done for ' + classifier.__name__ + 'with n_estimators' + str(score) + ' ' + str(acc_score))
    results.write('\n')


# I`ve got the biggest accuracy score (0.8684) with AdaBoostClassifier with n_estimators=300
ada = AdaBoostClassifier(n_estimators=300)
ada_train = ada.fit(train, train_y)

predicted_y = ada_train.predict(validate)
acc_score = accuracy_score(validate_y, predicted_y)
print(acc_score)

unknown = get_images('unknown')
un_predicted = ada_train.predict(unknown)
print(os.listdir('unknown'))
print(un_predicted)

# In this attempt accuracy score was 0.921
# 28 from 37 pictures were right choice