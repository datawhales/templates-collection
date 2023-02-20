import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import StandardScaler


def load_data():
    fashion_mnist = tf.keras.datasets.fashion_mnist

    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    return (train_images, train_labels), (test_images, test_labels)


def preprocessing(train_images, test_images):
    scaler = StandardScaler()

    # Shape 변환: (60000, 28, 28) -> (60000, 784)
    train_images = train_images.reshape(train_images.shape[0], -1)
    test_images = test_images.reshape(test_images.shape[0], -1)

    train_images = scaler.fit_transform(train_images)
    test_images = scaler.transform(test_images)

    # Shape 원래대로 다시 변환
    train_images = train_images.reshape(train_images.shape[0], 28, 28)
    test_images = test_images.reshape(test_images.shape[0], 28, 28)

    return train_images, test_images


def train(train_images, train_labels, n_epochs=10):
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10),
    ])

    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )

    model.fit(train_images, train_labels, epochs=n_epochs)
    return model


def evaluate(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

    print(f"\nTest Accuracy: {test_acc:.4f}")


def inference(model, test_image):
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

    plt.figure(figsize=(5, 5))
    plt.imshow(test_image)
    plt.colorbar()
    plt.grid(False)
    plt.show()
    
    test_image = np.expand_dims(test_image, axis=0)
    pred = probability_model.predict(test_image)

    return class_names[np.argmax(pred)]


def main():
    (train_images, train_labels), (test_images, test_labels) = load_data()
    
    train_images, test_images = preprocessing(train_images, test_images)

    model = train(train_images, train_labels)

    evaluate(model, test_images, test_labels)

    print("Example")
    print(inference(model, test_images[10]))


if __name__ == "__main__":
    main()
