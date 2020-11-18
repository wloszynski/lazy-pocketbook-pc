import paramiko
import keyboard
from plyer import notification
import time

try:
    keyboard.add_hotkey("ctrl+alt+1", lambda: ssh.exec_command(forward))
    keyboard.add_hotkey("ctrl+alt+2", lambda: ssh.exec_command(backward))
    keyboard.add_hotkey("ctrl+alt+3", lambda: ssh.exec_command(home))
    keyboard.add_hotkey("ctrl+alt+4", lambda: ssh.exec_command(option))
except Exception:
    print('Keyboard problems')

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

keyboard.wait()

running = True

while running:
    time.sleep(0.1)
    if(ssh.get_transport().is_active() == False):
        print('Lack of connection, session aborted')
        print('\007')
        notification.notify(
            title = 'Lack of connection, session aborted',
            timeout = 2
        )
        exit()
        break
