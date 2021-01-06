import random
try:
    from tkinter import *
except:
    from Tkinter import *

def callback(event):
    r1c1o = canvas.find_withtag("11o")
    r2c1o = canvas.find_withtag("12o")
    r3c1o = canvas.find_withtag("13o")
    r1c2o = canvas.find_withtag("21o")
    r2c2o = canvas.find_withtag("22o")
    r3c2o = canvas.find_withtag("23o")
    r1c3o = canvas.find_withtag("31o")
    r2c3o = canvas.find_withtag("32o")
    r3c3o = canvas.find_withtag("33o")
    arr = []
    arr.append(r1c1o)
    arr.append(r2c1o)
    arr.append(r3c1o)
    arr.append(r1c2o)
    arr.append(r2c2o)
    arr.append(r3c2o)
    arr.append(r1c3o)
    arr.append(r2c3o)
    arr.append(r3c3o)
    new = list(filter(lambda x: x == (), arr))
    county = new.count(())
    r1c1x = canvas.find_withtag("11x")
    r2c1x = canvas.find_withtag("12x")
    r3c1x = canvas.find_withtag("13x")
    r1c2x = canvas.find_withtag("21x")
    r2c2x = canvas.find_withtag("22x")
    r3c2x = canvas.find_withtag("23x")
    r1c3x = canvas.find_withtag("31x")
    r2c3x = canvas.find_withtag("32x")
    r3c3x = canvas.find_withtag("33x")
    ar = []
    ar.append(r1c1x)
    ar.append(r2c1x)
    ar.append(r3c1x)
    ar.append(r1c2x)
    ar.append(r2c2x)
    ar.append(r3c2x)
    ar.append(r1c3x)
    ar.append(r2c3x)
    ar.append(r3c3x)
    new1 = list(filter(lambda x: x == (), ar))
    countx = new1.count(())
    county = 9 - county
    countx = 9 - countx
    if county == countx:
        x, y = (event.x), (event.y)
        obj = canvas.find_overlapping(x, y, x, y)

        if x < 200 and y < 200 and obj == ():
            canvas.create_rectangle(0, 0, 199, 199, fill='black', tags="11x")
            canvas.create_line(50, 50, 150, 150, fill='white')
            canvas.create_line(50, 150, 150, 50, fill='white')
        elif 200 < y < 400 and x < 200 and obj == ():
            canvas.create_rectangle(0, 201, 199, 399, fill='black', tags="12x")
            canvas.create_line(50, 250, 150, 350, fill='white')
            canvas.create_line(50, 350, 150, 250, fill='white')
        elif 400 < y < 600 and x < 200 and obj == ():
            canvas.create_rectangle(0, 401, 199, 599, fill='black', tags="13x")
            canvas.create_line(50, 450, 150, 550, fill='white')
            canvas.create_line(50, 550, 150, 450, fill='white')
        elif 200 < x < 400 and y < 200 and obj == ():
            canvas.create_rectangle(201, 0, 399, 199, fill='black', tags="21x")
            canvas.create_line(250, 50, 350, 150, fill='white')
            canvas.create_line(250, 150, 350, 50, fill='white')
        elif 200 < x < 400 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(201, 201, 399, 399, fill='black', tags="22x")
            canvas.create_line(250, 250, 350, 350, fill='white')
            canvas.create_line(250, 350, 350, 250, fill='white')
        elif 200 < x < 400 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(201, 401, 399, 599, fill='black', tags="23x")
            canvas.create_line(250, 450, 350, 550, fill='white')
            canvas.create_line(250, 550, 350, 450, fill='white')
        elif 400 < x < 600 and y < 200 and obj == ():
            canvas.create_rectangle(401, 0, 599, 199, fill='black', tags="31x")
            canvas.create_line(450, 50, 550, 150, fill='white')
            canvas.create_line(450, 150, 550, 50, fill='white')
        elif 400 < x < 600 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(401, 201, 599, 399, fill='black', tags="32x")
            canvas.create_line(450, 250, 550, 350, fill='white')
            canvas.create_line(450, 350, 550, 250, fill='white')
        elif 400 < x < 600 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(401, 401, 599, 599, fill='black', tags="33x")
            canvas.create_line(450, 450, 550, 550, fill='white')
            canvas.create_line(450, 550, 550, 450, fill='white')

    r1c1x = canvas.find_withtag("11x")
    r2c1x = canvas.find_withtag("12x")
    r3c1x = canvas.find_withtag("13x")
    r1c2x = canvas.find_withtag("21x")
    r2c2x = canvas.find_withtag("22x")
    r3c2x = canvas.find_withtag("23x")
    r1c3x = canvas.find_withtag("31x")
    r2c3x = canvas.find_withtag("32x")
    r3c3x = canvas.find_withtag("33x")

    if r1c1x and r2c1x and r3c1x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    elif r1c2x and r2c2x and r3c2x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    elif r1c3x and r2c3x and r3c3x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    elif r1c1x and r1c2x and r1c3x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    elif r2c1x and r2c2x and r2c3x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    elif r3c1x and r3c2x and r3c3x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    elif r1c1x and r2c2x and r3c3x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    elif r3c1x and r2c2x and r1c3x != ():
        tk.after(1000)
        tk.destroy()
        return winscreen()
    else:
        if county + countx == 8:
            tk.destroy()
            return tiescreen()
        else:
            pass;


