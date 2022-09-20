from pymem import *

inputs = input("Enter the DLL PATH and process name to inject: ").split(' ')
dll_path = inputs[0]
dll_path_bytes = bytes(dll_path, "UTF-8")
process_name=inputs[1]

open_process = Pymem(process_name)
process.inject_dll(open_process.process_handle, dll_path_bytes)
print('DLL successfully injected')
