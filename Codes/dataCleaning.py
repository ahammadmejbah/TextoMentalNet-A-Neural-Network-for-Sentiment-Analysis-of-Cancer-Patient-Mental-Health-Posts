import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

texts = mental_health_data['posts'].astype(str)
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
data = pad_sequences(sequences, maxlen=200)

label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(mental_health_data['predicted'])
labels = to_categorical(integer_encoded)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
