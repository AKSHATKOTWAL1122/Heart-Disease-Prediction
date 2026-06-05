import tensorflow as ts
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle, os

keras.utils.set_random_seed(42)
df = pd.read_csv('http://storage.googleapis.com/download.tensorflow.org/data/heart.csv')
df.head()
df.target.value_counts(normalize=True, dropna= False)
categorical_variables = ['sex', 'cp', 'fbs', 'restecg','exang', 'ca', 'thal']
numeric_variables = ['age', 'trestbps','chol', 'thalach', 'oldpeak', 'slope']
df = pd.get_dummies(df, columns = categorical_variables)
feature_columns = df.drop('target', axis=1).columns.tolist()
df.head()
df.shape

df_test = df.sample(frac = 0.2, random_state = 42)
df_train = df.drop(df_test.index)
scaler = StandardScaler()
df_train[numeric_variables] = scaler.fit_transform(df_train[numeric_variables])
df_test[numeric_variables] = scaler.transform(df_test[numeric_variables])
train = df_train.astype('float32').to_numpy()
test = df_test.astype('float32').to_numpy()
X_train = df_train.drop('target', axis=1).astype('float32').to_numpy()
y_train = df_train['target'].astype('float32').to_numpy()

X_test = df_test.drop('target', axis=1).astype('float32').to_numpy()
y_test = df_test['target'].astype('float32').to_numpy()

input_layer = keras.Input(shape=(X_train.shape[1],))
h = keras.layers.Dense(16, activation="relu", name="Hidden")(input_layer)
output_layer = keras.layers.Dense(1, activation="sigmoid", name="Output")(h)

model = keras.Model(inputs=input_layer, outputs=output_layer)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
# keras.utils.plot_model(model, show_shapes=True)  # requires pydot
model.compile(optimizer = 'adam',
              loss = 'binary_crossentropy',
              metrics = ['accuracy'])


history = model.fit(X_train, y_train, epochs=150, batch_size = 32, validation_split=0.2, verbose = 1)

os.makedirs('artifacts', exist_ok=True)
model.save('artifacts/model.keras')
pickle.dump(scaler, open('artifacts/scaler.pkl', 'wb'))
pickle.dump(feature_columns, open('artifacts/columns.pkl', 'wb'))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(history.history['accuracy'], label='Train')
axes[0].plot(history.history['val_accuracy'], label='Validation')
axes[0].set_title('Accuracy')
axes[0].set_xlabel('Epoch')
axes[0].legend()

axes[1].plot(history.history['loss'], label='Train')
axes[1].plot(history.history['val_loss'], label='Validation')
axes[1].set_title('Loss')
axes[1].set_xlabel('Epoch')
axes[1].legend()

plt.tight_layout()
plt.show()
model.evaluate(X_test, y_test)