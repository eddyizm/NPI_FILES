from datetime import datetime, timedelta

class GetURL():
    def __init__(self):
        self.month = None
        self.second_monday = None

    def get_monthly_url(self):

        year = datetime.now().year
        month = datetime.now().month

        # Start with the first day of the month
        first_day_of_month = datetime(year, month, 1)
        # Find the first Monday
        first_monday = first_day_of_month + timedelta(days=(7 - first_day_of_month.weekday()))
        # Calculate the second Monday
        self.second_monday = first_monday + timedelta(days=7)

        # Format the date as MMDDYY)
        formatted_date = self.second_monday.strftime('%m%d%y')

        # Construct the URL with the formatted date
        url = f'https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_{formatted_date}.zip'

        return url