
import csv

CARS_CSV_FILE = "cars.csv"
BIRTH_MONTHS_CSV_FILE = "birth_months.csv"

def read_csv_cars():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.reader(f, delimiter = ",")

        for line in csv_reader:
            #print(line)
            print(line[1], line[4])


def read_csv_dict_cars():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.DictReader(f, delimiter = ",")

        #print("headers:", csv_reader.fieldnames)

        for row in csv_reader:
            #print(row)
            print(row["Make"], row["Year"], row["Price"])

'как сделать запись новых данных в файл .csv'

class FieldNames:
    NAME = "name"
    MONTH = "month"
    DEPARTMENT = "department"

def write_csv_dict():
    fieldnames = [FieldNames.NAME, FieldNames.MONTH, FieldNames.DEPARTMENT]
    with open(BIRTH_MONTHS_CSV_FILE, "w", newline ='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        row = {
            FieldNames.NAME: "John",
            FieldNames.MONTH: "May",
            FieldNames.DEPARTMENT: "IT",
        }
        csv_writer.writerow(row)

        row2 = {
            FieldNames.NAME: "Mary",
            FieldNames.DEPARTMENT: "HR",
            FieldNames.MONTH: "March",
        }
        row3 = {
            FieldNames.NAME: "Ann",
            FieldNames.MONTH: "September",
            FieldNames.DEPARTMENT: "Analytics",
        }
        rows = [row2, row3]
        csv_writer.writerows(rows)

def main():
    #read_csv_cars()
    #read_csv_dict_cars()
    write_csv_dict()

if __name__ == '__main__':
    main()

