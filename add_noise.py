import numpy as np
import random
import cv2
import glob

def gaussian_noise(img):
    mean = 0
    var = 110
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (img.shape[0],img.shape[1]))

    noisy_image = np.zeros(img.shape, np.float32)
    noisy_image[:, :, 0] = img[:, :, 0] + gaussian
    noisy_image[:, :, 1] = img[:, :, 1] + gaussian
    noisy_image[:, :, 2] = img[:, :, 2] + gaussian
    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def blur(img):
    kernel = np.ones((6, 6), np.float32) / 36
    #kernel = np.ones((6, 6), np.float32) / 36 - naver style Original
    #kernel = np.ones((5, 5), np.float32) / 25 - sharpness
    dst = cv2.filter2D(img, -1, kernel)
    return dst

def main():
    image = cv2.imread('padded_img.png',0) # Only for grayscale image
    noise_img = sp_noise(image,0.3)
    cv2.imwrite('sp_noise.jpg', noise_img)

if __name__ == "__main__":
    main()
