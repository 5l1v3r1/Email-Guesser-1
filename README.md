# Email Guesser
 A simple python program that guesses the emails of potential leads

### How it works?
This program/script looks at each lead and tries to find the domain(website url) using the company name. Based on the data returned, it guesses the email on the basis of ‘firstname.lastname@domain.com’. The use of this script circumvents having to manually google each company and select the first link that shows up as the domain.

The output result of this program can then be uploaded to an online email validity checker (such as https://www.emailhippo.com/) and the ones marked as valid can be used in marketing campaigns or to generate leads.

<A demo is in the works to be published soon. ;)>


### Current Dependencies and their pip installation commands:
- Beautiful Soup      | pip install beautifulsoup4
- Google              | pip install google
- Pandas              | pip install pandas
- XLRD                | pip install xlrd
- Openpyxl            | pip install openpyxl


### Current state and future roadmap:
The program isn't perfect as occasionally, it incorrectly identifies the domain of a company. I quickly hacked it together in an evening for the marketing department of a company I work at.
In future iterations of the program, i'lll try and improve the domain detection portion of the software to a reasonably good level. Later on, a GUI would be developed to facilitate use of the program for outside users.

- [x] Setup repo and commit initial program
- [ ] Optimise domain identification portion of code
- [ ] Create Graphical User Interface (GUI)
