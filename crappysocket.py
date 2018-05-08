from irclog import HOST,PORT,PASS,NICK,MODT,readbuffer
import socket, string


# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #creepytrash \r\n")
