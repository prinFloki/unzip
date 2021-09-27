import argparse
parser = argparse.ArgumentParser(description="sample argument parser")
#By default all arguments are of type String, nargs=? to prevent the script from demanding the arg
parser.add_argument('--first', '-f', default=0, nargs='?', type=int)
parser.add_argument('--second','-s', default=0, nargs='?', type=int)
#in th arg isn't one of the choices we get an error (case sensitive)
parser.add_argument('--user', '-u', default='Guest', nargs='?', choices=['Admin', 'admin', 'root', 'guest', 'Guest'])
#we pick the args
args=parser.parse_args()
print('Hello ' + args.user)
print('Addition of the two provided numbers is : '+f'{(args.first+args.second)}')