from tkinter import *


class CustomTextOutput:
    def __init__(self, root, max_lines=100):  # Optional: Limit displayed lines
        self.text_widget = Text(root, state="disabled", font=("Consolas", 12))
        self.text_widget.pack(expand=True)

        # # Optional scrollbar
        # self.scrollbar = Scrollbar(root, orient="vertical")
        # self.scrollbar.pack(side="right", fill="y")
        # self.text_widget.config(yscrollcommand=self.scrollbar.set)
        # self.scrollbar.config(command=self.text_widget.yview)
        #
        # self.max_lines = max_lines  # Store for potential line limiting

    def write(self, text):
        # Insert text at the end while keeping the end visible
        self.text_widget.insert(END, text + "\n")
        self.text_widget.see(END)

        # # Optional: Limit the number of lines displayed (if needed)
        # if self.max_lines > 0 and self.text_widget.index("end-1c") != END:  # Check for content
        #     self.text_widget.delete("1.0", END - EXTENDED[-1] + str(self.max_lines) + ".0")


def main():
    # Example usage
    root = Tk()
    output = CustomTextOutput(root, max_lines=20)  # Adjust max_lines as needed

    output.write("Welcome to the mini-command prompt!")
    output.write("> Your message here")
    root.mainloop()


if __name__ == '__main__':
    main()
