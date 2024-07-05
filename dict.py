from csv import DictWriter, DictReader
from os.path import exists


def get_data():
    while True:
        first_name = input('Enter name: ')
        last_name = input('Last name: ')
        phone_number = input('Phone number: ')
        if len(first_name) < 2 or ' ' in first_name:
            print('Error: name is too short or contain spaces.')
            continue
        elif len(last_name) < 2 or ' ' in last_name:
            print('Error: last name is too short or contain spaces.')
            continue
        elif not 11 <= len(phone_number) <= 18 or ' ' in phone_number:
            print('Error: invalid phone number syntax')
            continue
        else:
            print('New user was successfully added!')
            break
    return [first_name, last_name, phone_number]


def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['First_Name', 'Last_Name', 'Phone_Number'])
        f_w.writeheader()


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(filename, lst):
    res = read_file(filename)
    obj = {'First_Name': lst[0], 'Last_Name': lst[1], 'Phone_Number': lst[2]}
    res.append(obj)
    standard_write(filename, res)


def row_search(filename):
    last_name = input("Enter last name: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Last_Name']:
            return row
    return "Error: referred tracing not found."


def delete_row(filename):
    row_number = int(input("Type line number:  "))
    res = read_file(filename)
    print(f'{res.pop(row_number-1)} line was just deleted.')
    standard_write(filename, res)


def standard_write(filename, res):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['First_Name', 'Last_Name', 'Phone_Number'])
        f_w.writeheader()
        f_w.writerows(res)


def change_row(filename):
    row_number = int(input("Type line number: "))
    res = read_file(filename)
    data = get_data()
    previous_row = res[row_number-1]
    res[row_number-1]["First_Name"] = data[0]
    res[row_number-1]["Last_Name"] = data[1]
    res[row_number-1]["Phone_Number"] = data[2]
    print(f'{row_number} line was successfully changed!')
    standard_write(filename, res)


def copy_row(x_filename, y_filename):
    row_number = int(input('Type line number: '))
    res1 = read_file(x_filename)
    res2 = read_file(y_filename)
    res2.append(res1[row_number-1])
    print(f'{res1[row_number-1]} line was successfully copied from {x_filename} to {y_filename}!')
    standard_write(y_filename, res2)


def main():
    name = input('Enter file name you want to work with (name only): ')
    name += '.csv'
    while True:
        command = input("Command: ")
        if command == "quit":
            break
        elif command == "write":
            if not exists(name):
                print(f'Creating {name} file...')
                create_file(name)
            write_file(name, get_data())
        elif not exists(name):
            print('Error: File is not exist. Create it by typing "write" command.')
        elif command == "read":
            print(read_file(name))
        elif command == "find":
            print(row_search(name))
        elif command == "rmw":
            delete_row(name)
        elif command == "change":
            change_row(name)
        elif command == "copy":
            name2 = input('Enter file name, where u want to copy previous file data (name only): ') + '.csv'
            if not exists(name2):
                print(f'Creating {name2} file...')
                create_file(name2)
            copy_row(name, name2)


main()
