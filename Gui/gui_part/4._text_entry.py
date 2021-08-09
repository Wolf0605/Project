from tkinter import*

root = Tk()
root.title("Nado GUI")   
root.geometry("640x480+900+300")  
 
txt = Text(root, width=30, height=5) #텍스트 위젯 만들기. (여러줄 입력 받을때)
txt.pack() 

txt.insert(END, "글자를 입력하세요") #기본값을 미리 제공.  ****Text 에선 END 를 사용*****

e = Entry(root, width = 30)  #Entry 는 한줄 밖에 안됨. (한줄 입력 받을때)
e.pack()
e.insert(0,"한 줄만 입력해요")  #기본값 제공.              ******Entry 에선 0 을 사용******

def btncmd():
    print(txt.get("1.0",END))  #txt 에있는 내용을 가져옴.  1 : 첫번쨰 라인, 0: 0번째 colunm위치. **Text 는 1.0~ END***
    print(e.get())            # get(0,END) 쓰면 오류가 걸림.                                ***Entry 는 ()***

    txt.delete("1.0",END)     # delete   *Text 는 1.0 , END*
    e.delete(0,END)           # delete   *Entry는 0 , END*
btn = Button(root, text="클릭", fg="red",  command = btncmd)
btn.pack()

root.mainloop()