def process_time(self):
        try:
            n = int(self.lineEdit.text())
            self.lineEdit_8.setStyleSheet("border-color: rgb(32, 31, 31);") #main border colour
            self.lineEdit_8.clear()
            self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
            self.lineEdit_6.clear()
            if n == 0:
                self.lineEdit_8.clear()
                self.lineEdit_8.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_8.insert("Invalid N")
                self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
                self.lineEdit_6.clear()
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        except:
            self.lineEdit_8.clear()
            self.lineEdit_8.setStyleSheet("border-color: rgb(255, 255, 127);") #Yellow Border Colour
            self.lineEdit_8.insert("Invalid N")
            self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
            self.lineEdit_6.clear()
            self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
            self.lineEdit_7.clear()
            return
        try:
            p_burst = []
            p_arrival = []
            p_name = []
            for i in range(n):
                p_name.append(str(self.tableWidget.item(i, 0).text()))
                for j in range(0, i):
                    if p_name[j] == p_name[i]:
                        self.lineEdit_6.clear()
                        self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                        self.lineEdit_6.insert("Repeated process name")
                        return
            for i in range(n):
                p_arrival.append(float(self.tableWidget.item(i, 1).text()))
            for i in range(n):
                p_burst.append(float(self.tableWidget.item(i, 2).text()))
                if p_burst[i] == 0:
                    self.lineEdit_6.clear()
                    self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                    self.lineEdit_6.insert("invalid burst time")
                    self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                    self.lineEdit_7.clear()
                    return
            self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
            self.lineEdit_6.clear()
        except:
            self.lineEdit_6.clear()
            self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
            self.lineEdit_6.insert("invalid process input")
            self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
            self.lineEdit_7.clear()
            return

        if self.comboBox.currentText() == self.comboBox.itemText(3):  # Round Robin
            try:
                q = float(self.lineEdit_2.text())
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                if q == 0:
                    self.lineEdit_7.clear()
                    self.lineEdit_7.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                    self.lineEdit_7.insert("Invalid Q")
                    return
            except:
                self.lineEdit_7.clear()
                self.lineEdit_7.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_7.insert("Invalid Q")
                return
        if self.comboBox.currentText() == self.comboBox.itemText(4) or self.comboBox.currentText() == self.comboBox.itemText(5):  # Priority Non_preemptive
            try:
                self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
                self.lineEdit_6.clear()
                p_priority = []
                for i in range(n):
                    p_priority.append(float(self.tableWidget.item(i, 3).text()))
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("invalid process input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        turtle.clearscreen()
        t = turtle.Turtle()
        text = 0
        w_time = 0
        t.speed(20)
        t.color("White")
        t.setheading(180)
        t.forward(400)
        t.color("Black")
        idle = 0
        idle_total = 0
        x = 0
        k = 0
        p_exc = 0
        m = 0
        if self.comboBox.currentText() == self.comboBox.itemText(0):  # FCFS
            try:
                for i in range(n):
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(1):  # SJF(NonPreemptive)
            try:
                for i in range(n):
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_burst[j] < p_burst[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                        if p_arrival[j] < text:
                            if p_burst[j] < p_burst[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                    text = text + p_burst[i]
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(2):  # sjf(Preemptive)
            try:
                for i in range(n):  # Non_Preemptive
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_burst[j] < p_burst[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                text = 0
                for i in range(n):
                    for j in range(i + 1, n):
                        if p_arrival[j] < text:
                            if p_burst[j] < p_burst[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                        if p_arrival[i] > text:
                            p_arr = text
                            p_exc = 0
                            while p_arr < p_arrival[i]:
                                p_arr = p_arr + 0.1
                                p_exc = p_exc + 0.1
                            text = text + p_exc
                        if p_arrival[j] > text and p_arrival[j] < text + p_burst[i]:
                            if p_burst[j] < p_burst[i]:
                                p_arr = text
                                p_exc = 0
                                while p_arr < p_arrival[j]:
                                    p_arr = p_arr + 0.1
                                    p_exc = p_exc + 0.1
                                p_burst[i] = p_burst[i] - p_exc
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                p_arrival.insert(i, p_arrival[j])
                                p_burst.insert(i, p_exc)
                                p_name.insert(i, p_name[j])
                                n = n + 1
                                m = m + 1
                    text = text + p_burst[i]
                for i in range(n):
                    if p_burst[i] == 0:
                        p_burst.pop(i)
                        p_arrival.pop(i)
                        p_name.pop(i)
                        n = n - 1
                        m = m - 1
                    else:
                        continue
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    for j in range(i + 1, n):
                        if p_name[i] == p_name[j]:
                            index = i
                            p_arrival[j] = p_arrival[j] + p_burst[i]
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / (n - m)
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(3):  # Round Robin
            try:
                if q < 3:
                    coff = 15
                elif q < 5:
                    coff = 10
                elif q <= 10:
                    coff = 7
                elif q < 50:
                    coff = 5
                else:
                    coff = 3
                m = []
                for i in range(n):
                    for j in range(i + 1, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                text = 0
                count = n
                m = 0
                w_time = 0
                while count > 0:
                    count = n
                    for i in range(n):
                        if p_burst[i] == 0:
                            continue
                        if p_burst[i] < q and p_burst[i] <= text:
                            if text == 0:
                                t.setheading(270)
                                t.forward(30)
                                t.color("Black")
                                style = ('Courier', 12)
                                t.write("0", font=style)
                                t.color("White")
                                t.setheading(90)
                                t.forward(30)
                            t.color("Black")
                            t.setheading(0)
                            t.forward(5 * p_burst[i])
                            t.setheading(90)
                            t.forward(50)
                            t.setheading(180)
                            t.forward(5 * p_burst[i])
                            t.setheading(270)
                            t.forward(50)
                            t.setheading(0)
                            t.forward(5 * p_burst[i])
                            text = text + p_burst[i]
                            text = round(text, 2)
                            t.color("White")
                            t.setheading(270)
                            t.forward(30)
                            t.setheading(180)
                            t.forward(20)
                            t.color("Black")
                            style = ('Courier', 12)
                            t.write(text, font=style)
                            t.color("White")
                            t.setheading(0)
                            t.forward(20)
                            t.setheading(90)
                            t.forward(30)
                            t.setheading(180)
                            t.forward(4 * p_burst[i])
                            t.setheading(90)
                            t.forward(10)
                            t.color("Black")
                            style = ('Courier', 20)
                            t.write(p_name[i], font=style)
                            t.color("White")
                            t.setheading(270)
                            t.forward(10)
                            t.color("Black")
                            t.setheading(0)
                            t.forward(4 * p_burst[i])
                            t.color("Black")
                            w_time = w_time + (text - p_burst[i] - p_arrival[i])
                            p_burst[i] = 0
                            m = m + 1
                            continue
                        zizo = 0
                        for j in range(0, i):
                            if p_burst[j] != 0:
                                zizo = zizo + 1
                        if p_arrival[i] > text and zizo != 0:
                            continue
                        if p_arrival[i] > text:
                            idle = p_arrival[i] - text
                            text_idle = text + idle
                            t.color("Red")
                            t.setheading(0)
                            t.forward(5 * idle)
                            t.setheading(90)
                            t.forward(50)
                            t.setheading(180)
                            t.forward(5 * idle)
                            t.setheading(270)
                            t.forward(50)
                            t.setheading(0)
                            t.forward(5 * idle)
                            t.color("White")
                            t.setheading(270)
                            t.forward(30)
                            t.color("Red")
                            style = ('Courier', 12)
                            text_idle = round(text_idle, 2)
                            t.write(str(text_idle), font=style)
                            t.color("White")
                            t.setheading(90)
                            t.forward(30)
                            t.setheading(180)
                            t.forward(4.5 * idle)
                            t.setheading(90)
                            t.forward(10)
                            t.color("Red")
                            style = ('Courier', 12)
                            t.write("IDLE", font=style)
                            t.color("White")
                            t.setheading(270)
                            t.forward(10)
                            t.color("Red")
                            t.setheading(0)
                            t.forward(4.5 * idle)
                            idle_total = idle_total + idle
                            text = text + idle
                        t.color("Black")
                        t.setheading(0)
                        t.forward(coff * q)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(coff * q)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(coff * q)
                        text = text + q  # text
                        text = round(text, 2)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(15)
                        t.color("Black")
                        style = ('Courier', 12)
                        t.write(text, font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(0)
                        t.forward(15)
                        t.setheading(180)
                        t.forward((coff - 1) * q)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Black")
                        style = ('Courier', 20)
                        t.write(p_name[i], font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Black")
                        t.setheading(0)
                        t.forward((coff - 1) * q)
                        w_time = w_time + (text - q - p_arrival[i])
                        t.color("Black")
                        p_burst[i] = p_burst[i] - q
                        p_arrival[i] = text
                        m = m + 1
                        p_arrival[i] = text
                    for i in range(n):
                        if p_burst[i] == 0:
                            count = count - 1
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(4):  # Priority Non_preemptive
            try:
                for i in range(n):
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                            temp_priority = p_priority[i]
                            p_priority[i] = p_priority[j]
                            p_priority[j] = temp_priority
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_priority[j] < p_priority[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                        if p_arrival[j] < text:
                            if p_priority[j] < p_priority[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 15)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 15)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                    text = 0
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    while index >= 0:
                        text = text + p_burst[index]
                        index = index - 1
                    text = text + idle_total
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(15)
                    t.color("Black")
                    style = ('Courier', 12)
                    text = round(text, 2)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(0)
                    t.forward(15)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                    t.color("Black")
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(5):  # priority(Preemptive)
            try:
                p_priority = [float(self.tableWidget.item(0, 3).text())]
                for i in range(n - 1):
                    p_priority.append(float(self.tableWidget.item(i + 1, 3).text()))
                for i in range(n):  # Non_Preemptive
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                            temp_priority = p_priority[i]
                            p_priority[i] = p_priority[j]
                            p_priority[j] = temp_priority
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_priority[j] < p_priority[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                text = 0
                for i in range(n):
                    for j in range(i + 1, n):
                        if p_arrival[j] <= text:
                            if p_priority[j] < p_priority[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                        if p_arrival[i] > text:
                            p_arr = text
                            p_exc = 0
                            while p_arr < p_arrival[i]:
                                p_arr = p_arr + 0.5
                                p_exc = p_exc + 0.5
                            text = text + p_exc
                        if p_arrival[j] > text and p_arrival[j] < text + p_burst[i]:
                            if p_priority[j] < p_priority[i]:
                                p_arr = text
                                p_exc = 0
                                while p_arr < p_arrival[j]:
                                    p_arr = p_arr + 0.1
                                    p_exc = p_exc + 0.1
                                p_burst[i] = p_burst[i] - p_exc
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                                p_arrival.insert(i, p_arrival[j])
                                p_burst.insert(i, p_exc)
                                p_name.insert(i, p_name[j])
                                p_priority.insert(i, p_priority[j])
                                n = n + 1
                                m = m + 1
                    text = text + p_burst[i]
                for i in range(n):
                    if p_burst[i] == 0:
                        p_burst.pop(i)
                        p_arrival.pop(i)
                        p_name.pop(i)
                        p_priority.pop(i)
                        n = n - 1
                        m = m - 1
                    else:
                        continue
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    for j in range(i + 1, n):
                        if p_arrival[j] <= text:
                            if p_priority[j] < p_priority[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    for j in range(i + 1, n):
                        if p_name[i] == p_name[j]:
                            index = i
                            p_arrival[j] = p_arrival[j] + p_burst[i]
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / (n - m)
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
