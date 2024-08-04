#Kütüphanelerin yüklenmesi
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#Eğitim setinin ön işlemesi
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
training_set=train_datagen.flow_from_directory('C:\\Users\\enesb\\OneDrive\\Masaüstü\\archive\\training_set\\training_set',target_size=(64,64),batch_size=32,class_mode='binary')
#Test setinin ön işlemesi
test_datagen=ImageDataGenerator(rescale=1./25)
test_set=test_datagen.flow_from_directory('C:\\Users\\enesb\\OneDrive\\Masaüstü\\archive\\test_set\\test_set',target_size=(64,64),batch_size=32,class_mode='binary')
#yapay sinir ağı modeli oluşturuldu
cnn=tf.keras.models.Sequential()
#Convulation
cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu',input_shape=[64,64,3]))
#Pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
#İkinci convulation katmanı
cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
#Flattening
cnn.add(tf.keras.layers.Flatten())
#Full Connection(yapay sinir ağındaki gizli katmanlar ve norönları oluşturduk)
cnn.add(tf.keras.layers.Dense(units=128,activation='relu'))
#Çıkış katmanı
cnn.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))
#Derleme işlemi
cnn.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#Eğitim işlemi
cnn.fit(x=training_set,validation_data=test_set,epochs=50)
#Tahmin oluşturmak
import numpy as np
from keras.preprocessing import image
test_image=image.load_img('C:\\Users\\enesb\\OneDrive\\Masaüstü\\archive\\kopekler.jpg',target_size=(64,64))
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=cnn.predict(test_image)
training_set.class_indices
if result[0][0]==1:
    prediction='dog'
else:
    prediction='cat'
print(prediction)