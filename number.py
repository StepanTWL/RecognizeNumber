import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #выходной журнал tensorflow фиксирует только ошибки

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist         # библиотека рукописных цифр
from sklearn.model_selection import train_test_split # разделение выборонов�

def number():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train / 255
    x_test = x_test / 255


    plt.imshow(x_test[0], cmap=plt.cm.binary)
    plt.show()

    y_train_cat = keras.utils.to_categorical(y_train, 10)
    y_test_cat = keras.utils.to_categorical(y_test, 10)

    size_val = 10000
    x_val_split = x_train[:size_val]
    y_val_split = y_train_cat[:size_val]

    x_train_split = x_train[size_val:]
    y_train_split = y_train_cat[size_val:]

    model = keras.Sequential(
        [Flatten(input_shape=(28, 28, 1)), Dense(128, activation='relu'), Dense(10, activation='softmax')])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    x_train_split, x_val_split, y_train_split, y_val_split = train_test_split(x_train, y_train_cat, test_size=0.2)

    # model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2) # после каждых 32 изображений будут обновляться весовые коеф., 5 проходов, 80%/20% обучение/валидация (проверка что не идет переобучение выборки)
    model.fit(x_train, y_train_cat, batch_size=32, epochs=1, validation_data=(x_val_split, y_val_split))

    model.evaluate(x_test, y_test_cat)  # проверка на тестовой выборке

    n = 100
    x = np.expand_dims(x_test[n], axis=0)  # что бы из 2х мерной матрицы сделать 3х мерную
    res = model.predict(x)  # можно подавать только 3х мерную матрицу (несколько изображений)
    #plt.imshow(x_test[n], cmap=plt.cm.binary)
    #plt.show()

    pred = model.predict(x_test)
    pred = np.argmax(pred, axis=1)  # axis=1 во второй области списка (слой3)

    mask = pred != y_test
    x_false = x_test[mask]
    y_false = pred[mask]

number()