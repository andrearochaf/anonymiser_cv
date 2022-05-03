from exchanges import extract_pdf
from exchanges import create_pdf
import re

path_to_pdf = "ar.pdf"

mail = re.sub(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+" , " ", extract_pdf(path_to_pdf),flags=re.IGNORECASE)

address_identifier=["rue","boulevard","impasse","voie","chemin","allée","allee","av","bd"]
adress = rf"[0-9]+\s*({'|'.join(address_identifier)})\s*.*"
adresses = re.sub(adress, " ", mail,flags=re.IGNORECASE)


zipcode = re.sub(r".*\d{5}.*", " ", adresses, flags=re.IGNORECASE)


phonenumber = re.sub(r"([\0-9]{10,20})" , " ", zipcode, flags=re.IGNORECASE)
print(phonenumber)

date1 = r"([2-9]|1[0-2]?)/[0-3][1-9]/[1-2][9|0][0-9]{2}"
date2 = r"\d{2}-\d{2}-\d{4}"
date3 = r"\d{2}.\d{2}.\d{4}"
date4 = r"\d{4}"
date5 = r"[a-zA-Z]+ [0-9]{4}"
year = r"[0-9]{4}"
dates = re.sub(year, " ", phonenumber, flags=re.IGNORECASE)

create_pdf(dates, "new", 10)