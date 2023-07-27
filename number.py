import numpy as np

import main

from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist  # библиотека рукописных цифр
from sklearn.model_selection import train_test_split  # разделение выборонов�


class NN_number():
	def __init__(self):
		super().__init__()
		self.model = None
		self.x_test = None
	
	def predict(self):
		(x_train, y_train), (self.x_test, y_test) = mnist.load_data()
		
		x_train = x_train / 255
		self.x_test = self.x_test / 255
		
		y_train_cat = keras.utils.to_categorical(y_train, 10)
		y_test_cat = keras.utils.to_categorical(y_test, 10)
		
		self.model = keras.Sequential([
			Flatten(input_shape=(28, 28, 1)),
			Dense(128, activation='relu'),
			Dense(10, activation='softmax')
		])
		
		self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
		
		x_train_split, x_val_split, y_train_split, y_val_split = train_test_split(x_train, y_train_cat, test_size=0.2)
		self.model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_data=(x_val_split, y_val_split))
		
		self.model.evaluate(self.x_test, y_test_cat)  # проверка на тестовой выборке
	
	def recognize_picture(self, image):
		image = image / 255
		image = 1 - image
		x = np.expand_dims(image, axis=0)  # что бы из 2х мерной матрицы сделать 3х мерную
		res = self.model.predict(x)  # можно подавать только 3х мерную матрицу (несколько изображений)
		main.setProgressBars(res)