def easy(event):
    r1c1o = canvas.find_withtag("11o")
    r2c1o = canvas.find_withtag("12o")
    r3c1o = canvas.find_withtag("13o")
    r1c2o = canvas.find_withtag("21o")
    r2c2o = canvas.find_withtag("22o")
    r3c2o = canvas.find_withtag("23o")
    r1c3o = canvas.find_withtag("31o")
    r2c3o = canvas.find_withtag("32o")
    r3c3o = canvas.find_withtag("33o")
    arr = []
    arr.append(r1c1o)
    arr.append(r2c1o)
    arr.append(r3c1o)
    arr.append(r1c2o)
    arr.append(r2c2o)
    arr.append(r3c2o)
    arr.append(r1c3o)
    arr.append(r2c3o)
    arr.append(r3c3o)
    new = list(filter(lambda x: x == (), arr))
    county = new.count(())
    r1c1x = canvas.find_withtag("11x")
    r2c1x = canvas.find_withtag("12x")
    r3c1x = canvas.find_withtag("13x")
    r1c2x = canvas.find_withtag("21x")
    r2c2x = canvas.find_withtag("22x")
    r3c2x = canvas.find_withtag("23x")
    r1c3x = canvas.find_withtag("31x")
    r2c3x = canvas.find_withtag("32x")
    r3c3x = canvas.find_withtag("33x")
    ar = []
    ar.append(r1c1x)
    ar.append(r2c1x)
    ar.append(r3c1x)
    ar.append(r1c2x)
    ar.append(r2c2x)
    ar.append(r3c2x)
    ar.append(r1c3x)
    ar.append(r2c3x)
    ar.append(r3c3x)
    new1 = list(filter(lambda x: x == (), ar))
    countx = new1.count(())
    countx = 9 - countx
    county = 9 - county
    if county == countx - 1:
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        obj = canvas.find_overlapping(x, y, x, y)
        if x < 200 and y < 200 and obj == ():
            canvas.create_rectangle(0, 0, 199, 199, fill='black', tags="11o")
            canvas.create_oval(50, 50, 150, 150, outline='white')
        elif 200 < y < 400 and x < 200 and obj == ():
            canvas.create_rectangle(0, 201, 199, 399, fill='black', tags="12o")
            canvas.create_oval(50, 250, 150, 350, outline='white')
        elif 400 < y < 600 and x < 200 and obj == ():
            canvas.create_rectangle(0, 401, 199, 599, fill='black', tags="13o")
            canvas.create_oval(50, 450, 150, 550, outline='white')
        elif 200 < x < 400 and y < 200 and obj == ():
            canvas.create_rectangle(201, 0, 399, 199, fill='black', tags="21o")
            canvas.create_oval(250, 50, 350, 150, outline='white')
        elif 200 < x < 400 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(201, 201, 399, 399, fill='black', tags="22o")
            canvas.create_oval(250, 250, 350, 350, outline='white')
        elif 200 < x < 400 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(201, 401, 399, 599, fill='black', tags="23o")
            canvas.create_oval(250, 450, 350, 550, outline='white')
        elif 400 < x < 600 and y < 200 and obj == ():
            canvas.create_rectangle(401, 0, 599, 199, fill='black', tags="31o")
            canvas.create_oval(450, 50, 550, 150, outline='white')
        elif 400 < x < 600 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(401, 201, 599, 399, fill='black', tags="32o")
            canvas.create_oval(450, 250, 550, 350, outline='white')
        elif 400 < x < 600 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(401, 401, 599, 599, fill='black', tags="33o")
            canvas.create_oval(450, 450, 550, 550, outline='white')
        else:
            pass;
        r1c1o = canvas.find_withtag("11o")
        r2c1o = canvas.find_withtag("12o")
        r3c1o = canvas.find_withtag("13o")
        r1c2o = canvas.find_withtag("21o")
        r2c2o = canvas.find_withtag("22o")
        r3c2o = canvas.find_withtag("23o")
        r1c3o = canvas.find_withtag("31o")
        r2c3o = canvas.find_withtag("32o")
        r3c3o = canvas.find_withtag("33o")
        if r1c1o and r2c1o and r3c1o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c2o and r2c2o and r3c2o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c3o and r2c3o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c1o and r1c2o and r1c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r2c1o and r2c2o and r2c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r3c1o and r3c2o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c1o and r2c2o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c3o and r2c2o and r3c1o != ():
            tk.destroy()
            return losescreen()
        else:
            if county + countx == 9:
                tk.destroy()
                return losescreen()
            else:
                if county + countx == 9:
                    tk.destroy()
                    return menu()
                else:
                    pass;


