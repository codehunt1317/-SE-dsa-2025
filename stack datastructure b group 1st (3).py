undo, redo = [], []
doc = ""

def change(txt):
    global doc
    undo.append(doc)
    doc += txt
    redo.clear()

def undo_action():
    global doc
    if undo:
        redo.append(doc)
        doc = undo.pop()

def redo_action():
    global doc
    if redo:
        undo.append(doc)
        doc = redo.pop()

# --- Demo ---
change("Hello ")
change("World")
print("After changes:", doc)
undo_action()
print("After undo:", doc)
redo_action()
print("After redo:", doc)

# Time: O(1) per op | Space: O(n)