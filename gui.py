import tkinter
from tkinter import *
from tkinter import ttk
import sender
import receiver
import plyer

NORMAL_TILE_COLOR = '#50577A'
SELECTED_TILE_COLOR = '#AAAAAA'
BACKGROUND_COLOR = "#404258"
CANVAS_BACKGROUND = "#50577A"
SCALE = 0.7


def send():
    global senderVar,receiverVar,passwordVar,subjectVar,bodyText
    senderMail = senderVar.get()
    receiverMail = receiverVar.get()
    password = passwordVar.get()
    subject = subjectVar.get()
    body = bodyText.get("1.0", END)

    if senderMail == '' or senderMail is None:
        # cmd.config(text='empty sender mail')
        # window.update()
        plyer.notification.notify(
            title="fail",
            message='empty sender mail',
            app_name="akram_mailing",
            # app_icon="",  # Replace with your icon path (if desired)
            timeout=20  # Display for 20 seconds
        )
    elif password == '' or password is None:
        # cmd.config(text='empty sender password')
        # window.update()
        plyer.notification.notify(
            title="fail",
            message='empty password mail',
            app_name="akram_mailing",
            # app_icon="",  # Replace with your icon path (if desired)
            timeout=20  # Display for 20 seconds
        )
    elif receiverMail == '' or receiverMail is None:
        # cmd.config(text='empty receiver mail')
        # window.update()
        plyer.notification.notify(
            title="fail",
            message='empty receiver mail',
            app_name="akram_mailing",
            # app_icon="",  # Replace with your icon path (if desired)
            timeout=20  # Display for 20 seconds
        )
    elif subject == '' or subject is None:
        # cmd.config(text='empty subject')
        # window.update()
        plyer.notification.notify(
            title="fail",
            message='empty subject',
            app_name="akram_mail",
            # app_icon="",  # Replace with your icon path (if desired)
            timeout=20  # Display for 20 seconds
        )
    elif body == '' or body is None:
        # cmd.config(text='empty body')
        # window.update()
        plyer.notification.notify(
            title="fail",
            message='empty body',
            app_name="akram_mail",
            # app_icon="",  # Replace with your icon path (if desired)
            timeout=20  # Display for 20 seconds
        )
    else:
        result =sender.sendViaGmail(senderMail,password,receiverMail,subject,body)
        if result is True:
            plyer.notification.notify(
                title="sucess",
                message='mail sent successfully',
                app_name="akram_mail",
                # app_icon="",  # Replace with your icon path (if desired)
                timeout=20  # Display for 20 seconds
            )
        else:
            plyer.notification.notify(
                title="fail",
                message=result,
                app_name="akram_mail",
                # app_icon="",  # Replace with your icon path (if desired)
                timeout=20  # Display for 20 seconds
            )
        # cmd.config(text='mail sent successfully')
        subjectVar.set('')
        bodyText.delete("1.0",tkinter.END)
        # cmd.update()


def receive():
    global senderVar,receiverVar,passwordVar,rcmd
    senderMail = senderVar.get()
    receiverMail = receiverVar.get()
    password = passwordVar.get()

    if receiverMail is None or receiverMail == '':
        criteria = 'ALL'
    else:
        criteria = f'FROM {senderMail}'
    status,messages = receiver.receiveViaGmail(receiverMail,password,criteria)

    if status is not True:

        plyer.notification.notify(
            title="failed",
            message=status,
            app_name="akram mailing system",
            # app_icon="",  # Replace with your icon path (if desired)
            timeout=20  # Display for 20 seconds
        )
    else:

        plyer.notification.notify(
            title="success",
            message="messages received successfully",
            app_name="akram mailing system",
            # app_icon="",  # Replace with your icon path (if desired)
            timeout=20  # Display for 20 seconds
        )
        i = 1
        for message in messages:
            number = Label(mailsFrame, text=f"Message number: {i}")
            number.pack()
            propertiesLabel = Label(mailsFrame,text=f"From: {message.get('From')}\n"
                                                    f"To: {message.get('To')}\n"
                                                    f"BCC: {message.get('BCC')}\n"
                                                    f"Date: {message.get('Date')}\n"
                                                    f"Subject: {message.get('Subject')}\n")
            propertiesLabel.pack()
            # print(f"From: {message.get('From')}")
            # print(f"To: {message.get('To')}")
            # print(f"BCC: {message.get('BCC')}")
            # print(f"Date: {message.get('Date')}")
            # print(f"Subject: {message.get('Subject')}")
            #
            # print("Content")
            plyer.notification.notify(
                title="new message received",
                message=f"From: {message.get('From')}\n"
                        f"To: {message.get('To')}\n"
                        f"BCC: {message.get('BCC')}\n"
                        f"Date: {message.get('Date')}\n"
                        f"Subject: {message.get('Subject')}\n",
                app_name="akram mailing system",
                # app_icon="",  # Replace with your icon path (if desired)
                timeout=20  # Display for 20 seconds
            )
            plyer.camera
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    # print(part.as_string())
                    partLabel = Label(mailsFrame,text=part.as_string())
                    partLabel.pack()

            i += 1

        print(canvas.bbox('all'))
        print(mailsFrame.bbox())
        canvas.update()


def terminate(event):
    exit()


