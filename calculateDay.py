import pandas as pd

class calculateday:
        def daynumber(number):
            df_day = pd.read_csv("datacsv/number_day.csv")
            df_month = pd.read_csv("datacsv/number_month.csv")
            number_day, number_month = number.split("/")
            if int(number_day) <= 30 and (int(number_month) in (4, 6, 9, 11)):
                mean_day = str(int(number_day)) + " : " + df_day["Mean"][int(number_day) - 1]
                mean_month = str(int(number_month)) + " : " + df_month["Mean"][int(number_month) - 1]
            elif int(number_day) <= 31 and (int(number_month) in (1, 3, 5, 7, 8, 10, 12)):
                mean_day = str(int(number_day)) + " : " + df_day["Mean"][int(number_day) - 1]
                mean_month = str(int(number_month)) + " : " + df_month["Mean"][int(number_month) - 1]
            elif int(number_day) <= 29 and int(number_month)  == 2:
                mean_day = str(int(number_day)) + " : " + df_day["Mean"][int(number_day) - 1]
                mean_month = str(int(number_month)) + " : " + df_month["Mean"][int(number_month) - 1]
            return mean_day, mean_month