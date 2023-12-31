import numpy as np

from main import *

from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, MaxPool2D, Conv2D, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model


class NN_number():
	def __init__(self):
		super().__init__()
		self.model = None
		self.x_test = None
	
	def predict_nn(self):
		(x_train, y_train), (self.x_test, y_test) = mnist.load_data()
		
		x_train = x_train / 255
		self.x_test = self.x_test / 255
		
		self.model = keras.Sequential([
			Conv2D(
				input_shape=(28, 28, 1),
				filters=32,
				kernel_size=(5, 5),
				padding='same',
				activation='relu',
			),
			MaxPool2D(pool_size=(2, 2)),
			Conv2D(
				filters=64,
				kernel_size=(5, 5),
				padding='same',
				activation='relu',
			),
			MaxPool2D(pool_size=(2, 2)),
			Flatten(),
			Dense(1024, activation='relu'),
			Dropout(0.4),
			Dense(10, activation='softmax')
		])
		
		self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
		
		self.model.fit(x_train.reshape(-1, 28, 28, 1), y_train, epochs=5)
		
		self.model.evaluate(self.x_test.reshape(-1, 28, 28, 1), y_test)
	
	def recognize_picture(self, image):
		image = image / 255
		image = 1 - image
		x = np.expand_dims(image, axis=0)  # что бы из 2х мерной матрицы сделать 3х мерную
		model = load_model('nn_recognize_number.keras')
		res = model.predict(x)  # можно подавать только 3х мерную матрицу (несколько изображений)
		return res
	
if __name__ == '__main__':
	neural = NN_number()
	neural.predict_nn()
	neural.model.save('nn_recognize_number.keras')