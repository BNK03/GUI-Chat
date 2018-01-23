# GUI-Chat
Gui Chat interface in Python

1. The program has GUI with places where users enter their name, source port, destination
port, and destination IP, as well as a place to enter messages and a place to display messages.

2. Communication happens over UDP.

3. Each user starts up the program, enters the connection parameters, and then indicates they are
ready to start listening. This then starts up a thread that continually listens for
incoming data on the specified port number.

4. After that, when a user enters something in the message entry box and presses enter, their message
along with their name should be displayed in both their message display area and in the message
display area on the other side of the connection.

Collaboration Project
