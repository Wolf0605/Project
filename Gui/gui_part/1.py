from tkinter import*

root = Tk()
root.title("Nado GUI")   #title
# root.geometry("640x480")  #가로*세로
root.geometry("640x480+900+300")  #가로*세로 +x좌표 +y좌표

root.resizable(False, False) # x(너비), y(너비) 변경 불가.
btn1 = Button(root, text="버튼1") #버튼 만들기. 
btn1.pack()   #버튼만든거 창에 띄우게하기

btn2 = Button(root, padx=5, pady=10, text="버튼22222222222")   # 버튼은 x축 넓이 , y축 넓이  #넓이가 넓어질 수 있음

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4= Button(root, width =10, height=3, text="버튼4")  #넓이가 넓어질 수 없음. 글자가 짤릴지언정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg= 글씨색  bg = 백그라운드 색 
btn5.pack()

photo = PhotoImage(file=".vscode/basic/img.png")   #gui_basic 에 저장해놓은 img.png를 불러옴
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 눌렸습니다.")

btn7 = Button(root, text="동작하는 버튼", command = btncmd)  #command 에 함수를 넣어서 버튼누르면 텍스트 출력.
btn7.pack()

root.mainloop()