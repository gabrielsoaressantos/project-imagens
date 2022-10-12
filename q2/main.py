import cv2 as cv

video_cap = cv.VideoCapture(0)
frame_width = int(video_cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc("X", "V", "I", "D")
out = cv.VideoWriter("output.avi", fourcc, 5.8, (1288, 720))

_, frame1 = video_cap.read()
_, frame2 = video_cap.read()

while video_cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)

        if cv.contourArea(contour) < 900:
            continue

        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    image = cv.resize(frame1, (1280, 720))
    out.write(image)

    window_name = "Detecta objeto"
    cv.imshow(window_name, frame1)
    frame1 = frame2
    _, frame2 = video_cap.read()

    cv.waitKey(40)
    window_opened = cv.getWindowProperty(window_name, cv.WND_PROP_VISIBLE) == 1
    if not window_opened:
        break

cv.destroyAllWindows()
video_cap.release()
out.release()
