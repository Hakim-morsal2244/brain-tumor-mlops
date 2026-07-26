import numpy as np
from tensorflow.keras.utils import load_img, img_to_array


IMG_SIZE = (224, 224)


def preprocess_image(image_path):

    img = load_img(
        image_path,
        target_size=IMG_SIZE
    )

    img_array = img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    return img_array