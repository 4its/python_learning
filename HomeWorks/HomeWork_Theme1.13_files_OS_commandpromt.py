import argparse

def deffile(file):
    try:
        of = open(file, 'r')
        of.close()  # close file
    except FileNotFoundError:
        print("Looks like file doesn't exist. I'll create it for you.")
        of = open(file, 'w')  # usr right 'w' to create file
        of.close()  # close file
        print("File successfully created.\n")

def writeto(file, args):  # func to generate article.txt if it doesn't exist with random numbers
    fo = open(file, 'a')  # usr right 'w' to create file
    sample = str("{}\t{}\t{}\t{}\n".format(args.city,args.address,args.phone,args.fio))
    print("\nSrting below was succesfuly added to file '{}':\n{}".format(file,sample))
    fo.write(sample)  # write our string to file
    fo.close()  # close file

def printfile(file):
    fo = open(file, 'r')
    sample = fo.readlines()
    for i in range(len(sample)):
        print(sample[i])
    fo.close()


parser = argparse.ArgumentParser(
prog='Workers Script Script',
usage='%(prog)s [options]',
description='Program for forming info about workers', epilog='(c) Coded by George Egiazaryan')
c_help = 'Allow to add city of worker. Example: Moscow, St. Petersburg ...'
a_help = "Allow to add  city of worker. Must be covered in ''(quotes). Example: '119, 1-st street, 12-45'"
p_help = "Allow of add workers phone number. Numbers only. Example: 1234567890"
f_help = "Allow to add wrkers Name and Surname. Must be covered in ''(quotes). Example: 'Robert Downey Jr.'"

parser.add_argument ('-c', '--city',    type=str, nargs='?',  default='no City',   help=c_help, )
parser.add_argument ('-a', '--address', type=str, nargs='?',  default='no Address',help=a_help)
parser.add_argument ('-p', '--phone',   type=int, nargs='?',  required= True,      help=p_help)
parser.add_argument ('-f', '--fio',     type=str, nargs='?',  required= True,      help=f_help)
args = parser.parse_args()

file = 'Staff.txt'
deffile(file)
writeto(file, args)
printfile(file)
