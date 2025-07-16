import yfinance as yf
import matplotlib.pyplot as plt

def fetch_and_plot(ticker):
    data = yf.download(ticker, period="30d")
    data['Close'].plot(title=f'{ticker} Closing Prices - Last 30 Days')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    fetch_and_plot("TCS.NS")
