from tkinter import *
from tkinter import ttk

NORMAL_TILE_COLOR = '#50577A'
SELECTED_TILE_COLOR = '#AAAAAA'
BACKGROUND_COLOR = "#404258"
CANVAS_BACKGROUND = "#50577A"
SCALE = 1


window: Tk = Tk()
window.geometry(f"{int(SCALE * 900)}x{int(SCALE * 700)}")
window.title("test gui")
window.config()

canvas = Canvas(window,bg=BACKGROUND_COLOR)
canvas.pack(side='left',fill='both',expand=True)

scrollbar = Scrollbar(window,orient='vertical')
scrollbar.pack(side='right',fill='y')
canvas.config(yscrollcommand=scrollbar.set,scrollregion=canvas.bbox("all"))
scrollbar.config(command=canvas.yview)

frame = Frame(canvas,bg=SELECTED_TILE_COLOR)
label = Label(frame,font=('arial', int(24 * SCALE)),text='aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
                         'aaaaaaa\n'
              )
label.pack(fill='y')
canvas.create_window(100,50,anchor='nw',window=frame)
# window.update()
# scrollbar.update()
# frame.pack()
print(canvas.bbox("all"))
print(frame.bbox())
window.mainloop()
