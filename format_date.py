from datetime import datetime

def format_date(date):
    date_object = datetime.strptime(date, '%m/%d/%Y')
    # print(date_object.strftime('%Y%d%m'))
    return date_object.strftime('%Y%d%m')
    # return x
	
	

def main():
    print("hello world")
    print("date time format")

    print(format_date("11/12/2019"))
    # format_date('9/15/18')



# format_date("11/12/2019") ➞ "20191211"

# format_date("12/31/2019") ➞ "20193112"

# format_date("01/15/2019") ➞ "20191501"


if __name__ == "__main__":
    main()