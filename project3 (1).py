#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import socket
from threading import Thread


def listening():
    while True:
        (message, address) = sock.recvfrom(2048)
        output_label.insert(END, message.decode('utf-8') + '\n')


def sending():
    a = message_entry.get()
    b = name_entry.get()
    data = b + ':' + a
    sock.sendto(data.encode('utf-8'), (destination_ip_entry.get(),
                int(destination_port_entry.get())))
    output_label.insert(END, b + ': ' + a + '\n')


def begin_listening():
    global sock, listen_thread, desination_port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', int(listening_port_entry.get())))
    listen_thread = Thread(target=listening)
    listen_thread.start()
    output_label.insert(END, 'Now listening on '
                        + listening_port_entry.get() + '. \n')


root = Tk()
root.title('CMSCI 355 UDP Chat')

conn_frame = Frame()

# Change all labels to have conn_frame

message_entry = Entry(conn_frame, width=50)

listening_port_label = Label(conn_frame, text='Listening Port',
                             font=('Times', 12))
listening_port_entry = Entry(conn_frame, width=10)
listening_port_entry.bind('<Return>', lambda e=0: begin_listening())

destination_port_label = Label(conn_frame, text='Destination Port',
                               font=('Times', 12))
destination_port_entry = Entry(conn_frame, width=14)

destination_ip_label = Label(conn_frame, text='Destination ip',
                             font=('Times', 12))
destination_ip_entry = Entry(conn_frame, width=14)

name_label = Label(conn_frame, text='Name', font=('Times', 12))
name_entry = Entry(conn_frame, width=14)

output_label = ScrolledText(height=12, width=24, font=('Times', 12))

# Changed conn_frame to font.

message_entry.grid(row=0, column=0, columnspan=6)
conn_frame.grid(row=0, column=1)
message_entry.bind('<Return>', lambda e=0: sending())
output_label.grid(row=1, column=0, columnspan=2, rowspan=5)

listening_port_label.grid(row=1, column=3)
listening_port_entry.grid(row=1, column=4)

destination_port_label.grid(row=2, column=3)
destination_port_entry.grid(row=2, column=4)

destination_ip_label.grid(row=3, column=3)
destination_ip_entry.grid(row=3, column=4)

name_label.grid(row=4, column=3)
name_entry.grid(row=4, column=4)

root.mainloop()
