import paramiko
import pyxhook
from plyer import notification

# Alt_L 233
# Control_L 227
# Shift_L 225


def OnKeyPress(event):
    global ctrl_on
    global alt_on

    print (event.Key, event.Ascii)

    if event.Ascii == 227:
        ctrl_on = True
    elif event.Ascii == 233:
        if ctrl_on:
            alt_on = True
    elif event.Ascii == 49:
        if ctrl_on and alt_on:
            ssh.exec_command(forward)
            ctrl_on = False
            alt_on = False
    elif event.Ascii == 50:
        if ctrl_on and alt_on:
            ssh.exec_command(backward)
            ctrl_on = False
            alt_on = False
    elif event.Ascii == 51:
        if ctrl_on and alt_on:
            ssh.exec_command(home)
            ctrl_on = False
            alt_on = False
    elif event.Ascii == 52:
        if ctrl_on and alt_on:
            ssh.exec_command(option)
            ctrl_on = False
            alt_on = False

try:
    
    host = '169.254.0.1'
    port = 22
    username = 'root'
    password = '1257'

    forward = 'cat f.txt > /dev/input/event0'
    backward = 'cat b.txt > /dev/input/event0'
    home = 'cat h.txt > /dev/input/event0'
    option = 'cat o.txt > /dev/input/event0'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, port, username, password)

    print('Connected to PocketBook')
    print('\007')
    notification.notify(
        title = 'Connected To PocketBook',
        timeout = 2
    )


except Exception:
    print('Lack of connection, session aborted')
    print('\007')
    notification.notify(
        title = 'Lack of connection, session aborted',
        timeout = 2
    )
    exit()
ctrl_on = False
alt_on = False

hm = pyxhook.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()
 