def medium(event):
    global x, x
    r1c1o = canvas.find_withtag("11o")
    r2c1o = canvas.find_withtag("12o")
    r3c1o = canvas.find_withtag("13o")
    r1c2o = canvas.find_withtag("21o")
    r2c2o = canvas.find_withtag("22o")
    r3c2o = canvas.find_withtag("23o")
    r1c3o = canvas.find_withtag("31o")
    r2c3o = canvas.find_withtag("32o")
    r3c3o = canvas.find_withtag("33o")
    arr = []
    arr.append(r1c1o)
    arr.append(r2c1o)
    arr.append(r3c1o)
    arr.append(r1c2o)
    arr.append(r2c2o)
    arr.append(r3c2o)
    arr.append(r1c3o)
    arr.append(r2c3o)
    arr.append(r3c3o)
    new = list(filter(lambda x: x == (), arr))
    county = new.count(())
    r1c1x = canvas.find_withtag("11x")
    r2c1x = canvas.find_withtag("12x")
    r3c1x = canvas.find_withtag("13x")
    r1c2x = canvas.find_withtag("21x")
    r2c2x = canvas.find_withtag("22x")
    r3c2x = canvas.find_withtag("23x")
    r1c3x = canvas.find_withtag("31x")
    r2c3x = canvas.find_withtag("32x")
    r3c3x = canvas.find_withtag("33x")
    ar = []
    ar.append(r1c1x)
    ar.append(r2c1x)
    ar.append(r3c1x)
    ar.append(r1c2x)
    ar.append(r2c2x)
    ar.append(r3c2x)
    ar.append(r1c3x)
    ar.append(r2c3x)
    ar.append(r3c3x)
    new1 = list(filter(lambda x: x == (), ar))
    countx = new1.count(())
    countx = 9 - countx
    county = 9 - county
    if county == countx - 1:
        if county == 0 and r2c2x == ():
            x = 350
            y = 350
        elif r1c1x and r1c2x != () and r1c3o == () or r1c1x and r1c3x != () and r1c2o == () or r1c2x and r1c3x != () and r1c1o == ():
            first = []
            first.append(r1c1x)
            first.append(r1c2x)
            first.append(r1c3x)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 150
            elif aba == 1:
                x = 350
                y = 150
            elif aba == 2:
                x = 550
                y = 150
        elif r2c1x and r2c2x != () and r2c3o == () or r2c1x and r2c3x != () and r2c2o == () or r2c2x and r2c3x != () and r2c1o == ():
            first = []
            first.append(r2c1x)
            first.append(r2c2x)
            first.append(r2c3x)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 350
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 550
                y = 350

        elif r3c1x and r3c2x != () and r3c3o == () or r3c1x and r3c3x != () and r3c2o == () or r3c2x and r3c3x != () and r3c1o == ():
            first = []
            first.append(r3c1x)
            first.append(r3c2x)
            first.append(r3c3x)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 550
            elif aba == 1:
                x = 350
                y = 550
            elif aba == 2:
                x = 550
                y = 550
        elif r1c1x and r2c1x != () and r3c1o == () or r1c1x and r3c1x != () and r2c1o == () or r2c1x and r3c1x != () and r1c1o == ():
            first = []
            first.append(r1c1x)
            first.append(r2c1x)
            first.append(r3c1x)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 150
            elif aba == 1:
                x = 150
                y = 350
            elif aba == 2:
                x = 150
                y = 550
        elif r1c2x and r2c2x != () and r3c2o == () or r1c2x and r3c2x != () and r2c2o == () or r2c2x and r3c2x != () and r1c2o == ():
            first = []
            first.append(r1c2x)
            first.append(r2c2x)
            first.append(r3c2x)
            aba = first.index(())
            if aba == 0:
                x = 350
                y = 150
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 350
                y = 550
        elif r1c3x and r2c3x != () and r3c3o == () or r1c3x and r3c3x != () and r2c3o == () or r2c3x and r3c3x != () and r1c3o == ():
            first = []
            first.append(r1c3x)
            first.append(r2c3x)
            first.append(r3c3x)
            aba = first.index(())
            if aba == 0:
                x = 550
                y = 150
            elif aba == 1:
                x = 550
                y = 350
            elif aba == 2:
                x = 550
                y = 550
        elif r1c1x and r2c2x != () and r3c3o == () or r1c1x and r3c3x != () and r2c2o == () or r2c2x and r3c3x != () and r1c1o == ():
            first = []
            first.append(r1c1x)
            first.append(r2c2x)
            first.append(r3c3x)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 150
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 550
                y = 550
        elif r3c1x and r2c2x != () and r1c3o == () or r3c1x and r1c3x != () and r2c2o == () or r1c3x and r2c2x != () and r3c1o == ():
            first = []
            first.append(r3c1x)
            first.append(r2c2x)
            first.append(r1c3x)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 550
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 550
                y = 150
        else:
            x = random.randint(0, 600)
            y = random.randint(0, 600)
        obj = canvas.find_overlapping(x, y, x, y)
        if x < 200 and y < 200 and obj == ():
            canvas.create_rectangle(0, 0, 199, 199, fill='black', tags="11o")
            canvas.create_oval(50, 50, 150, 150, outline='white')
        elif 200 < y < 400 and x < 200 and obj == ():
            canvas.create_rectangle(0, 201, 199, 399, fill='black', tags="12o")
            canvas.create_oval(50, 250, 150, 350, outline='white')
        elif 400 < y < 600 and x < 200 and obj == ():
            canvas.create_rectangle(0, 401, 199, 599, fill='black', tags="13o")
            canvas.create_oval(50, 450, 150, 550, outline='white')
        elif 200 < x < 400 and y < 200 and obj == ():
            canvas.create_rectangle(201, 0, 399, 199, fill='black', tags="21o")
            canvas.create_oval(250, 50, 350, 150, outline='white')
        elif 200 < x < 400 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(201, 201, 399, 399, fill='black', tags="22o")
            canvas.create_oval(250, 250, 350, 350, outline='white')
        elif 200 < x < 400 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(201, 401, 399, 599, fill='black', tags="23o")
            canvas.create_oval(250, 450, 350, 550, outline='white')
        elif 400 < x < 600 and y < 200 and obj == ():
            canvas.create_rectangle(401, 0, 599, 199, fill='black', tags="31o")
            canvas.create_oval(450, 50, 550, 150, outline='white')
        elif 400 < x < 600 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(401, 201, 599, 399, fill='black', tags="32o")
            canvas.create_oval(450, 250, 550, 350, outline='white')
        elif 400 < x < 600 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(401, 401, 599, 599, fill='black', tags="33o")
            canvas.create_oval(450, 450, 550, 550, outline='white')
        else:
            pass;
        r1c1o = canvas.find_withtag("11o")
        r2c1o = canvas.find_withtag("12o")
        r3c1o = canvas.find_withtag("13o")
        r1c2o = canvas.find_withtag("21o")
        r2c2o = canvas.find_withtag("22o")
        r3c2o = canvas.find_withtag("23o")
        r1c3o = canvas.find_withtag("31o")
        r2c3o = canvas.find_withtag("32o")
        r3c3o = canvas.find_withtag("33o")
        if r1c1o and r2c1o and r3c1o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c2o and r2c2o and r3c2o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c3o and r2c3o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c1o and r1c2o and r1c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r2c1o and r2c2o and r2c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r3c1o and r3c2o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c1o and r2c2o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c3o and r2c2o and r3c1o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        else:
            if county + countx == 9:
                tk.destroy()
                return menu()
            else:
                pass;


