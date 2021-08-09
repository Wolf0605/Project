import tkinter.ttk as ttk               # Combobox 쓰려면 넣어 줘야함.
from tkinter import*

root = Tk()
root.title("Nado GUI")   
root.geometry("640x480+900+300")  

values = [str(i) + "일" for i in range(1,32)]  #1 ~ 31 
combobox = ttk.Combobox(root, height = 5, values=values )  # height = 5 로  목록 5개만 보여줌
combobox.pack()
combobox.set("카드 결제일")  #최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height = 10, values=values , state ="readonly" )  # height = 10 목록 10개 
readonly_combobox.current(0) # 0번째 인덱스 값 선택                                       #+ 직접 수정 안됨. readonly
readonly_combobox.pack()


def btncmd():
   print(combobox.get())
   print(readonly_combobox.get())
btn = Button(root, text="클릭", fg="red",  command = btncmd)
btn.pack()

root.mainloop()