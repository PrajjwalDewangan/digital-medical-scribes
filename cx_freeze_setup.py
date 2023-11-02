import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["flet", "torch"], "includes": ["sys"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="guifoo",
    version="0.1",
    description="Transcriber",
    options={"build_exe": build_exe_options},
    executables=[Executable("transcriber.py", base=base, icon="icon.ico")],
)