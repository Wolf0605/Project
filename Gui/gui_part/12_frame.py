
from tkinter import*

root = Tk()
root.title("Nado GUI")   
root.geometry("640x480+900+300")  

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side= "bottom")
# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)  #relief :  테두리모양 bd :외각선
frame_burger.pack(side="left", fill="both", expand= True)

Button(frame_burger, text="햄버거").pack()  #frame_bureger 안에서 일어나는거라 root 대신 저거넣음.
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both" ,expand= True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()


root.mainloop()