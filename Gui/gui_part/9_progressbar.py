import time
import tkinter.ttk as ttk               # Combobox 쓰려면 넣어 줘야함.
from tkinter import*

root = Tk()
root.title("Nado GUI")   
root.geometry("640x480+900+300")  

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")# indeterminate
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")  # determinate
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

def btncmd():
  progressbar.stop() # 작동 중지


btn = Button(root, text="클릭", fg="red",  command = btncmd)
btn.pack()

p_var2 = DoubleVar() # 정수로 올라가는거 뿐만아니라 실수도 반영
progressbar2 = ttk.Progressbar(root, maximum=100, length= 150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i)            # progress bar 의 설정.
        progressbar2.update()    # 값이 차는게 보여짐. (ui 업데이트)
        print(p_var2.get())

btn = Button(root, text="클릭", fg="red",  command = btncmd2)
btn.pack()

root.mainloop()