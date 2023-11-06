import cv2
import numpy as np

# Read the binary image
binary_image = cv2.imread('input_images/d.JPG', cv2.IMREAD_GRAYSCALE)

def two_pass_labeling(image):
    height, width = image.shape
    labels = np.zeros_like(image, dtype=np.int32)
    current_label = 1
    label_equivalency = {}

    def get_label_equivalent(label):
        if label not in label_equivalency:
            return label
        return get_label_equivalent(label_equivalency[label])

    # First pass
    for y in range(height):
        for x in range(width):
            if image[y, x] == 255:
                neighbors = []
                if x > 0:
                    left = labels[y, x - 1]
                    if left > 0:
                        neighbors.append(left)
                if y > 0:
                    above = labels[y - 1, x]
                    if above > 0:
                        neighbors.append(above)

                if not neighbors:
                    labels[y, x] = current_label
                    current_label += 1
                else:
                    min_neighbor = min(neighbors)
                    labels[y, x] = min_neighbor
                    for neighbor in neighbors:
                        if neighbor != min_neighbor:
                            label_equivalency[neighbor] = min_neighbor

    # Second pass
    for y in range(height):
        for x in range(width):
            if labels[y, x] > 0:
                labels[y, x] = get_label_equivalent(labels[y, x])

    return labels, current_label

labels, num_labels = two_pass_labeling(binary_image)

# Create a random color map for labeling each component
color_map = np.random.randint(0, 256, size=(num_labels, 3), dtype=np.uint8)

# Create a colored image
colored_image = np.zeros((binary_image.shape[0], binary_image.shape[1], 3), dtype=np.uint8)

# Color each component with a different color
for label in range(1, num_labels):
    colored_image[labels == label] = color_map[label]

# Save the colored image
cv2.imwrite('output_images/colored_image.jpg', colored_image)

# Display the colored image
cv2.imshow('Colored Image', colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
