from tkinter import *
import random
from tkinter import messagebox

##############Root###########################
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typing speed game')

words = ['Apple','access','account','across','Time','Really','address','adventure',
               'approval','actually','service','order','Little','small','fight','italian',
               'beach','believe','beside','blame','borrow']

###############functions ##############3
def labelSlider():
    global count,sliderwords
    text = 'Welcome to typing Increaser Game'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelSlider)

def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
        #print("score ",score)
    else:
        miss += 1
        #print("miss ",miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
#print(wordEntry.get())
    wordEntry.delete(0,END)

def time():
    global timeleft,score,miss
    
    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total score = {}'.format(score,miss,score-miss))
        dk = messagebox.askretrycancel('notification','For Play Again Click Retry Button')
        if(dk == True):
            score = 0
            miss = 0
            timeleft = 60
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
        else:
            root.destroy()

################# Variables ######################3
score = 0
timeleft = 60
count = 0
sliderwords = ''
miss = 0

##############################Label ################################
fontLabel = Label(root,text='Welcome to typing speed increaser game',font=('times',25,'italic bold'),bg='powder blue',width=40)
fontLabel.place(x=10,y=10)
labelSlider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('times',40,'italic bold'),bg='powder blue')
wordLabel.place(x=350,y=200)

scoreLabel = Label(root,text='Your score : ',font=('times',25,'italic bold'),bg='powder blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score,font=('times',25,'italic bold'),bg='powder blue')
scoreLabelCount.place(x=80,y=170)

timerLabel = Label(root,text='Time left : ',font=('times',25,'italic bold'),bg='powder blue')
timerLabel.place(x=600,y=100)

timeLabelCount = Label(root,text=timeleft,font=('times',25,'italic bold'),bg='powder blue')
timeLabelCount.place(x=650,y=170)

gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',font=('times',30,'italic bold'),bg='powder blue')
gamePlayDetailLabel.place(x=120,y=450)

######################## Entry #######################################
wordEntry = Entry(root,font=('times',25,'bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()

root.bind('<Return>',startGame)
root.mainloop()
