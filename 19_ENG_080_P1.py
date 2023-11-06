import cv2
import numpy as np
import random

# Global variables
label_array = []
label_conversion = {}


# Binarize the image
def binarize_image(image_array, threshold=130):
    binary_image = np.zeros_like(image_array)
    binary_image[image_array > threshold] = 1
    return binary_image


# Colorize the labeled regions
def colorize_labeled_regions(labeled_image):
    rows, columns = labeled_image.shape
    label_colors = {0: (0, 0, 0)}
    colored_image = np.zeros((rows, columns, 3), dtype=np.uint8)

    for i in range(rows):
        for j in range(columns):
            label = labeled_image[i, j]
            if label not in label_colors:
                label_colors[label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            colored_image[i, j, :] = label_colors[label]

    return colored_image


# Assign labels to connected components using the two-pass algorithm
def two_pass_labeling(binary_image):
    rows, columns = binary_image.shape

    for i in range(rows):
        for j in range(columns):
            if binary_image[i, j] == 1:
                if i == 0 and j == 0:
                    binary_image[i, j] = assign_label([])

                elif i == 0 and j > 0:
                    binary_image[i, j] = assign_label([binary_image[i, j - 1]])
                else:
                    binary_image[i, j] = assign_label([binary_image[i - 1, j], binary_image[i, j - 1]])

    for key in label_conversion:
        for i in range(rows):
            for j in range(columns):
                if binary_image[i][j] in label_conversion:
                    binary_image[i][j] = label_conversion[binary_image[i][j]]

    return binary_image


# Determine the label for a pixel based on its neighbors
def assign_label(neighbor_pixels):
    if all(x == 0 for x in neighbor_pixels):
        if not label_array:
            label_array.append(1)
            return max(label_array)
        else:
            label_array.append(max(label_array) + 1)
            return max(label_array)
    else:
        neighbor_pixels = [x for x in neighbor_pixels if x != 0]
        neighbor_pixels.sort()

        min_value = neighbor_pixels[0]
        max_value = neighbor_pixels[-1]

        if max_value == min_value:
            return min_value
        else:
            label_conversion[max_value] = min_value
            return min_value

def main():
    # Load the image using OpenCV. Replace "your_image.jpg" with the path to your image.
    image = cv2.imread("input_images/Sample Image 1.bmp", cv2.IMREAD_GRAYSCALE)

    # Add borders to the image
    # image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=255)

    # Binarize the image
    binary_image = binarize_image(image)

    labeled_image = two_pass_labeling(binary_image)
    colored_image = colorize_labeled_regions(labeled_image)

    cv2.imshow("Output Colorized Image", colored_image)

    # Save the output image
    cv2.imwrite("output_images/Output_Colorized_Image.jpg", colored_image)
    print("\nOutput image is saved in 'Output_Colorized_Image.jpg'")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
