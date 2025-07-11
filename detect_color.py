import cv2
import numpy as np

# مسار الفيديو
video_path = r"C:\Users\wedad\OneDrive\Desktop\task2-artificial-inteligence\.dist\fruitColor.mp4"
cap = cv2.VideoCapture(video_path)

# تعريف نطاقات الألوان لكل فاكهة في HSV
color_ranges = {
    "Orange(Orange)": [((10, 100, 100), (25, 255, 255))],
    "Red (Red Apple)": [((0, 120, 70), (10, 255, 255)), ((160, 120, 70), (179, 255, 255))],
    "Yellow(Lemon)": [((25, 100, 100), (35, 255, 255))]
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (400, 400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detected_color = "Unknown"
    max_pixels = 0

    # تحليل كامل الإطار لأن الخلفية سوداء (مافي تشويش)
    for fruit, ranges in color_ranges.items():
        mask_total = None
        for lower, upper in ranges:
            mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
            if mask_total is None:
                mask_total = mask
            else:
                mask_total = cv2.bitwise_or(mask_total, mask)

        pixels_count = cv2.countNonZero(mask_total)

        if pixels_count > max_pixels:
            max_pixels = pixels_count
            detected_color = fruit

    cv2.putText(frame, f"Fruit: {detected_color}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Fruit Detection", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
