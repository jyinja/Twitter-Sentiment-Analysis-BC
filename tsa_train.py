#Create a Neural Network
#Create the model (experimental) by JY
from tensorflow import keras
import nltk
def train(X_train_mod, y_train, features, shuffle, drop, layer1, layer2, epoch, lr, epsilon, validation):
    model_nn = Sequential()
    model_nn.add(Dense(layer1, input_shape=(features,), activation='relu'))
    model_nn.add(Dropout(drop))
    model_nn.add(Dense(layer2, activation='sigmoid'))
    model_nn.add(Dropout(drop))
    model_nn.add(Dense(3, activation='softmax'))

    optimizer = keras.optimizers.Adam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=epsilon, decay=0.0, amsgrad=False)
    model_nn.compile(loss='sparse_categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])
    model_nn.fit(np.array(X_train_mod), y_train,batch_size=32,epochs=epoch,verbose=1,validation_split=validation,shuffle=shuffle)
    return model_nn
