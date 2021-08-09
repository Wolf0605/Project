from tkinter import*

root = Tk()
root.title("Nado GUI")   
root.geometry("640x480+900+300")  
 
listbox = Listbox(root, selectmode="extended", height=0)  # extended = 다중 선택 가능 , single = 하나만 선택 가능
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")  #END 로 사용하면 맨 뒤에 붙음.
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #삭제
    # listbox.delete(END)  #맨 뒤에 항목을 삭제f
    # listbox.delete(0)   #맨 앞에 황목을 삭제

    #갯수 확인
    print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인 
    print("1번쨰부터 3번째까지의 항목  : ",listbox.get(0,2))  # 0 , 1, 2 값 확인.

    # 선택된 항목 확인
    print("선택된 항목 : " ,listbox.curselection())
btn = Button(root, text="클릭", fg="red",  command = btncmd)
btn.pack()

root.mainloop()