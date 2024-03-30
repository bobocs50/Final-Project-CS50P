import sys
import pyfiglet
import csv
from fpdf import FPDF
import os



"""

Title; ExpenseTracker
Name; Ngoc Hwang Philipp Huynh
GitHub n edX usernames; both bobocs50
city n country; Buchen, Germany
date; 28.2.24



"""






lsLimit= []
lsData= []
lsFixed= []
dctData = {}
dctFixedValue = {}
dctFixedKey = {}

currency_dict = {
    'USD': 'USD',
    'EUR': 'EUR',
    'GBP': 'GBP',
    'JPY': 'JPY',
    'CNY': 'CNY',
    'AUD': 'AUD',
    'CAD': 'CAD',
    'CHF': 'CHF',
    'INR': 'INR',
    'SGD': 'SGD',
    'HKD': 'HKD',
    'NZD': 'NZD',
    'KRW': 'KRW',
    'SEK': 'SEK',
    'NOK': 'NOK'
}


class PDF(FPDF):
    def __init__(self, dctFixedKey=None, dctFixedValue=None, currency= None, totalFixed=None, limit=None, MoneyLeft=None, MoneySpent=None, weeklyLimit=None,newLimit=None, week1Data=None, week2Data=None, week3Data=None, week4Data=None):
        super().__init__()
        self.dctFixedKey = dctFixedKey
        self.dctFixedValue = dctFixedValue
        self.totalFixed = totalFixed
        self.limit = limit
        self.MoneyLeft = MoneyLeft
        self.MoneySpent = MoneySpent
        self.newLimit = newLimit
        self.week1Data = week1Data
        self.week2Data = week2Data
        self.week3Data = week3Data
        self.week4Data = week4Data
        self.currency = currency

    def header(self):
        self.set_font("helvetica", "B", 25)
        #calculae width of cell
        width = self.get_string_width("Dashboard") + 6
        self.set_x((210 - width) / 2)
        #Colors for header
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        #text
        self.cell(width, 14, "Dashboard", border=1, align="C", fill=True)
        self.ln(20)

    def fix(self, totalFixed, currency):
        #Header Fixed Expenses
        self.ln(5)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(40, 7, "Fixed Expenses", border= 1, align= "C", fill=True)
        self.ln(10)
        #get length of fixed DCT
        lenWords = len(dctFixedKey)
        #first fixed expenses
        self.set_font("arial", "B", 10)
        for n in range(lenWords):
            key = f"FixedKey{n+1}"
            value = f"FixedValue{n+1}"
            self.set_text_color(0, 0, 0)
            self.cell(40, 7, f"{dctFixedKey[key].capitalize()}: {dctFixedValue[value]} {currency}")
            self.ln(4)
        #total fixed expenses
        self.ln(2)
        self.set_text_color(0, 0, 0)
        self.cell(40, 4, f"total: {totalFixed} {currency}", border=1)


    def week1(self,week1Data,currency):
        self.ln(12)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 68.00125)
        self.cell(40, 7, "Week 1", border= 1, align= "C", fill=True)

        #week1 expenses
        self.ln(10)
        self.set_text_color(0, 0, 0)
        self.set_font("arial", "B", 10)
        self.cell(40, 7, f"Food: {(dctData['dataValue1'])} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Transportation: {(dctData['dataValue2'])} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Personal care: {(dctData['dataValue3'])} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Recreation: {(dctData['dataValue4'])} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Misc: {(dctData['dataValue5'])} {currency}")
        self.ln(6)
        self.cell(40, 4, f"total: {week1Data} {currency}", border=1)

    def week2(self,week2Data,currency):
        self.set_y(68.00125)
        self.set_x(110)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(40, 7, "Week 2", border= 1, align= "C", fill=True)
        #week 2 expenses
        self.set_text_color(0, 0, 0)
        self.set_font("arial", "B", 10)
        self.set_y(78.00125)
        self.set_x(110)
        self.cell(40, 7, f"Food: {dctData.get('dataValue6', '')} {currency}")
        self.set_y(82.00125)
        self.set_x(110)
        self.cell(40, 7, f"Transportation: {dctData.get('dataValue7', '')} {currency}")
        self.set_y(86.00125)
        self.set_x(110)
        self.cell(40, 7, f"Personal care: {dctData.get('dataValue8', '')} {currency}")
        self.set_y(90.00125)
        self.set_x(110)
        self.cell(40, 7, f"Recreation: {dctData.get('dataValue9', '')} {currency}")
        self.set_y(94.00125)
        self.set_x(110)
        self.cell(40, 7, f"Misc: {dctData.get('dataValue10', '')} {currency}")
        self.set_y(100.00125)
        self.set_x(110)
        self.cell(40, 4, f"total: {week2Data} {currency}", border=1)

    def week3(self, week3Data,currency):
        self.ln(8)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(40, 7, "Week 3", border= 1, align= "C", fill=True)

         #week1 expenses
        self.ln(10)
        self.set_text_color(0, 0, 0)
        self.set_font("arial", "B", 10)
        self.cell(40, 7, f"Food: {dctData.get('dataValue11', '')} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Transportation: {dctData.get('dataValue12', '')} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Personal care: {dctData.get('dataValue13', '')} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Recreation: {dctData.get('dataValue14', '')} {currency}")
        self.ln(4)
        self.cell(40, 7, f"Misc: {dctData.get('dataValue15', '')} {currency}")
        self.ln(6)
        self.cell(40, 4 , f"total: {week3Data} {currency}", border=1)

    def week4(self, week4Data,currency):
        self.set_y(108.00125)
        self.set_x(110)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(40, 7, "Week 4", border= 1, align= "C", fill=True)
        #expenses
        self.set_text_color(0, 0, 0)
        self.set_font("arial", "B", 10)
        self.set_y(118.00125)
        self.set_x(110)
        self.cell(40, 7, f"Food: {dctData.get('dataValue6', '')} {currency}")
        self.set_y(122.00125)
        self.set_x(110)
        self.cell(40, 7, f"Transportation: {dctData.get('dataValue7', '')} {currency}")
        self.set_y(126.00125)
        self.set_x(110)
        self.cell(40, 7, f"Personal care: {dctData.get('dataValue8', '')} {currency}")
        self.set_y(130.00125)
        self.set_x(110)
        self.cell(40, 7, f"Recreation: {dctData.get('dataValue9', '')} {currency}")
        self.set_y(134.00125)
        self.set_x(110)
        self.cell(40, 7, f"Misc: {dctData.get('dataValue10', '')} {currency}")
        self.set_y(140.00125)
        self.set_x(110)
        self.cell(40, 4, f"total: {week4Data} {currency}", border=1)

    def weeklyLimit(self, weeklyLimit,currency):
        self.ln(30)
        width = self.get_string_width("Dashboard") + 40
        self.set_x((210 - width) / 2)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(width, 7, "Weekly limit", border= 1, align= "C", fill=True)
        #limit
        self.ln(10)
        width = self.get_string_width("Dashboard") + 6
        self.set_x((210 - width) / 2)
        self.set_font("arial", "B", 10)
        self.set_text_color(0, 0, 0)
        self.cell(width, 7, f"Weekly limit: {weeklyLimit} {currency}")

    def Setlimit(self, limit,currency):
        self.ln(10)
        width = self.get_string_width("Dashboard") + 40
        self.set_x((210 - width) / 2)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(width, 7, "Limit", border= 1, align= "C", fill=True)
        #limit
        self.ln(10)
        width = self.get_string_width("Dashboard")
        self.set_x((210 - width) / 2)
        self.set_font("arial", "B", 10)
        self.set_text_color(0, 0, 0)
        self.cell(width, 7, f"Limit: {limit} {currency}")

    def spentTotal(self, MoneySpent,currency):
        self.ln(10)
        width = self.get_string_width("Dashboard") + 40
        self.set_x((210 - width) / 2)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(width, 7, "Spending", border= 1, align= "C", fill=True)
        #limit
        self.ln(10)
        width = self.get_string_width("Dashboard") + 6
        self.set_x((210 - width) / 2)
        self.set_font("arial", "B", 10)
        self.set_text_color(0, 0, 0)
        self.cell(width, 7, f"Spending: {MoneySpent} {currency}")

    def leftTotal(self, MoneySpent,currency):
        self.ln(10)
        width = self.get_string_width("Dashboard") + 40
        self.set_x((210 - width) / 2)
        self.set_font("helvetica", "B", 13)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)
        self.cell(width, 7, "Left", border= 1, align= "C", fill=True)
        #limit
        self.ln(10)
        width = self.get_string_width("Dashboard") + 6
        self.set_x((210 - width) / 2)
        self.set_font("arial", "B", 10)
        self.set_text_color(0, 0, 0)
        self.cell(width, 7, f"Balance: {MoneySpent} {currency}")




