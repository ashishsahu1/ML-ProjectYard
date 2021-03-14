# Dataset -  https://www.kaggle.com/c/dogs-vs-cats

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()
    

# Loading data
base_dir = 'images'
train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')

train_cats = os.path.join(train_dir, 'cats')
train_dogs = os.path.join(train_dir, 'dogs')
test_cats = os.path.join(test_dir, 'cats')
test_dogs = os.path.join(test_dir, 'dogs')

num_cats_tr = len(os.listdir(train_cats))
num_dogs_tr = len(os.listdir(train_dogs))
num_cats_test = len(os.listdir(test_cats))
num_dogs_test = len(os.listdir(test_dogs))

total_train = num_cats_tr + num_dogs_tr
total_test = num_cats_test + num_dogs_test

BATCH_SIZE = 32
IMG_SHAPE = 150 

train_image_generator = ImageDataGenerator(
    rescale=1./255,rotation_range=40,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest'
    )

test_image_generator = ImageDataGenerator(rescale=1./255)


train_data_gen = train_image_generator.flow_from_directory(batch_size=BATCH_SIZE,directory=train_dir,shuffle=True,target_size=(IMG_SHAPE, IMG_SHAPE),class_mode='binary')
test_data_gen = train_image_generator.flow_from_directory(batch_size=BATCH_SIZE,directory=test_dir,shuffle=False,target_size=(IMG_SHAPE, IMG_SHAPE),class_mode='binary')
images = [train_data_gen[0][0][0] for i in range(5)]
plotImages(images)

# model

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SHAPE, IMG_SHAPE, 3)), # RGB
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')])


model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.summary()

EPOCHS = 50

history = model.fit_generator(
    train_data_gen,steps_per_epoch=int(np.ceil(total_train / float(BATCH_SIZE))),epochs=EPOCHS,test_data=test_data_gen,test_steps=int(np.ceil(total_test / float(BATCH_SIZE)))
    )


# analysis
acc = history.history['accuracy']
test_acc = history.history['test_accuracy']

loss = history.history['loss']
test_loss = history.history['test_loss']

epochs_range = range(EPOCHS)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, test_acc, label='test Accuracy')
plt.legend(loc='lower right')
plt.title('Training and test Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, test_loss, label='test Loss')
plt.legend(loc='upper right')
plt.title('Training and test Loss')
plt.show()