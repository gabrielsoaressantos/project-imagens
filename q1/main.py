import cv2 as cv

img = cv.imread("img.png")
hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)


def find_color(colorName, lowerColor, upperColor):
    mask = cv.inRange(hsvImg, lowerColor, upperColor)
    count_list = sorted(
        cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0],
        key=cv.contourArea,
        reverse=True,
    )[:2]

    if count_list:
        for i in count_list:
            (cx, cy), _ = cv.minEnclosingCircle(i)
            coordinates = (int(cx) - 53, int(cy) + 53)
            font_size = 0.5
            text_color = (0, 0, 0)
            font_weight = 1
            cv.putText(
                img,
                colorName,
                coordinates,
                cv.FONT_HERSHEY_COMPLEX,
                font_size,
                text_color,
                font_weight,
            )


lowerRed = (0, 50, 50)
upperRed = (17, 255, 255)
find_color("VERMELHO", lowerRed, upperRed)

lowerGreen = (30, 50, 50)
upperGreen = (80, 75, 255)
find_color("VERDE", lowerGreen, upperGreen)

cv.imshow("image", img)
cv.waitKey(0)
