from tensorflow.contrib.saved_model import load_keras_model

new_model = load_keras_model("models/model_weigth.h5")
new_model.summary()