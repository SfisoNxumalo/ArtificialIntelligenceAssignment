import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
import random
import re

from Data.data import training_labels, training_sentences

# ---- 2) LABEL ENCODING (stable order) ----
# We convert the text labels (like 'greeting', 'farewell') into numbers the model can learn
# label_set gets all unique labels so we know all the possible classes
# label_index maps each label to a unique number (e.g., 'greeting' -> 0)
# y_train turns our original training_labels into numeric form using that mapping
# This is what the model will actually try to predict during training
labels = sorted(set(training_labels))
label_to_index = {l:i for i,l in enumerate(labels)}
y_train = np.array([label_to_index[l] for l in training_labels], dtype=np.int32)

# ---- 3) TEXT VECTORIZATION with OOV ----
# Here we turn all our training sentences into numbers the model can understand
# Tokenizer reads all the sentences and makes a vocab list
# oov_token="<OOV>" makes sure words the model hasn't seen get a placeholder instead of breaking things
# texts_to_matrix with mode="binary" converts each sentence into a vector where each position is 1 if the word exists, 0 if not
# This gives us fixed-size input vectors ready for the neural network
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(training_sentences)
X_train = tokenizer.texts_to_matrix(training_sentences, mode="binary")  # multi-hot BoW with OOV bucket

# ---- 4) MODEL ----
# Build a neural network that will learn which intent a sentence belongs to
# Layers: input Dense (32 neurons) -> Dropout 30% -> Dense 32 -> Output Dense with softmax for label probabilities
# Compile with adam optimizer and sparse categorical crossentropy loss
# Train on X_train and y_train for 400 epochs
model = Sequential([
    Dense(26, input_shape=(X_train.shape[1],), activation="relu"),
    Dropout(0.2),
    Dense(26, activation="relu"),
    Dense(len(labels), activation="softmax")
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=200, verbose=1)


if __name__ == "__main__":
    print("1Nebula Chatbot ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "quit":
            break
        print("Bot:", "Hellow")