def hard(event):
    r1c1o = canvas.find_withtag("11o")
    r2c1o = canvas.find_withtag("12o")
    r3c1o = canvas.find_withtag("13o")
    r1c2o = canvas.find_withtag("21o")
    r2c2o = canvas.find_withtag("22o")
    r3c2o = canvas.find_withtag("23o")
    r1c3o = canvas.find_withtag("31o")
    r2c3o = canvas.find_withtag("32o")
    r3c3o = canvas.find_withtag("33o")
    arr = []
    arr.append(r1c1o)
    arr.append(r2c1o)
    arr.append(r3c1o)
    arr.append(r1c2o)
    arr.append(r2c2o)
    arr.append(r3c2o)
    arr.append(r1c3o)
    arr.append(r2c3o)
    arr.append(r3c3o)
    new = list(filter(lambda x: x == (), arr))
    county = new.count(())
    r1c1x = canvas.find_withtag("11x")
    r2c1x = canvas.find_withtag("12x")
    r3c1x = canvas.find_withtag("13x")
    r1c2x = canvas.find_withtag("21x")
    r2c2x = canvas.find_withtag("22x")
    r3c2x = canvas.find_withtag("23x")
    r1c3x = canvas.find_withtag("31x")
    r2c3x = canvas.find_withtag("32x")
    r3c3x = canvas.find_withtag("33x")
    ar = []
    ar.append(r1c1x)
    ar.append(r2c1x)
    ar.append(r3c1x)
    ar.append(r1c2x)
    ar.append(r2c2x)
    ar.append(r3c2x)
    ar.append(r1c3x)
    ar.append(r2c3x)
    ar.append(r3c3x)
    new1 = list(filter(lambda x: x == (), ar))
    countx = new1.count(())
    countx = 9 - countx
    county = 9 - county
    if county == countx - 1:
        r1c1x = canvas.find_withtag("11x")
        r2c1x = canvas.find_withtag("12x")
        r3c1x = canvas.find_withtag("13x")
        r1c2x = canvas.find_withtag("21x")
        r2c2x = canvas.find_withtag("22x")
        r3c2x = canvas.find_withtag("23x")
        r1c3x = canvas.find_withtag("31x")
        r2c3x = canvas.find_withtag("32x")
        r3c3x = canvas.find_withtag("33x")
        r1c1o = canvas.find_withtag("11o")
        r2c1o = canvas.find_withtag("12o")
        r3c1o = canvas.find_withtag("13o")
        r1c2o = canvas.find_withtag("21o")
        r2c2o = canvas.find_withtag("22o")
        r3c2o = canvas.find_withtag("23o")
        r1c3o = canvas.find_withtag("31o")
        r2c3o = canvas.find_withtag("32o")
        r3c3o = canvas.find_withtag("33o")

        if r1c1o and r1c2o != () and r1c3x == () or r1c1o and r1c3o != () and r1c2x == () or r1c2o and r1c3o != () and r1c1x == ():
            first = []
            first.append(r1c1o)
            first.append(r1c2o)
            first.append(r1c3o)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 150
            elif aba == 1:
                x = 350
                y = 150
            elif aba == 2:
                x = 550
                y = 150
        elif r2c1o and r2c2o != () and r2c3x == () or r2c1o and r2c3o != () and r2c2x == () or r2c2o and r2c3o != () and r2c1x == ():
            first = []
            first.append(r2c1o)
            first.append(r2c2o)
            first.append(r2c3o)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 350
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 550
                y = 350

        elif r3c1o and r3c2o != () and r3c3x == () or r3c1o and r3c3o != () and r3c2x == () or r3c2o and r3c3o != () and r3c1x == ():
            first = []
            first.append(r3c1o)
            first.append(r3c2o)
            first.append(r3c3o)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 550
            elif aba == 1:
                x = 350
                y = 550
            elif aba == 2:
                x = 550
                y = 550
        elif r1c1o and r2c1o != () and r3c1x == () or r1c1o and r3c1o != () and r2c1x == () or r2c1o and r3c1o != () and r1c1x == ():
            first = []
            first.append(r1c1o)
            first.append(r2c1o)
            first.append(r3c1o)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 150
            elif aba == 1:
                x = 150
                y = 350
            elif aba == 2:
                x = 150
                y = 550
        elif r1c2o and r2c2o != () and r3c2x == () or r1c2o and r3c2o != () and r2c2x == () or r2c2o and r3c2o != () and r1c2x == ():
            first = []
            first.append(r1c2o)
            first.append(r2c2o)
            first.append(r3c2o)
            aba = first.index(())
            if aba == 0:
                x = 350
                y = 150
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 350
                y = 550
        elif r1c3o and r2c3o != () and r3c3x == () or r1c3o and r3c3o != () and r2c3x == () or r2c3o and r3c3o != () and r1c3x == ():
            first = []
            first.append(r1c3o)
            first.append(r2c3o)
            first.append(r3c3o)
            aba = first.index(())
            if aba == 0:
                x = 550
                y = 150
            elif aba == 1:
                x = 550
                y = 350
            elif aba == 2:
                x = 550
                y = 550
        elif r1c1o and r2c2o != () and r3c3x == () or r1c1o and r3c3o != () and r2c2x == () or r2c2o and r3c3o != () and r1c1x == ():
            first = []
            first.append(r1c1o)
            first.append(r2c2o)
            first.append(r3c3o)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 150
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 550
                y = 550
        elif r3c1o and r2c2o != () and r1c3x == () or r3c1o and r1c3o != () and r2c2x == () or r1c3o and r2c2o != () and r3c1x == ():
            first = []
            first.append(r3c1o)
            first.append(r2c2o)
            first.append(r1c3o)
            aba = first.index(())
            if aba == 0:
                x = 150
                y = 550
            elif aba == 1:
                x = 350
                y = 350
            elif aba == 2:
                x = 550
                y = 150
        else:
            if county == 0 and r2c2x == ():
                x = 350
                y = 350
            elif r1c1x and r1c2x != () and r1c3o == () or r1c1x and r1c3x != () and r1c2o == () or r1c2x and r1c3x != () and r1c1o == ():
                first = []
                first.append(r1c1x)
                first.append(r1c2x)
                first.append(r1c3x)
                aba = first.index(())
                if aba == 0:
                    x = 150
                    y = 150
                elif aba == 1:
                    x = 350
                    y = 150
                elif aba == 2:
                    x = 550
                    y = 150
            elif r2c1x and r2c2x != () and r2c3o == () or r2c1x and r2c3x != () and r2c2o == () or r2c2x and r2c3x != () and r2c1o == ():
                first = []
                first.append(r2c1x)
                first.append(r2c2x)
                first.append(r2c3x)
                aba = first.index(())
                if aba == 0:
                    x = 150
                    y = 350
                elif aba == 1:
                    x = 350
                    y = 350
                elif aba == 2:
                    x = 550
                    y = 350

            elif r3c1x and r3c2x != () and r3c3o == () or r3c1x and r3c3x != () and r3c2o == () or r3c2x and r3c3x != () and r3c1o == ():
                first = []
                first.append(r3c1x)
                first.append(r3c2x)
                first.append(r3c3x)
                aba = first.index(())
                if aba == 0:
                    x = 150
                    y = 550
                elif aba == 1:
                    x = 350
                    y = 550
                elif aba == 2:
                    x = 550
                    y = 550
            elif r1c1x and r2c1x != () and r3c1o == () or r1c1x and r3c1x != () and r2c1o == () or r2c1x and r3c1x != () and r1c1o == ():
                first = []
                first.append(r1c1x)
                first.append(r2c1x)
                first.append(r3c1x)
                aba = first.index(())
                if aba == 0:
                    x = 150
                    y = 150
                elif aba == 1:
                    x = 150
                    y = 350
                elif aba == 2:
                    x = 150
                    y = 550
            elif r1c2x and r2c2x != () and r3c2o == () or r1c2x and r3c2x != () and r2c2o == () or r2c2x and r3c2x != () and r1c2o == ():
                first = []
                first.append(r1c2x)
                first.append(r2c2x)
                first.append(r3c2x)
                aba = first.index(())
                if aba == 0:
                    x = 350
                    y = 150
                elif aba == 1:
                    x = 350
                    y = 350
                elif aba == 2:
                    x = 350
                    y = 550
            elif r1c3x and r2c3x != () and r3c3o == () or r1c3x and r3c3x != () and r2c3o == () or r2c3x and r3c3x != () and r1c3o == ():
                first = []
                first.append(r1c3x)
                first.append(r2c3x)
                first.append(r3c3x)
                aba = first.index(())
                if aba == 0:
                    x = 550
                    y = 150
                elif aba == 1:
                    x = 550
                    y = 350
                elif aba == 2:
                    x = 550
                    y = 550
            elif r1c1x and r2c2x != () and r3c3o == () or r1c1x and r3c3x != () and r2c2o == () or r2c2x and r3c3x != () and r1c1o == ():
                first = []
                first.append(r1c1x)
                first.append(r2c2x)
                first.append(r3c3x)
                aba = first.index(())
                if aba == 0:
                    x = 150
                    y = 150
                elif aba == 1:
                    x = 350
                    y = 350
                elif aba == 2:
                    x = 550
                    y = 550
            elif r3c1x and r2c2x != () and r1c3o == () or r3c1x and r1c3x != () and r2c2o == () or r1c3x and r2c2x != () and r3c1o == ():
                first = []
                first.append(r3c1x)
                first.append(r2c2x)
                first.append(r1c3x)
                aba = first.index(())
                if aba == 0:
                    x = 150
                    y = 550
                elif aba == 1:
                    x = 350
                    y = 350
                elif aba == 2:
                    x = 550
                    y = 150
            else:
                x = random.randint(0, 600)
                y = random.randint(0, 600)
        obj = canvas.find_overlapping(x, y, x, y)
        if x < 200 and y < 200 and obj == ():
            canvas.create_rectangle(0, 0, 199, 199, fill='black', tags="11o")
            canvas.create_oval(50, 50, 150, 150, outline='white')
        elif 200 < y < 400 and x < 200 and obj == ():
            canvas.create_rectangle(0, 201, 199, 399, fill='black', tags="12o")
            canvas.create_oval(50, 250, 150, 350, outline='white')
        elif 400 < y < 600 and x < 200 and obj == ():
            canvas.create_rectangle(0, 401, 199, 599, fill='black', tags="13o")
            canvas.create_oval(50, 450, 150, 550, outline='white')
        elif 200 < x < 400 and y < 200 and obj == ():
            canvas.create_rectangle(201, 0, 399, 199, fill='black', tags="21o")
            canvas.create_oval(250, 50, 350, 150, outline='white')
        elif 200 < x < 400 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(201, 201, 399, 399, fill='black', tags="22o")
            canvas.create_oval(250, 250, 350, 350, outline='white')
        elif 200 < x < 400 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(201, 401, 399, 599, fill='black', tags="23o")
            canvas.create_oval(250, 450, 350, 550, outline='white')
        elif 400 < x < 600 and y < 200 and obj == ():
            canvas.create_rectangle(401, 0, 599, 199, fill='black', tags="31o")
            canvas.create_oval(450, 50, 550, 150, outline='white')
        elif 400 < x < 600 and 200 < y < 400 and obj == ():
            canvas.create_rectangle(401, 201, 599, 399, fill='black', tags="32o")
            canvas.create_oval(450, 250, 550, 350, outline='white')
        elif 400 < x < 600 and 400 < y < 600 and obj == ():
            canvas.create_rectangle(401, 401, 599, 599, fill='black', tags="33o")
            canvas.create_oval(450, 450, 550, 550, outline='white')
        else:
            pass;
        r1c1o = canvas.find_withtag("11o")
        r2c1o = canvas.find_withtag("12o")
        r3c1o = canvas.find_withtag("13o")
        r1c2o = canvas.find_withtag("21o")
        r2c2o = canvas.find_withtag("22o")
        r3c2o = canvas.find_withtag("23o")
        r1c3o = canvas.find_withtag("31o")
        r2c3o = canvas.find_withtag("32o")
        r3c3o = canvas.find_withtag("33o")
        if r1c1o and r2c1o and r3c1o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c2o and r2c2o and r3c2o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c3o and r2c3o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c1o and r1c2o and r1c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r2c1o and r2c2o and r2c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r3c1o and r3c2o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c1o and r2c2o and r3c3o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        elif r1c3o and r2c2o and r3c1o != ():
            tk.after(1000)
            tk.destroy()
            return losescreen()
        else:
            if county + countx == 9:
                tk.destroy()
                return menu()
            else:
                pass;


