import pluck
import tkinter as tk
import pyaudio

# simple tk interface, depends on pluck.py

p = pyaudio.PyAudio()
# def callback(in_data, frame_count, time_info, status):
#     return in_data, pyaudio.paContinue

# open pyaudio stream
stream = p.open(format=p.get_format_from_width(2),
                channels=1,
                rate=44100,
                output=True)

# start interface
window = tk.Tk()

# bool parameters for checkboxes
fb_bool = tk.BooleanVar()
bend_bool = tk.BooleanVar()

frame = tk.Frame(relief=tk.GROOVE, borderwidth=5)
label = tk.Label(master=frame,text="Hello GuitarDemo",fg="white",bg="black",width=25,height=2)

fb_check = tk.Checkbutton(frame, text='feedback', variable=fb_bool)
bend_check = tk.Checkbutton(frame, text='bend', variable=bend_bool)

freq_scale = tk.Scale(master=frame, from_=82, to=440, orient=tk.HORIZONTAL, label='freq', length=425)
dur_scale = tk.Scale(master=frame, from_=300, to=800, orient=tk.HORIZONTAL, label='dur', length=425, showvalue=0)
tone_scale = tk.Scale(master=frame, from_=0, to=100, orient=tk.HORIZONTAL, label='tone', length=425, showvalue=0)
gain_scale = tk.Scale(master=frame, from_=1, to=20, orient=tk.HORIZONTAL, label='gain', length=425, showvalue=0)
freq2_scale = tk.Scale(master=frame, from_=82, to=440, orient=tk.HORIZONTAL, label='bend to', length=425)

pluck_btn = tk.Button(
    master=frame,text="pluck",width=25,height=3,
    command=lambda: stream.write(
        pluck.pluck(
            freq=freq_scale.get(), 
            dur=dur_scale.get()/100,
            tone=tone_scale.get(),
            gain=gain_scale.get(),
            bend=bend_bool.get(),
            bend_to=freq2_scale.get(),
            feedback=fb_bool.get()
            )
        )
    )

chord_btn = tk.Button(
    master=frame,text="pluck chord",width=25,height=3,
    command=lambda: stream.write(
        pluck.pluck_chord(
            freq=freq_scale.get(), 
            dur=dur_scale.get()/100,
            tone=tone_scale.get(),
            gain=gain_scale.get(),
            bend=bend_bool.get(),
            bend_to=freq2_scale.get(),
            feedback=fb_bool.get()
            )
        )
    )

label.pack()
pluck_btn.pack()
chord_btn.pack()

fb_check.pack()
bend_check.pack()
freq_scale.pack()
dur_scale.pack()
tone_scale.pack()
gain_scale.pack()
freq2_scale.pack()

frame.pack()
window.mainloop()

stream.stop_stream()
stream.close()
p.terminate()
#print("closed")
