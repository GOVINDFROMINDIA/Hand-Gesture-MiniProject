import tkinter as tk
from PIL import ImageTk, Image
from keras.models import load_model
import cv2
import numpy as np
import k
import v
import s
import threading

def run_tkinter():
    root = tk.Tk()
    root.title("System Controls")
    root.geometry("550x680")
    img = Image.open("bg.png")
    bg_img = ImageTk.PhotoImage(img)
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.mainloop()

def run_camera():
    np.set_printoptions(suppress=True)
    model = load_model("keras_Model.h5", compile=False)
    class_names = open("labels.txt", "r").readlines()
    camera = cv2.VideoCapture(0)

    run_camera_loop = True

    while run_camera_loop:
        ret, image = camera.read()
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        cv2.imshow("Webcam Image", image)

        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1

        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        if index == 0 and confidence_score >= 0.7:
            print("VOLUME")
            v.run_volume_control()
            run_camera_loop = False
        elif index == 1 and confidence_score >= 0.7:
            print("KEYBOARD")
            k.run_keyboard_input()
            run_camera_loop = False
        elif index == 2 and confidence_score >= 0.7:
            print("BRIGHTNESS")
            s.run_brightness_control()
            run_camera_loop = False
        elif index == 3 and confidence_score >= 0.7:
            run_camera_loop = False
            break

        keyboard_input = cv2.waitKey(1)

        if keyboard_input == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

    if run_camera_loop:
        run_camera()

thread_tkinter = threading.Thread(target=run_tkinter)
thread_camera = threading.Thread(target=run_camera)

thread_tkinter.start()
thread_camera.start()

thread_tkinter.join()
thread_camera.join()
