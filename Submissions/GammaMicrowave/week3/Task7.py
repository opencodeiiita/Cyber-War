import subprocess

# checks info stored in systeminfo then decodes it in our readable format and using split to show
# each info on a new line.
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []
# splitting key and value apart in such a way that it looks clean.
for item in Id:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    print(i[2:-2])
