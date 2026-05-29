#Create a stock dictionary
stock_dic = {
    'MSFT' : 200,
    'AMZN' : 300,
    'GOOGL': 400,
    'META' : 500,
    'NVDA' : 600,
    'TSLA' : 700
}

def stock_tracker():
    #Get data from user
    stock_name = input("Please enter the stock name: ").upper()
    stock_quantity = input("Please enter the invested stock quantity: ")
    #Converts quantity into integer
    stock_quantity = int(stock_quantity)

    #Checks if stock exists
    if stock_name in stock_dic:
        stock_price = stock_dic[stock_name]

        #Calculate the total investment.
        total_investment = stock_price * stock_quantity 
        print("Your total investment value: ", total_investment)


        #Save the data in txt. file (File Handling)
        file = open("portfolio.txt", "a")
        file.write(f"Stock Name: {stock_name}\n")
        file.write(f"Quantity: {stock_quantity}\n")
        file.write(f"Stock Price: {stock_price}\n")
        file.write(f"Total Investment: {total_investment}\n")
        file.write("-----------------------------\n")
        file.close()
        print("Investment details saved in portfolio.txt")

    else:
        print("Your stock name", stock_name, "is not in record")

#Calling Function
stock_tracker()


