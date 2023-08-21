import psycopg2
import csv

# File path and name.
filePath = 'd:\\neostudy\\'
fileName = 'credit_debit_info.csv'

def export_credit_debit_info_to_csv():
    # Connection parameters, change according to your settings
    connect = psycopg2.connect(
        dbname="neostudy",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

    # New cursor object
    cursor = connect.cursor()

    try:
        # Call the PostgreSQL function and fetch the result
        cursor.callproc('get_credit_debit_info', ['2018-01-09'])
        result = cursor.fetchall()


        headers = [i[0] for i in cursor.description]

        # Write the result to the CSV file
        csvFile = csv.writer(open(filePath + fileName, 'w', newline=''),
                             delimiter=',', lineterminator='\r\n')  # quoting=csv.QUOTE_ALL, escapechar='\\'

        # Add the headers and data to the CSV file.
        csvFile.writerow(headers)
        csvFile.writerows(result)


        print(f"Data exported to {fileName} successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error exporting data: {str(error)}")

    # Close the cursor and the connection
    cursor.close()
    connect.close()

if __name__ == '__main__':
    export_credit_debit_info_to_csv()