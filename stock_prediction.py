import yfinance as yf
from datetime import date, timedelta
import valid_tickers


def main():
    """Main function that takes user input of a valid ticker followed by a valid date."""
    # Get user input: one stock ticker and a time horizon of a min of one day and max of six months.
    ticker = input("Please enter a stock symbol or ticker: ").upper()

    # Checks that ticker is valid.
    while ticker not in valid_tickers.all_ticker_symbols or ticker in valid_tickers.missing_recent_data:
        ticker = input("Please reenter a valid stock symbol or ticker: ").upper()

    future_date = input("Please enter a number of days from 1-7 days from the present "
                        "to predict the price on that future date: ")

    # Checks that date is valid.
    result = date_check(future_date)
    while not result:
        future_date = input("Please reenter a number of days from 1-7 days from the present "
                            "to predict the price on that future date: ")
        result = date_check(future_date)

    import ml
    return ml.delphi(ticker, future_date)


def date_check(user_days):
    """Verifies that the date inputted by user is in the correct format, and is greater than
    the present date and less than one week in the future.
    """
    today = date.today()
    one_week = today + timedelta(days=7)
    future_date = today + timedelta(days=int(user_days))

    past_date = today > future_date
    past_max = future_date > one_week

    if past_date or past_max or user_days == "0":
        return False
    else:
        return True


def get_ticker_history(ticker):
    """Use yfinance to get historical data for a ticker. The ticker must be given as a string."""
    ticker_obj = yf.Ticker(ticker)
    ticker_hist = ticker_obj.history(period="ytd")
    return ticker_hist


if __name__ == "__main__":
    main()
