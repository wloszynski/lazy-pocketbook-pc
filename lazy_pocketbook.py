import paramiko
import pyxhook

try:
    host = 'ip'
    port = 22
    username = 'root'
    password = 'password'

    forward = 'cat f.txt > /dev/input/event0'
    backward = 'cat b.txt > /dev/input/event0'
    home = 'cat h.txt > /dev/input/event0'
    option = 'cat o.txt > /dev/input/event0'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, port, username, password)

    print('Connected')

except Exception:
    print('Lack of connection, session aborted')
    exit()


def OnKeyPress(event):
    print (event.Key)

    # press 1 to forward
    if event.Ascii == 49:
        ssh.exec_command(forward)
    # press 2 to backward
    elif event.Ascii == 50:
        ssh.exec_command(backward)
    # press 3 to home
    elif event.Ascii == 51:
        ssh.exec_command(home)
    # press 4 to option
    elif event.Ascii == 52:
        ssh.exec_command(option)
    # press 5 to exit
    elif event.Ascii == 53:
        exit()


hm = pyxhook.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()
