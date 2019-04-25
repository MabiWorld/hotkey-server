# Mabinogi Hotkey Server #

For when mabiui.nexon.net is down.

These instructions are written for Windows 10. If you're not running Windows 10, I feel bad for you.

These instructions and this software come with no guarantee or support. Use at your own risk.


## Setup ##

1. In the Cortana menu, search cmd
2. Right-click Command Prompt and Run as administrator
3. Type this in the console: `echo 127.0.0.1 mabiui.nexon.net >> C:\Windows\System32\drivers\etc\hosts`
4. Install the latest Python 3 release from [here](https://www.python.org/downloads/windows/)
5. Double-click `hotkey-server.py`
6. A console window should appear that says `Started local hotkey server...` if one does not you screwed something up.

The server must be running before you enter a game server in Mabinogi *every time*.


## Tear down ##

When `mabiui.nexon.net` is back up you need to remove the entry from your hosts file that we did.

1. In the Cortana menu, search notepad
2. Right-click Notepad and Run as administrator
3. Go to File -> Open and in the `File name` field at the bottom of the window, paste the path `C:\Windows\System32\drivers\etc\hosts`
4. The last line of your file will say `127.0.0.1 mabiui.nexon.net`
5. Delete that line only
6. File -> Save

You should be able to connect to the official server again.
