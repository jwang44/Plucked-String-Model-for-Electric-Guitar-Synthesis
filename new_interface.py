import pluck
import tkinter as tk
import pyaudio
'''
single pluck button, with bend and dist
'''
p = pyaudio.PyAudio()
# def callback(in_data, frame_count, time_info, status):
#     return in_data, pyaudio.paContinue
stream = p.open(format=p.get_format_from_width(2),
                channels=1,
                rate=44100,
                output=True)

window = tk.Tk()
frame_border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

dist_bool = tk.BooleanVar()
bend_bool = tk.BooleanVar()
frame = tk.Frame(relief=tk.GROOVE, borderwidth=5)
label = tk.Label(master=frame,text="Hello GuitarDemo",fg="white",bg="black",width=25,height=2)

dist_check = tk.Checkbutton(frame, text='distortion', variable=dist_bool)
bend_check = tk.Checkbutton(frame, text='bend', variable=bend_bool)
freq_scale = tk.Scale(master=frame, from_=82, to=440, orient=tk.HORIZONTAL, label='freq', length=425)
tone_scale = tk.Scale(master=frame, from_=10, to=100, orient=tk.HORIZONTAL, label='tone', length=425, showvalue=0)
gain_scale = tk.Scale(master=frame, from_=1, to=100, orient=tk.HORIZONTAL, label='gain', length=425, showvalue=0)
freq2_scale = tk.Scale(master=frame, from_=82, to=440, orient=tk.HORIZONTAL, label='bend to', length=425)

pluck_btn = tk.Button(
    master=frame,text="pluck",width=25,height=3,
    command=lambda: stream.write(
        pluck.pluck_note(
            freq=freq_scale.get(), 
            tone=tone_scale.get(), 
            dist=dist_bool.get(),
            gain=gain_scale.get(),
            bend=bend_bool.get(),
            bend_to=freq2_scale.get()
            )
        )
    )

label.pack()
pluck_btn.pack()

dist_check.pack()
bend_check.pack()
freq_scale.pack()
tone_scale.pack()
gain_scale.pack()
freq2_scale.pack()
frame.pack()
window.mainloop()

stream.stop_stream()
stream.close()
p.terminate()
print("closed")
