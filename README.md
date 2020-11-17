# LazyPocketBook PC
LazyPocketBook is an app that allows you to change pages remotely on your PocketBook e-reader.

# INSTALLATION GUIDE
To use LazyPocketBook you must install Python and some Python modules.
Make sure you have Python3 installed.
1. Install paramiko, pyxhook and plyer modules.

* `pip3 install paramiko`
* `pip3 install pyxhook`
* `pip3 install plyer`

2. Download repository
* Extract repository files on your desktop
* Extract pb_jailbreak.zip
3. Connect PocketBook to PC
* Open your file explorer
* Turn on viewing hidden files (on Ubuntu it is Ctrl+h)
* Copy Jailbreak.app and Services.app to your PocketBook Applications folder.
4. Then from your PocketBook menu
* Launch @Jailbreak. If it succeeds, it will install root su. It does nothing else. Running it again will undo root.
* Launch @Services. This will install the system services, kernel modules, settings menus etc. su must be installed. If jailbreak is missing, the app will silently fail to run. Running it again will undo the install.

Once the device boots after Services install, new menu entry 'Rooted device settings' should appear in settings menu. In it, it will show generated root password, you can change it to your own too.

5. Connect your PC and PocketBook to the same WiFi network.
6. Once the device boots after Services install, new menu entry 'Rooted device settings' should appear in settings menu. In it, it will show generated root password. Remember the password.
7. Using terminal connect via ssh to your PocketBook
* `ssh root@169.254.0.1`
* When it ask you for password enter it
* Now in your ssh terminal type
* `cat /dev/input/event0 > f.txt`
* press forward button on your PocketBook
* then press CTRL+C on PC
* now do the same thing for backward, home and options
* `cat /dev/input/event0 > b.txt`
* press backward button on your PocketBook
* then press CTRL+C on PC
* `cat /dev/input/event0 > h.txt`
* press home button on your PocketBook
* then press CTRL+C on PC
* `cat /dev/input/event0 > o.txt`
* press option button on your PocketBook
* then press CTRL+C on PC
8. Now exit the SSH with CTRL+D
9. Run Python lazy_pocketbook_linux.py script
* `python3 ./lazy_pocketbook_linux.py`
10. Now you can control your PocketBook remotely.

# Remember
* Your PC and PocketBook must be connected to the same network.
* Your PocketBook must be turned ON when you are launching the script.

# KeyBindings
* FORWARD = CTRL + ALT + 1
* BACKWARD = CTRL + ALT + 2
* HOME = CTRL + ALT + 3
* OPTIONS = CTRL + ALT + 4


# TO DO 
1. Checking if ssh is active, if not exit()
2. ~~Key combination (for exampla ctrl+arrow_up, to go forward etc.)~~
3. Make it more user friendly
4. ~~Create version for Windows (pyxhook works only on linux, pyhook works on Windows)~~, 'keyboard' module works on both but there is a need for sudo/admin, and I have some import problems with that module.
