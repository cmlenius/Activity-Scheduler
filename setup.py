import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Activity_Scheduler",
    version = "1.0",
    description = "cx_Freeze Activity_Scheduler",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Activity_Scheduler.py", base=base)])