def newgameasy():
    w.destroy()
    global canvas
    global tk
    canvas_width = 600
    canvas_height = 600
    tk = Tk()
    tk.title('Tic-Tac-Toe  Game')
    tk.geometry("600x600-95+60")
    tk.config(background='black')
    canvas = Canvas(tk, width=canvas_width, height=canvas_height, background='black')
    canvas.create_line(0, 200, 604, 200, fill='white')
    canvas.create_line(0, 400, 604, 400, fill='white')
    canvas.create_line(200, 0, 200, 604, fill='white')
    canvas.create_line(400, 0, 400, 604, fill='white')
    canvas.pack(expand=YES)
    canvas.bind("<Button-1>", callback)
    tk.bind("<Button-3>", easy)
    canvas.pack()
    mainloop()


def newgamehard():
    w.destroy()
    global canvas
    global tk
    canvas_width = 600
    canvas_height = 600
    tk = Tk()
    tk.title('Tic-Tac-Toe  Game')
    tk.geometry("600x600-95+60")
    tk.config(background='black')
    canvas = Canvas(tk, width=canvas_width, height=canvas_height, background='black')
    canvas.create_line(0, 200, 604, 200, fill='white')
    canvas.create_line(0, 400, 604, 400, fill='white')
    canvas.create_line(200, 0, 200, 604, fill='white')
    canvas.create_line(400, 0, 400, 604, fill='white')
    canvas.pack(expand=YES)
    canvas.bind("<Button-1>", callback)
    tk.bind("<Button-3>", hard)
    canvas.pack()
    mainloop()


