import argparse

parser = argparse.ArgumentParser('Sum of two ints + displaying the user')
parser.add_argument('--user','-u',nargs='?',default='guest',choices=['salah','moncef','root','guest'])
parser.add_argument('--first','-f',type=int, default=0)
parser.add_argument('--second', '-s', type=int, default=0)

args = parser.parse_args()

print('hey mr ' + args.user + ' the sum of the provided numbers is : '+f'{(args.first+args.second)}')