if __name__ == '__main__':
    # setting the window
    window: Tk = Tk()
    window.geometry(f"{int(SCALE * 900)}x{int(SCALE * 700)}")
    window.title("SMTP client")
    window.config()
    # window.resizable(False, False)

    # notebook
    notebook = ttk.Notebook(window)
    senderTab = Frame(notebook,background=BACKGROUND_COLOR)
    receiverTab = Frame(notebook,background=BACKGROUND_COLOR)
    notebook.add(senderTab,text='Send')
    notebook.add(receiverTab,text='Receive')
    notebook.pack(expand=True,fill='both')

    # vars
    senderVar = StringVar(senderTab,'')
    receiverVar = StringVar(senderTab,'')
    passwordVar = StringVar(senderTab,'')
    subjectVar = StringVar(senderTab,'')

    # ============Sender tab=============

    # sender
    senderLabel = Label(senderTab, text='sender mail', font=('arial', int(12 * SCALE)), foreground='#D6E4E5'
                        ,background=BACKGROUND_COLOR)
    senderLabel.place(x=SCALE * 50, y=SCALE * 50)

    senderEntry = Entry(senderTab, textvariable=senderVar, font=('arial', int(14 * SCALE)))
    senderEntry.place(x=SCALE * 50, y=SCALE * 75)

    # pass
    passLabel = Label(senderTab, text='sender password', font=('arial', int(12 * SCALE)), foreground='#D6E4E5'
                        , background=BACKGROUND_COLOR)
    passLabel.place(x=SCALE * 50, y=SCALE * 120)

    passEntry = Entry(senderTab, textvariable=passwordVar, font=('arial', int(14 * SCALE)),show='*')
    passEntry.place(x=SCALE * 50, y=SCALE * 145)

    # receiver
    receiverLabel = Label(senderTab, text='receiver mail', font=('arial', int(12 * SCALE)), foreground='#D6E4E5',
                          background=BACKGROUND_COLOR)
    receiverLabel.place(x=SCALE * 550, y=SCALE * 50)

    receiverEntry = Entry(senderTab, textvariable=receiverVar, font=('arial', int(14 * SCALE)))
    receiverEntry.place(x=SCALE * 550, y=SCALE * 75)

    # subject
    subjectLabel = Label(senderTab, text='Subject:', font=('arial', int(17 * SCALE)), foreground='#D6E4E5',
                         background=BACKGROUND_COLOR)
    subjectLabel.place(x=SCALE * 50, y=SCALE * 220)

    subjectEntry = Entry(senderTab, textvariable=subjectVar, font=('arial', int(14 * SCALE)))
    subjectEntry.place(x=SCALE * 150, y=SCALE * 220)

    # body
    bodyLabel = Label(senderTab, text='Body:', font=('arial', int(17 * SCALE)), foreground='#D6E4E5',
                         background=BACKGROUND_COLOR)
    bodyLabel.place(x=SCALE * 50, y=SCALE * 260)

    bodyText = Text(senderTab, font=('arial', int(14 * SCALE)),height=10)
    bodyText.place(x=SCALE * 50, y=SCALE * 300)

    # send button
    sendButton = Button(senderTab, text='send', font=('arial', int(25 * SCALE)), foreground='#D6E4E5',
                    background="#404258", command=send)
    sendButton.place(x=SCALE * 420, y=SCALE * 550)

    # ============Receiver tab=============
    canvas = Canvas(receiverTab,bg=BACKGROUND_COLOR)
    canvas.pack(side='right',fill='both',expand=True)

    scrollbar = Scrollbar(receiverTab,orient='vertical')
    scrollbar.pack(side='right',fill='y')
    canvas.config(yscrollcommand=scrollbar.set,scrollregion=canvas.bbox("all"))
    scrollbar.config(command=canvas.yview)

    # receiver
    receiverFrame = Frame(receiverTab,bg=BACKGROUND_COLOR)

    rreceiverLabel = Label(receiverFrame, text='receiver mail', font=('arial', int(12 * SCALE)), foreground='#D6E4E5',
                           background=BACKGROUND_COLOR, padx=10, pady=5)
    rreceiverLabel.pack()

    rreceiverEntry = Entry(receiverFrame, textvariable=receiverVar, font=('arial', int(14 * SCALE)))
    rreceiverEntry.pack()

    # pass
    rpassLabel = Label(receiverFrame, text='password', font=('arial', int(12 * SCALE)), foreground='#D6E4E5'
                      , background=BACKGROUND_COLOR,padx=10,pady=5)
    rpassLabel.pack()

    rpassEntry = Entry(receiverFrame, textvariable=passwordVar, font=('arial', int(14 * SCALE)), show='*')
    rpassEntry.pack()

    receiverFrame.pack(anchor='nw', padx=20, pady=20, side='top')
    # messageFrame = Frame(canvas, bg=BACKGROUND_COLOR)

    # sender
    senderFrame = Frame(receiverTab, bg=BACKGROUND_COLOR)
    rsenderLabel = Label(senderFrame, text='sender mail', font=('arial', int(12 * SCALE)), foreground='#D6E4E5'
                         , background=BACKGROUND_COLOR, padx=10, pady=5)
    rsenderLabel.pack(side='top', padx=20, pady=20)

    rsenderEntry = Entry(senderFrame, textvariable=senderVar, font=('arial', int(14 * SCALE)))
    rsenderEntry.pack(side='bottom')
    senderFrame.pack(anchor='ne', padx=20, pady=20)

    mailsFrame = Frame(canvas,bg=BACKGROUND_COLOR)
    # mailsFrame.pack()
    # canvas.create_window((0,0),anchor='nw',window=messageFrame)
    canvas.create_window(0,0,anchor='nw',window=mailsFrame)
    # prompts

    # receive button
    receiveButton = Button(receiverTab, text='fetch mails', font=('arial', int(25 * SCALE)), foreground='#D6E4E5',
                        background="#404258", command=receive)
    receiveButton.pack(side='bottom',padx=10,pady=10)

    # =====================================
    # bindings and end
    window.bind("<Escape>",terminate)
    window.mainloop()
