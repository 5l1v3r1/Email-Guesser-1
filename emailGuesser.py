#cd Dropbox/Bridge\ \(WorkAccounts\ -\ Personal\)/STL\ Partners/0\ -\ DevWork/
import pandas
from googlesearch import search

excelFile = 'Sample Data.xlsx'
found = 0

try:
    workBook = pandas.ExcelFile(excelFile)
    ##Code that checks whether the sheet name 'RawCleaned' exists
    for sheet in workBook.sheet_names:
        rcSheet = 0

        if(sheet == 'RawCleaned'):
            rcSheet = 1
            break
    None if (rcSheet == 1) else (print("'RawCleaned' sheet not found") & exit())

except FileNotFoundError:  
    print("The file '"+ excelFile +"' does not exist in the current directory.")
    exit()

dataframe = pandas.read_excel(workBook, 'RawCleaned')
print(dataframe)

#To do: Write code that checks that the three required data headers (firstN, lastN and company) are in the file

companyList = list(dataframe['Company'])
website = []
emailDomain = []
guessedEmails = []

#Searching of the company domain
print("Domain retrieval in progress...")
num = 1
for company in companyList:
    for link in search(company, tld="com", num=10, stop=1, pause=2): 
        website.append(link)
        #cleaned domain
        link = link.replace("https://www.", "")
        link = link.replace("https://", "")
        link = link.replace("http:", "")
        emailDomain.append(link)
    print("Domain "+ str(num) +" of " +str(len(companyList))+ " retrieved..")
    num += 1
print("Domain retrieval Completed")
dataframe['Website'] = website
dataframe['Email Domain'] = emailDomain

"""
#Guessing the emails by combining first name, last name and email domain
for i in range(0, len(dataframe)):
    guessedEmail = dataframe['First Name'][i] +"."+ dataframe['Last Name'][i] +"@"+ dataframe['Email Domain'][i]
    print(guessedEmail)
    guessedEmails.append(guessedEmail)
dataframe['Guessed emails'] = guessedEmails
"""

#dataframe = dataframe.drop(['Email Domain'], axis = 1)
print(dataframe)

dataframe.to_excel(excel_writer = 'egOutput.xlsx' , sheet_name='Output', index=False)