  # YOUR PROJECT TITLE
    #### Video Demo:  <https://youtu.be/XCmYM1kAuxc>
    #### Description:
    Tracking Expenses every week and displaying them in a Dashboard with all the necessary datas.
    First we have to enter out currency in the sys.argv[1], so the currency can bet set on our PDF file. Unfortunatly
    the fpdf library doesnt support any symbols which made me change the currency dict into names(example EUR).
    Also for every wrong input, we get another prompt to input the right information. And for more readibly structure, I used pyfiglet.
    My information input starts by asking my monthly limit. Then it asks about my fix costs. Here, I can input as many datas I want.
    If I want to end my input, I have to write "end".
    Then we come to the catergories. We have to input the amount for given categories such as food, transportation, personal care, recreation and misc.
    Thats it with the input.

    All the data is stored in a extra database. To be more precise in data.csv, fixed.csv and limit.csv file. From here we can extract all the information for
    the calculation.
    First we have our total expenses for our fixed spening, then for each week and then the total amount. We also have the weekly limit. This number depends on how much
    we over/underspend our weekly limit.

    So after we calculated all the data, we can now use the FPDF library. Here we can now display it on the PDF file and make the magic visible.
    And after the week 4 is done, we can now start the program again, so all the data in the databases get reseted. But before that, It created another file to save
    all the datas there. Now we can start the program as usual.

    And the next question is, how can I track on which week I am. So because I have saved datas on the data.csv file, I can check how many information are already put in.
    So if we have 5 rows, that means the week 2 can begin.
























    TODO



# automaticaly checks if week 1,2,3 or 4 is empty
# if week 5, reset!
# if week 1 is empty ask for "askFix", else nothing!
# if week 1 is full, dont ask for monthly limit


# ASK LIMIT FOR MONTH -> store in limit.csv
# ASK Fix expenses -> Housing, Phone -> STORE IN data.csv
# ASK Catergories to put expenses in -> Food/Groceries, Transportation, Personal Care, Recreation, MISC -> STORE IN fixed.csv
# CALCULATELIMIT -- >FIXED EXPENSES, HOW MUCH LEFT split into the next 3 weeks, Spent this week, Spent in total
#IDEAS -> convert foreign currency to home currency


#THE WHOLE TODO IS IN different parts of the CODE. SORRY
