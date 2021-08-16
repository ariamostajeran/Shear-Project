from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np


def get_image():
    user_input = input()
    image_data = image.imread(user_input)

    print(image_data.shape)
    return image_data


if __name__ == '__main__':
    img_data = get_image()

    new_img = [[(255, 255, 255) for x in range(img_data.shape[1])] for i in range(img_data.shape[0] + 100)]
    for i in range(img_data.shape[0]):
        for j in range(img_data.shape[1]):
            try:
                new_img[i][j+int(img_data.shape[0] / 14)] = img_data[i][int(i*0.06) + j]
            except:
                pass
    new_img2 = [[(255, 255, 255) for x in range(img_data.shape[1])] for i in range(img_data.shape[0] + 100)]

    for i in range(img_data.shape[0]):
        for j in range(img_data.shape[1]):
            if np.all(img_data[i][j] > 230):
                if np.any(np.array(new_img[i][j]) < 230):
                    new_img2[i][j] = np.array((250, 218, 221))
            else:
                new_img2[i][j] = img_data[i][j]
    plt.imshow(new_img2)

    plt.show()