def main():
    currency = checkCurrency()
    week = checkweek()
    if week == "reset": #resets all data from csv, when week4 is over
        deleteData()
        sys.exit(pyfiglet.figlet_format("Reset done", font = "small"))

    if week == "Week 1":
        askLimit("How much is your montly limit ? ")
        #print week
    print(pyfiglet.figlet_format(week, font = "starwars"))

    askFix()
    askCat()
    pdfSetup(week, currency)




def checkCurrency():
    while True:

        if len(sys.argv) == 2 and sys.argv[1] in currency_dict:
        # Get the first argument
            arg = sys.argv[1]

        # Check if the argument matches a currency symbol
            if arg in currency_dict:
                # Print the corresponding abbreviation
                return(currency_dict[arg])
            else:
                print("Currency symbol not found.")
        else:
            sys.exit("Missing currency")




def pdfSetup(week, currency):
    totalFixed, limit, MoneyLeft, MoneySpent, weeklyLimit, week1Data, week2Data, week3Data, week4Data = calculate(week)
    pdf = PDF(dctFixedKey, dctFixedValue, currency, totalFixed, limit, MoneyLeft, MoneySpent, weeklyLimit, week1Data, week2Data, week3Data, week4Data)
    pdf.add_page()
    pdf.fix(totalFixed, currency)
    pdf.week1(week1Data, currency)
    pdf.week2(week2Data, currency)
    pdf.week3(week3Data, currency)
    pdf.week4(week4Data, currency)
    pdf.weeklyLimit(weeklyLimit, currency)
    pdf.Setlimit(limit, currency)
    pdf.spentTotal(MoneySpent, currency)
    pdf.leftTotal(MoneyLeft, currency)
    pdf.output("Expenses_Sheet.pdf")

    if week == "Week 4":
        pdf.output("Expenses_Sheet_Saved.pdf")


