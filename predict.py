import cv2
import numpy as np

def predict_image(img_path):

    img = cv2.imread(img_path)

    img = cv2.resize(img, (256, 256))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

    noise = np.std(gray)

    edges = cv2.Canny(gray, 100, 200)

    edge_density = np.sum(edges > 0) / edges.size

    fft = np.fft.fft2(gray)

    fft_shift = np.fft.fftshift(fft)

    magnitude = 20 * np.log(np.abs(fft_shift) + 1)

    frequency_score = np.mean(magnitude)

    print("Sharpness:", sharpness)
    print("Noise:", noise)
    print("Edge Density:", edge_density)
    print("Frequency Score:", frequency_score)

    ai_score = 0

    if sharpness < 300:
        ai_score += 1

    if noise < 70:
        ai_score += 1

    if edge_density < 0.1:
        ai_score += 1

    if frequency_score < 140:
        ai_score += 1

    print("AI Score:", ai_score)

    if ai_score >= 2:
        prediction = "AI Generated"
    else:
        prediction = "Real Image"

    confidence = 60 + (ai_score * 10)

    return prediction, confidence
