from tqdm import tqdm
import zipfile

wordlist = "rockyou.txt"
zip_file = "zipp.zip"

zip_file = zipfile.ZipFile(zip_file)

nwords = len(list(open(wordlist,"rb")))

print("Total passwords to test:",nwords)

with open(wordlist,"rb") as wordlist:
	for word in tqdm(wordlist,total = nwords, unit = "word"):
		try:
			zip_file.extractall(pwd=word.strip())
		except:
			continue
		else:
			print("Password found:", word.decode().strip())
			exit(0)
print("Password not found")
