from bluebird import BlueBird
import csv

query = {
    'fields': [
        {'items': ['مصر']},
        {'items': ['أمريكا'], 'match': 'none'},
    ],
    'lang': 'ar',
    'since': '2011-01-01',
    'until': '2021-01-01'
}

# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
for tweet in BlueBird().search(query, deep=True):
    csvWriter.writerow([tweet])
    print(tweet)
