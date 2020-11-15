import paramiko

host = '169.254.0.1'
port = 22
username = 'root'
password = '1257'

forward = 'cat f.txt > /dev/input/event0'
backward = 'cat f.txt > /dev/input/event0'
home = 'cat h.txt > /dev/input/event0'
option = 'cat o.txt > /dev/input/event0'

command = forward

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)

line = stdout.readlines()

print(line)