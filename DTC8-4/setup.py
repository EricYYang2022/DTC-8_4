import cx_Freeze


import os.path

includefiles = []
includes = []
excludes = []
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

#// set TCL_LIBRARY=C:\Users\VergilTheHuragok\AppData\Local\Programs\Python\Python35\tcl\tcl8.6  
#// set TK_LIBRARY=C:\Users\VergilTheHuragok\AppData\Local\Programs\Python\Python35\tcl\tk8.6)

executables = [cx_Freeze.Executable("PostArduino.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           'includes': ["tkinter"],
                           "include_files":["music.png",
                                            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),]}},
    executables = executables

    )
