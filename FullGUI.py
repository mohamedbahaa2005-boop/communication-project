from tkinter import * 
from tkinter import filedialog
from tkinter import *
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

def double_func():
    submit()
    excute()

def excute():

    loud = louder(data, 1.5)
    high = pitch_shift(data, 1.3)
    sf.write('loud.wav', loud.astype(np.float32), rate)
    sf.write('high_pitch.wav', high.astype(np.float32), rate)
    plt.figure(figsize=(10, 6))

    t = np.arange(rate*2) / rate

    plt.subplot(3,1,1)
    plt.plot(t, data[:rate*2])
    plt.title('Original')

    plt.subplot(3,1,2)
    plt.plot(t, loud[:rate*2])
    plt.title('Louder')

    plt.subplot(3,1,3)
    plt.plot(t, high[:rate*2])
    plt.title('Higher Pitch')

    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()

print("Files saved: loud.wav, high_pitch.wav, plot.png")

def pitch_shift(audio, amount):
      fft = np.fft.fft(audio)
      n = len(fft)
      new = np.zeros(n, dtype=complex)

      for i in range(n//2):
          new_i = int(i * amount)
          if new_i < n//2:
             new[new_i] = fft[i]

          return np.fft.ifft(new).real


def louder(audio, amount):
      fft = np.fft.fft(audio)
      fft = fft * amount
      return np.fft.ifft(fft).real

def submit():
    global loude_amount
    global pitch_amount
    loude_amount = amplitude_scale.get()
    pitch_amount = pitch_scale.get()
    amplitude_scale.config(state="disabled")
    pitch_scale.config(state="disabled")
    amplitude_value.config(
        text=f"your amplitude = {loude_amount}"
    )
    pitch_value.config(
        text=f"your pitch = {pitch_amount}"
    )
    amplitude_value.place(x=250,y=10)
    pitch_value.place(x=250,y=180)

    loud = louder(data, 1.5)
    high = pitch_shift(data, 1.3)
    
def reScale():
    loude_amount = 0
    pitch_amount = 0
    amplitude_scale.config(state="normal")
    pitch_scale.config(state="normal")

    amplitude_value.place_forget()
    pitch_value.place_forget()


def next():
    global amplitude_scale, pitch_scale, amplitude_value, pitch_value
    slider_window = Tk()
    slider_window.geometry("700x420")
    amplitude = Label(slider_window,text='amplitude:',
              font=('Arial',20,'bold'))
    pitch  = Label(slider_window,text='pitch:',
              font=('Arial',20,'bold'))
    amplitude_value= Label(slider_window,text='your amplitude =',
              font=('Arial',10))
    pitch_value = Label(slider_window,text='your pitch =',
              font=('Arial',10))
    amplitude_scale = Scale(slider_window,from_=0,
              to=2,
              length=650,
              orient=HORIZONTAL, #orientation of scale 
              font = ('consolas',20),
              tickinterval=0.5,
                resolution=0.01 #add numeric indicators 
              )
    pitch_scale = Scale(slider_window,from_=0.5,
              to=2,
              length=650,
              orient=HORIZONTAL, #orientation of scale 
              font = ('consolas',20),
              tickinterval=0.5, #add numeric indicators
                resolution=0.01 
              )
    submit_button = Button(slider_window,text='Submit',command=double_func)
    reScale_button = Button(slider_window,text='Rescale',command=reScale)
    submit_button.config(font=('Arial',10,'bold'),
              activeforeground='#2b2828',
              activebackground='grey',
              )
    reScale_button.config(font=('Arial',10,'bold'),
              activeforeground='#2b2828',
              activebackground='grey',
              )
    amplitude.place(x=0,y=0)
    pitch.place(x=0,y=175)
    amplitude_scale.place(x=0,y=45)
    pitch_scale.place(x=0,y=220)
    submit_button.place(x=275,y=375) #y=375 x=310
    reScale_button.place(x=345,y=375)
    fileUploud_window.destroy()

def openFile():
    # Open file dialog to select an MP3
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])

    # Convert to WAV
   # audio = AudioSegment.from_mp3(file_path)
   # wav_name = 'converted_audio.wav'
   # audio.export(wav_name, format='wav')
   # print("Conversion done!")

    global rate, data

    # Read WAV
    data, rate = sf.read(file_path)
    if len(data.shape) == 2:
        data = data.mean(axis=1)
        data = data.astype(float)
        Duration = f"Duration: {len(data)/rate:.1f} seconds"

    Duration_lable = Label(fileUploud_window,text=Duration,
              font=('Arial',10,'bold'))
    print("WAV loaded!")
    print("Sample rate:", rate)
    print("Data shape:", data.shape)
    next_button.config(state="normal")
    Duration_lable.place(x=40,y=100)


def real():
    global next_button, fileUploud_window
    fileUploud_window = Tk()
    fileUploud_window.geometry("700x420")
    openFile_button = Button(fileUploud_window,text="open",command=openFile)
    next_button = Button(fileUploud_window, text="Next-->",command=next)
    label1 = Label(fileUploud_window,text='Choose your file:',
              font=('Arial',20,'bold'))
    openFile_button.config(font=('Arial',12,'bold'),
              activeforeground='#2b2828',
              activebackground='grey',
              )
    next_button.config(font=('Arial',12,'bold'),
              activeforeground='#2b2828',
              activebackground='grey',
              )
    openFile_button.place(x=260,y=12)
    next_button.place(x=310,y=350)
    label1.place(x=10,y=10)
    next_button.config(state="disabled")
    main_window.destroy()

def goofy():
    goofy_window = Tk()
    goofy_window.geometry("1000x220")
    goofy1= Label(goofy_window,text='I dont know man remember we are \n "LOST IN SYNC"',
              font=('Arial',40,'bold')).pack()
    goofy1= Label(goofy_window,text='So we cant tell the time',
              font=('Arial',10,'bold')).pack()
    main_window.destroy()



main_window = Tk() 

main_window.geometry("700x420")

lable3= Label(main_window,text='Welcome to Lost in Sync \n program',
              font=('Arial',40,'bold')).pack()


button_real = Button(text="Audio Signal Analysis",command=real)
button_gofy = Button(text="what was the time ?!!",command=goofy)

button_real.config(font=('Arial',30,'bold'),
              activeforeground='#2b2828',
              activebackground='grey',
              padx=5,
              pady=10
              )
button_gofy.config(font=('Arial',30,'bold'),
              activeforeground='#2b2828',
              activebackground='grey',
              padx=5,
              pady=10
              )

button_real.place(x=120,y=175)
button_gofy.place(x=120,y=300)

main_window.mainloop() 