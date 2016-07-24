'''
import cx_Freeze
from cx_Freeze import setup, Executable
executables = [cx_Freeze.Executable("first.py")]

cx_Freeze.setup(
    name="A bit Racey",
    version="1.1",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )
'''
from distutils.core import setup
import py2exe

setup(windows=['pygame1.py'])
