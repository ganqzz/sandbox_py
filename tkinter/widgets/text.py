from tkinter import *

root = Tk()

text = Text(root, width=40, height=10)
text.pack()
text.config(wrap=WORD)  # char(default), word, none
text.config(undo=True)  # enable undo/redo

# base formats: line.char
text.insert('1.0 + 2 lines', 'Inserted message')
text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.')
print(text.get('1.0', 'end'))  # line1:char0 ~ end
print(text.get('1.0', '1.end'))  # logical line
text.delete('1.0')
text.delete('1.0', '1.0 lineend')
text.delete('1.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is the first line.')

text.config(state='disabled')
text.delete('1.0', 'end')
text.config(state='normal')

# Tags
text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background='yellow')
text.tag_remove('my_tag', '1.1', '1.3')
print(text.tag_ranges('my_tag'))
print(text.tag_names())  # 'sel': selected area
text.replace('my_tag.first', 'my_tag.last', 'That')
text.tag_delete('my_tag')

# Marks
# 'insert': cursor position, 'current': the character position to the closest mouse position
text.insert('insert', '_')
text.mark_set('my_mark', 'end')
print(text.mark_names())
text.mark_gravity('my_mark', 'right')
text.mark_unset('my_mark')

image = PhotoImage(file='python_logo.gif').subsample(5, 5)
text.image_create('insert', image=image)
text.image_create('insert', image=image)

button = Button(text, text='Click Me')
text.window_create('insert', window=button)

root.mainloop()
