import argparse
import os
import tempfile
import json

def put(key, val):
    with open(storage_path, 'w') as f:
        json.dump({key:val}, f)

def get_val(key):
    with open(storage_path, 'r') as f:
        j = f.read()
        j = json.loads(j) if j else ''
        return j.get(key, None)

parser = argparse.ArgumentParser(description='Dsc')
parser.add_argument('--key')
parser.add_argument('--val')

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.key and args.val:
    put(args.key,args.val)
elif args.key:
    print(get_val(args.key))
else:
    print("No parametrs")