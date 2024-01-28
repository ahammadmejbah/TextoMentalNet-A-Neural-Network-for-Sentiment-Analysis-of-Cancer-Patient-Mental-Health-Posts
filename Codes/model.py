from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional

embedding_dim = 100
max_words = 5000
max_sequence_length = 200
lstm_units = 64
dense_units = 256
dropout_rate = 0.5
num_classes = 4  

def add_lstm_layers(model, num_layers, lstm_units, return_sequences=True):
    for i in range(num_layers):
        if i == num_layers - 1:  
            return_sequences = False
        model.add(Bidirectional(LSTM(lstm_units, return_sequences=return_sequences)))
        model.add(Dropout(dropout_rate))


def add_dense_layers(model, num_layers, dense_units):
    for _ in range(num_layers):
        model.add(Dense(dense_units, activation='relu'))
        model.add(Dropout(dropout_rate))


model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=max_sequence_length))
add_lstm_layers(model, num_layers=10, lstm_units=lstm_units)
add_dense_layers(model, num_layers=9, dense_units=dense_units)
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
