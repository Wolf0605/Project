from tkinter import*

root = Tk()
root.title("Nado GUI")   #title
# root.geometry("640x480")  #가로*세로
root.geometry("640x480+900+300")  #가로*세로 +x좌표 +y좌표

root.resizable(False, False) # x(너비), y(너비) 변경 불가.

label1 = Label(root, text="Hi")   # label 
label1.pack()

photo = PhotoImage(file="313.png")
label2 = Label(root, image = photo)
label2.pack()
def change():
    label1.config(text="또만나요")  # config  label1에 있던 라벨을 바꿔줌.
    global photo2     #바꿀때 photo 값만 전역 변수로 바꿔줌. 안그러면 오류 생김.
    photo2 = PhotoImage(file = ".vscode/basic/img.png") 
    label2.config(image = photo2)
    
btn = Button(root, text="클릭", command = change)
btn.pack()

root.mainloop()