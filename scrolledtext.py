import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title('ScrolledText Widget')

st = ScrolledText(root, width=50, height=10, bg='white', fg='black')
st.pack(fill='both', side='left', expand=True)

root.mainloop()