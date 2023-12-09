import sys
import cv2
import glob
import os

image_path = os.path.dirname(os.path.abspath(__file__))
video_name = "demo.wmv"

def image_load(image_path):

    img_array = []

    for filename in sorted(glob.glob(os.path.join(image_path, "image/*.png"))):
        img = cv2.imread(filename)
        img = cv2.resize(img, dsize=(600, 600), interpolation=cv2.INTER_LINEAR)
        h, w, channels = img.shape
        size = (h, w)
        img_array.append(img)

    return size, img_array


def video_generator(folder_path, file_name, size, fps, img_array):

    out = cv2.VideoWriter(filename=os.path.join(folder_path, file_name), fourcc=cv2.VideoWriter_fourcc('M','P','4','3'), fps=fps, frameSize=size)
    for img in img_array:
        out.write(img)

    out.release()

def video_play(file_name):
    cap = cv2.VideoCapture(file_name)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not (ret):  # 프레임정보를 정상적으로 읽지 못하면
            break
        color = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        cv2.imshow("frame", color)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    img_size, img_array = image_load(image_path)
    video_generator(folder_path= image_path, file_name=video_name, size=img_size, fps=20, img_array=img_array)
    video_play(file_name=video_name)



