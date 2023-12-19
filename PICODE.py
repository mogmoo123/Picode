'''
PICODE 전용 컴파일러
접두사 정리:
';' : 코드
없음 : 숫자
;314 (o)
314 (x) <- 그냥 숫자
'''

from tkinter import *
from keyboard import is_pressed

path = ''

class Compile:
    intVars = []
    floatVars = []
    strVars= []
    def Compile(file):

        
        def var(code):
            if (code[0]=="1"):
                return floatVars[int(code[1])]
            if (code[0] == "4"):
                return strVars[int(code[1])]
            if (code[0] == "3"):
                return intVars[int(code[1])]

        f = open(file)
        intVars = []
        floatVars = []
        strVars = []
        line = 0
        loop = 0
        while(True):
            line += 1
            code = f.readline().strip('\n')
            if(code == ''):
                break

            '''
            여기서부터는 코드를 작성한걸 해석하는 부분
            이제 준비는 끝났다고 보면됨
            '''
            
            if(code[0:8] == "3.141592") : break

            #출력
            if(code[0:5] == ";;314"):
                try:
                    if(code[5] == "3"):
                        print(intVars[int(code[6])])
                    if(code[5] == "1"):
                        print(floatVars[int(code[6])])
                    if(code[5] == "4"):
                        print(strVars[int(code[6])])
                except IndexError:
                    print(f"어이쿠 {line}번째 줄에 없는 변수가 쓰였어요!\nCouldn't found variable in line {line}")
                    break

            #입력
            if(code[0:5] == ";;159"):
                try:
                    if(code[5] == "3"):
                        intVars[int(code[6])] = int(input(code[7:code.__len__()]))
                    if(code[5] == "1"):
                        floatVars[int(code[6])] = float(input(code[7:code.__len__()]))
                    if(code[5] == "4"):
                        strVars[int(code[6])] = str(input(code[7:code.__len__()]))
                except IndexError:
                    print(f"저런 {line}번째 줄에 없는 변수가 쓰였어요!\nCouldn't found variable in line{line}")
                    break
                except ValueError:
                    print(f"이런 {line}번째 줄에 자료형이 잘못 되었어요~!\nThe data type is wrong in line{line}")

            #변수

            #정수형 변수
            if(code[0:2] == ";3"):
                if(intVars.__len__() <= int(code[2])):
                    intVars.append(int(code[3:code.__len__()]))
                intVars[int(code[2])] = int(code[3:code.__len__()])
                    
            #실수형 변수
            if(code[0:2] == ";1"):
                if(floatVars.__len__() <= int(code[2])):
                    floatVars.append(float(code[3:code.__len__()]))
                floatVars[int(code[2])] = float(code[3:code.__len__()])
            #문자형 변수
            if(code[0:2] == ";4"):
                if(strVars.__len__() <= int(code[2])):
                    strVars.append(str(code[3:code.__len__()]))
                strVars[int(code[2])] = str(code[3:code.__len__()])

            #반복문
            if(code[0:2] == ";."):
                if(loop == int(code[3])-1):
                    continue
                f.seek(int(code[3]))
                loop+=1
            
            #조건문
                

        print("프로그램 종료\nProgram End.")
        f.close()

def window():
    def pathinput():
        
        try:
            global path
            path=str(CodePathEnter.get())
            open(path)
        except FileNotFoundError:
            print(f"아이고 세상에나 없는 파일이에요!\nCouldn't found the file '{path}'")
    
    def compilestart():
        Compile.Compile(file= path)

    root = Tk()
    ##Setup Window
    root.title('PICODE 0.1V Compiler')
    root.geometry('600x300')
    root.maxsize(width=600,height=300)
    root.minsize(width=600,height=300)
    ##Design Window
    logo = PhotoImage(file='logo.png')
    titleText = Label(root,image=logo)
    CodePathEnter = Entry(root,width=30,background='#9E9E9E',foreground='#AFD485',font=('나눔고딕',10,'bold'))
    CodePathEnterLabel = Label(root,text='Path',font=('나눔고딕',20,'bold'),foreground='#9E9E9E')
    Codeloader = Button(root,text='Load', font=('나눔고딕',20),background='#9E9E9E',foreground='#AFD485',height=1,command=pathinput)
    CompileButton = Button(root,text='COMPILE', font=('나눔고딕',20),background='#9E9E9E',foreground='#B8E5E0',height=1,command=compilestart)
    ##Place Widgets
    titleText.pack()
    CodePathEnter.place(x=190,y=110)
    CodePathEnterLabel.place(x=120,y=100)
    Codeloader.place(x=120,y=140)
    CompileButton.place(x=120,y=200)
    ##Generation Window
    root.mainloop()

    

def main():
    window()

if __name__ == "__main__":
    main()