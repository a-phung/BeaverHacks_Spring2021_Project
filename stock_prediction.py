import yfinance as yf
from datetime import date, datetime, timedelta
import valid_tickers
import mla


def main():
    """Main function that takes user input of a valid ticker followed by a valid date."""
    # Get user input: one stock ticker and a time horizon of a min of one day and max of six months.
    ticker = input("Please enter a stock symbol or ticker: ").upper()

    # Checks that ticker is valid.
    while ticker not in valid_tickers.all_ticker_symbols or ticker in valid_tickers.missing_recent_data:
        ticker = input("Please reenter a valid stock symbol or ticker: ").upper()

    future_date = input("Please enter a future time up to six months from the present in the format "
                        "'YYYY-MM-DD' to predict the price on that date: ")

    # Checks that date is valid.
    result = date_check(future_date)
    while not result:
        future_date = input("Please reenter a valid future date up to one week from the present "
                            "in the format 'YYYY-MM-DD' to predict the price on that date: ")
        result = date_check(future_date)
    return mla.delphi(ticker)


def date_check(user_date):
    """Verifies that the date inputted by user is in the correct format, and is greater than
    the present date and less than six months in the future.
    """
    try:
        today = date.today()
        one_week = today + timedelta(days=14)
        if len(str(today)) != len(user_date):
            return False
        if user_date[4] != "-" or user_date[7] != "-":
            return False

        future_year = int(user_date[:4])
        future_month = int(user_date[5:7])
        future_day = int(user_date[8:])

        past_date = today > datetime(future_year, future_month, future_day).date()
        past_max = one_week < datetime(future_year, future_month, future_day).date()

        if past_date or past_max:
            return False
        else:
            return True

    except ValueError:
        return False


def get_ticker_history(ticker):
    """Use yfinance to get historical data for a ticker. The ticker must be given as a string."""
    ticker_obj = yf.Ticker(ticker)
    ticker_hist = ticker_obj.history(period="ytd")
    return ticker_hist


if __name__ == "__main__":
    main()