def newgamemedium():
    w.destroy()
    global canvas
    global tk
    canvas_width = 600
    canvas_height = 600
    tk = Tk()
    tk.title('Tic-Tac-Toe  Game')
    tk.geometry("600x600-95+60")
    tk.config(background='black')
    canvas = Canvas(tk, width=canvas_width, height=canvas_height, background='black')
    canvas.create_line(0, 200, 604, 200, fill='white')
    canvas.create_line(0, 400, 604, 400, fill='white')
    canvas.create_line(200, 0, 200, 604, fill='white')
    canvas.create_line(400, 0, 400, 604, fill='white')
    canvas.pack(expand=YES)
    canvas.bind("<Button-1>", callback)
    tk.bind("<Button-3>", medium)
    canvas.pack()
    mainloop()


def close():
    top.destroy()


def closeask():
    w.destroy()


def askifeasy():
    top.destroy()
    global w
    w = Tk()
    w.geometry("400x200-800+120")
    w.config(background='black')
    L = Label(w, text='Are you sure you want to play in easy mode ?', fg='White', bg='black', font='avantgarde50')
    yes = Button(w, text="Yes ?", fg='White', bg='black', command=newgameasy, font='avantgarde50')
    no = Button(w, text="No ?", fg='White', bg='black', command=menu3, font='avantgarde50')
    ex = Button(w, text="Do you want to exit", fg='White', bg='black', command=close, font='avantgarde50')
    L.pack()
    yes.pack()
    no.pack()
    ex.pack()
    L.place(relx=0.5, rely=0.1, anchor=CENTER)
    yes.place(relx=0.3333333333, rely=0.4, anchor=CENTER)
    no.place(relx=0.66666666666, rely=0.4, anchor=CENTER)
    ex.place(relx=0.5, rely=0.7, anchor=CENTER)
    mainloop()


