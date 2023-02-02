from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from utils import CvFpsCalc, ResetData
import os
import csv
dataset = 'sp_model/keypoint.csv'
model_save_path = 'sp_model/keypoint_classifier.hdf5'
tflite_save_path = 'sp_model/keypoint_classifier.tflite'
# Read setting.csv to get NUM_CLASSES
with open('setting.csv',
          encoding='utf-8-sig') as f:
    custum_setting = csv.reader(f)
    data = [i for i in custum_setting]
    n = int(data[0][0])

RANDOM_SEED = 42
NUM_CLASSES = n  # accroding to how many gestures , setting by user

X_dataset = np.loadtxt(dataset, delimiter=',',
                       dtype='float32', usecols=list(range(1, (21 * 2) + 1)))
y_dataset = np.loadtxt(dataset, delimiter=',', dtype='int32', usecols=(0))
X_train, X_test, y_train, y_test = train_test_split(
    X_dataset, y_dataset, train_size=0.75, random_state=RANDOM_SEED)

model = tf.keras.models.Sequential([
    tf.keras.layers.Input((21 * 2, )),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
])

model.summary()  # tf.keras.utils.plot_model(model, show_shapes=True)
# Model checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    model_save_path, verbose=1, save_weights_only=False)
# Callback for early stopping
es_callback = tf.keras.callbacks.EarlyStopping(patience=20, verbose=1)
# Model compilation
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
# Model compilation
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
# Model evaluation
val_loss, val_acc = model.evaluate(X_test, y_test, batch_size=128)
# Loading the saved model
model = tf.keras.models.load_model(model_save_path)
# Inference test
predict_result = model.predict(np.array([X_test[0]]))
print(np.squeeze(predict_result))
print(np.argmax(np.squeeze(predict_result)))


def print_confusion_matrix(y_true, y_pred, report=True):
    labels = sorted(list(set(y_true)))
    cmx_data = confusion_matrix(y_true, y_pred, labels=labels)

    df_cmx = pd.DataFrame(cmx_data, index=labels, columns=labels)

    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(df_cmx, annot=True, fmt='g', square=False)
    ax.set_ylim(len(set(y_true)), 0)
    plt.show()

    # if report:
    #     print('Classification Report')
    #     print(classification_report(y_test, y_pred))


Y_pred = model.predict(X_test)
y_pred = np.argmax(Y_pred, axis=1)

# print_confusion_matrix(y_test, y_pred)
# Save as a model dedicated to inference
model.save(model_save_path, include_optimizer=False)
# Transform model (quantization)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quantized_model = converter.convert()

open(tflite_save_path, 'wb').write(tflite_quantized_model)


ResetData.reset_setting()  # 關閉前清除使用者設定的手數量、鏡頭編號
print('訓練筆數快存刪除成功')
success = os.system("python success_msg.py")
success

exit()