def deleteData():
    with open("data.csv", 'w', newline='') as file:
        pass
    with open("limit.csv", 'w', newline='') as file:
        pass
    with open("fixed.csv", 'w', newline='') as file:
        pass



def checkweek():
     ls= []

     with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader: #append every row into ls
            ls.append(row)
        if len(ls) == 0: #if there is no word return week1
            return("Week 1")
        elif len(ls) == 5:
            return("Week 2") #if there are 5 words return week2
        elif len(ls) == 10:
            return("Week 3")
        elif len(ls) == 15:
            return("Week 4")
        elif len(ls) == 20:
            return("reset")



def askLimit(prompt):
    while True:
        try:
            limit = float(input(prompt))
            #append limit to limit.csv
            with open("limit.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames =["limit"])
                writer.writerow({"limit": limit})
                break
        except ValueError:
            pass



#ask for key(catergory) and value (cost)
def askFix():

    while True:
        askfix = input("Add any fix costs ? YES/NO ").upper()
        if askfix == "YES":
            result = pyfiglet.figlet_format("FIX COST", font = "starwars" ) #ascii
            print(result)
            with open("fixed.csv", "a") as file: #open csv
                writer = csv.DictWriter(file, fieldnames=["category", "expenses"] )
                while True: #input key, value until "END"
                    try:
                        catFix = input("Category: ")
                        costFix = float(input("Expenses: "))
                        askEnd = input("Write END if finished: ").upper()

                        writer.writerow({
                        "category": catFix,
                        "expenses": costFix,
                        })

                        if askEnd == "END": #if END return to main
                            return

                    except ValueError:
                        print("Wrong input!")
                        pass

        elif askfix == "NO":
            return

        else:
            print("Invalid input! Please enter YES or NO")


def askCat():
    result = pyfiglet.figlet_format("Categories", font = "small" ) #ascii
    print(result)
    while True:
        try:
            #open csv and set writer
            with open("data.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["category", "expenses"])
                #all inputs
                food = float(input("Food/Groceries: "))
                trans = float(input("Transportation: "))
                pcare = float(input("Personal Care: "))
                recreation = float(input("Recreation: "))
                misc = float(input("Misc: "))
                #appending to data.csv
                writer.writerow({"category": "food", "expenses": food})
                writer.writerow({"category": "trans", "expenses": trans})
                writer.writerow({"category": "pcare", "expenses": pcare})
                writer.writerow({"category": "recreation", "expenses": recreation})
                writer.writerow({"category": "misc", "expenses": misc})
                break
        except ValueError:
            print("Wrong Input")
            pass


def calculate(week):

    #open files

    with open("limit.csv", "r") as file1:
        reader1 = csv.DictReader(file1)
        for line in file1:
            lsLimit.append(line)
    with open("data.csv", "r") as file3:
        reader3 = csv.DictReader(file3)
        for line in file3:
            lsData.append(line)
    with open("fixed.csv", "r") as file2:
        reader2 = csv.DictReader(file2)
        for line in file2:
            lsFixed.append(line)

    #unpack lsLimit
    limit = float(lsLimit[0].replace('\n', ''))

    #check week to set range p
    if week == "Week 1":
        p = 5
    elif week == "Week 2":
        p = 10
    elif week == "Week 3":
        p = 15
    else:
        p = 20

    #unpack lsData
    for n in range(p):
        nopurpose, valueData = lsData[n].replace('\n', '').split(",")
        dctData[f"dataValue{n+1}"] = float(valueData)
    #unpack fixData
    for index, line in enumerate(lsFixed):
        dontcare1, valueFixed = line.replace('\n', '').split(",")
        dctFixedValue[f"FixedValue{index+1}"] = float(valueFixed)
    for index, line in enumerate(lsFixed):
        key, dontcare = line.replace('\n', '').split(",")
        dctFixedKey[f"FixedKey{index+1}"] = key



    #calulation!!!!

    #sum all ints from dctfix
    totalFixed = 0
    for value in dctFixedValue.values():  #iterates directly trough values in dict
        totalFixed += value

    #sum all ints from dctvalues
    totalData = 0
    for value in dctData.values():  #iterates directly trough values in dict
        totalData += value

    #sum ints week1
    week1Data = 0
    for index, valuew1 in enumerate(dctData.values()):
        if index < 5:
            week1Data += valuew1



    #sum ints week2
    week2Data = 0
    for index, valuew2 in enumerate(dctData.values()):
        if 5  <= index <= 10:
            week2Data += valuew2



    #sum ints week3
    week3Data = 0
    for index, valuew3 in enumerate(dctData.values()):
        if 10  <= index <= 15:
            week3Data += valuew3



    #sum ints week4
    week4Data = 0
    for index, valuew4 in enumerate(dctData.values()):
        if 15  <= index <= 20:
            week4Data += valuew4



    #how much money is left from limit = limit - all rows from  fixed/data
    MoneyLeft = limit - totalData - totalFixed


    #weekly limit
    if week == "Week 1":
        weeklyLimit = (limit - week1Data)/ 3

    if week == "Week 2":
        weeklyLimit = (limit - week1Data - week2Data)/ 2
    if week == "Week 3":
        weeklyLimit = MoneyLeft
    if week == "Week 4":
        weeklyLimit = MoneyLeft
    MoneySpent = totalData + totalFixed


    weeklyLimit = "{:.1f}".format(weeklyLimit)
    limit = "{:.1f}".format(limit)
    totalFixed = "{:.1f}".format(totalFixed)
    MoneyLeft = "{:.1f}".format(MoneyLeft)
    MoneySpent = "{:.1f}".format(MoneySpent)
    week1Data ="{:.1f}".format(week1Data)
    week2Data ="{:.1f}".format(week2Data)
    week3Data ="{:.1f}".format(week3Data)
    week4Data ="{:.1f}".format(week4Data)


    #how much spent in month = all rows from fixed # all rows from data



    return totalFixed, limit, MoneyLeft, MoneySpent,weeklyLimit, week1Data, week2Data, week3Data, week4Data



if __name__ == "__main__":
    main()