def askifmedium():
    top.destroy()
    global w
    w = Tk()
    w.geometry("400x200-800+120")
    w.config(background='black')
    L = Label(w, text='Are you sure you want to play in medium mode ?', fg='White', bg='black', font='avantgarde50')
    yes = Button(w, text="Yes ?", fg='White', bg='black', command=newgamemedium, font='avantgarde50')
    no = Button(w, text="No ?", fg='White', bg='black', command=menu3, font='avantgarde50')
    ex = Button(w, text="Do you want to exit", fg='White', bg='black', command=close, font='avantgarde50')
    L.pack()
    yes.pack()
    no.pack()
    ex.pack()
    L.place(relx=0.5, rely=0.1, anchor=CENTER)
    yes.place(relx=0.3333333333, rely=0.4, anchor=CENTER)
    no.place(relx=0.66666666666, rely=0.4, anchor=CENTER)
    ex.place(relx=0.5, rely=0.7, anchor=CENTER)
    mainloop()


def askifhard():
    top.destroy()
    global w
    w = Tk()
    w.geometry("400x200-800+120")
    w.config(background='black')
    L = Label(w, text='Are you sure you want to play in hard mode ?', fg='White', bg='black', font='avantgarde50')
    yes = Button(w, text="Yes ?", fg='White', bg='black', command=newgamehard, font='avantgarde50')
    no = Button(w, text="No ?", fg='White', bg='black', command=menu3, font='avantgarde50')
    ex = Button(w, text="Do you want to exit", fg='White', bg='black', command=close, font='avantgarde50')
    L.pack()
    yes.pack()
    no.pack()
    ex.pack()
    L.place(relx=0.5, rely=0.1, anchor=CENTER)
    yes.place(relx=0.3333333333, rely=0.4, anchor=CENTER)
    no.place(relx=0.66666666666, rely=0.4, anchor=CENTER)
    ex.place(relx=0.5, rely=0.7, anchor=CENTER)
    mainloop()


