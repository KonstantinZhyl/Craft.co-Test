import re
import csv
import sys


file = open(sys.argv[-2], "r")
content = file.read()
file.close()

tags = re.findall(r"<tr>[\s\S]+?data-event-category=\"Job Link\"[\s\S]+?</tr>", content)   # finds rows in table

vacancies = []
for i in tags:
    tmp = re.findall(r">\s*([^<>]*?\w[^<>]*?)\s*?<" , i)        # finds info in rows
    for i in range(3, len(tmp)):                                # in case of multiple locations for that vacancy
        vacancies.append([tmp[0], tmp[1], tmp[2], tmp[i]])

with open(sys.argv[-1], 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['Job Title', 'Category', 'Status', 'Location'])
    for vacancy in vacancies:
        spamwriter.writerow([x.replace("&amp;", "&") for x in vacancy])

print("Done")
