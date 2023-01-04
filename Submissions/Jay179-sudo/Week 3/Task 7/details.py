import platform

my_system = platform.uname()
print("The system details are given below: ")
print(f"System: {my_system.system}")
print(f"Machine: {my_system.machine}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