def menu():
    global top
    top = Tk()
    top.geometry("300x300-800+120")
    top.config(background='black')
    top.title('Menu')
    e = Button(top, text="Start game in easy mode ?", fg='White', bg='black', command=askifeasy, font='avantgarde50')
    m = Button(top, text="Start game in medium mode ?", fg='White', bg='black', command=askifmedium,
               font='avantgarde50')
    h = Button(top, text="Start game in hard mode ?", fg='White', bg='black', command=askifhard, font='avantgarde50')
    ex = Button(top, text='Do you want to exit ?', fg='White', bg='black', command=close, font='avantgarde50')
    L = Label(top, text='Welcome to Tic-Tac-Toe game', fg='White', bg='black', font='avantgarde50')
    e.pack()
    L.pack()
    m.pack()
    h.pack()
    ex.pack()
    L.place(relx=0.5, rely=0.1, anchor=CENTER)
    e.place(relx=0.45, rely=0.275, anchor=CENTER)
    m.place(relx=0.6, rely=0.450, anchor=CENTER)
    h.place(relx=0.45, rely=0.625, anchor=CENTER)
    ex.place(relx=0.7, rely=0.8, anchor=CENTER)
    mainloop()


def menu2():
    global top
    p.destroy()
    top = Tk()
    top.geometry("300x150-750+200")
    top.config(background='black')
    top.title('Menu')

    con = Button(top, text="Do you want to continue ?", fg='White', bg='black', command=menu4, font='avantgarde50')
    ex = Button(top, text='Do you want to exit ?', fg='White', bg='black', command=close, font='avantgarde50')
    L = Label(top, text='Are you enjoying Tic-Tac-Toe game?', fg='White', bg='black', font='avantgarde50')

    L.pack()
    con.pack()
    ex.pack()
    L.place(relx=0.5, rely=0.1, anchor=CENTER)
    con.place(relx=0.35, rely=0.45, anchor=CENTER)
    ex.place(relx=0.7, rely=0.8, anchor=CENTER)
    mainloop()


def menu3():
    w.destroy()
    global top
    top = Tk()
    top.geometry("300x300-800+120")
    top.config(background='black')
    top.title('Menu')
    e = Button(top, text="Start game in easy mode ?", fg='White', bg='black', command=askifeasy, font='avantgarde50')
    m = Button(top, text="Start game in medium mode ?", fg='White', bg='black', command=askifmedium,
               font='avantgarde50')
    h = Button(top, text="Start game in hard mode ?", fg='White', bg='black', command=askifhard, font='avantgarde50')
    ex = Button(top, text='Do you want to exit ?', fg='White', bg='black', command=close, font='avantgarde50')
    L = Label(top, text='Welcome to Tic-Tac-Toe game', fg='White', bg='black', font='avantgarde50')
    e.pack()
    L.pack()
    m.pack()
    h.pack()
    ex.pack()
    L.place(relx=0.5, rely=0.1, anchor=CENTER)
    e.place(relx=0.45, rely=0.275, anchor=CENTER)
    m.place(relx=0.6, rely=0.450, anchor=CENTER)
    h.place(relx=0.45, rely=0.625, anchor=CENTER)
    ex.place(relx=0.7, rely=0.8, anchor=CENTER)
    mainloop()


def menu4():
    global top
    top.destroy()
    top = Tk()
    top.geometry("300x300-800+120")
    top.config(background='black')
    top.title('Menu')
    e = Button(top, text="Start game in easy mode ?", fg='White', bg='black', command=askifeasy, font='avantgarde50')
    m = Button(top, text="Start game in medium mode ?", fg='White', bg='black', command=askifmedium,
               font='avantgarde50')
    h = Button(top, text="Start game in hard mode ?", fg='White', bg='black', command=askifhard, font='avantgarde50')
    ex = Button(top, text='Do you want to exit ?', fg='White', bg='black', command=close, font='avantgarde50')
    L = Label(top, text='Welcome to Tic-Tac-Toe game', fg='White', bg='black', font='avantgarde50')
    e.pack()
    L.pack()
    m.pack()
    h.pack()
    ex.pack()
    L.place(relx=0.5, rely=0.1, anchor=CENTER)
    e.place(relx=0.45, rely=0.275, anchor=CENTER)
    m.place(relx=0.6, rely=0.450, anchor=CENTER)
    h.place(relx=0.45, rely=0.625, anchor=CENTER)
    ex.place(relx=0.7, rely=0.8, anchor=CENTER)
    mainloop()


def winscreen():
    global p
    p = Tk()
    photo_path = "giphy.gif"
    photo = PhotoImage(file=photo_path)
    label = Label(p, image=photo)
    label.pack()
    p.after(2500, func=menu2)
    mainloop()


def losescreen():
    global p
    p = Tk()
    photo_path = "lose.gif"
    photo = PhotoImage(file=photo_path)
    label = Label(p, image=photo)
    label.pack()
    p.after(2000, func=menu2)
    mainloop()


def tiescreen():
    global p
    p = Tk()
    photo_path = "tie.gif"
    photo = PhotoImage(file=photo_path)
    label = Label(p, image=photo)
    label.pack()
    p.after(2000, func=menu2)
    mainloop()


menu()