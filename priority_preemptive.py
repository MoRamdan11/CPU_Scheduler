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
