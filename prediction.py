from tkinter import *
from tkinter import filedialog
import numpy as np
from keras.models import load_model
from tkinter import messagebox
import os

window=Tk()
window.geometry("400x150")

def file_open():
    global filepath
    file= filedialog.askopenfile(mode='r', filetypes=[('PhotoImage','*jpg')])
    if file:
        filepath=os.path.abspath(file.name)
        
def predict():
    import tensorflow as tf
    image = tf.keras.utils.load_img(filepath, target_size=(28,28), grayscale=True, color_mode='grayscale')
    input_arr = tf.keras.utils.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    res = model.predict(input_arr)
    if res[0][0]==1:
        predictions='0'
    elif res[0][1]==1:
        predictions='1'
    elif res[0][2]==1:
        predictions='2'
    elif res[0][3]==1:
        predictions='3'
    elif res[0][4]==1:
        predictions='4'
    elif res[0][5]==1:
        predictions='5'
    elif res[0][6]==1:
        predictions='6'
    elif res[0][7]==1:
        predictions='7'
    elif res[0][8]==1:
        predictions='8'
    elif res[0][9]==1:
        predictions='9'
    lab2=Label(window, text='Prediciton is: ',width=10)
    lab2.place(x=10,y=50)
    res_label= Label(window, text=predictions, width=3)
    res_label.place(x=80,y=50)

model=load_model('model.h5')

lab=Label(window, text='Select image for prediciton: ',width=20)
lab.place(x=5,y=10)

select_button=Button(window, text='select', command=file_open,width=10)
select_button.place(x=180,y=5)

predict_button= Button(window, text='Predict',command=predict,width=10)
predict_button.place(x=280,y=5)

window.mainloop()