import yfinance as yf  # Import yfinance library for fetching stock data
import pandas as pd

# Define the portfolio dictionary to store stock ticker symbols and share counts
portfolio = {}

def add_stock(ticker , shares):
    portfolio[ticker] = portfolio.get(ticker , 0) + shares
    print(f"Add {shares} shares to {ticker} to the portfolio.")


def remove_stock(ticker):

    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Remove {ticker} from the portfolio.")

    else:
        print(f"{ticker} is not present in the portfolio.")


def display_portfolio():
    data = {"Ticker": [] , "Shares": [] , "Current price": [] , "Values": []}

    for ticker , shares in portfolio.items():
        stock = yf.Ticker(ticker)
        price = stock.history(period = "1d")["Close"].iloc[0]
        data["Ticker"].append(ticker)
        data["Shares"].append(shares)
        data["Current price"].append(price)
        data["Values"].append(shares * price)


    df = pd.DataFrame(data)
    df["Total Portfolio Value"] = df["Values"].sum()
    print(df)


add_stock("AAPL" , 10)
add_stock("MSFT" , 6)
add_stock("AMZN" , 20)
add_stock("TSLA" , 14)
display_portfolio()
remove_stock("MSFT")
display_portfolio()





