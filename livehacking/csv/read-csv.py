import sys
import userdb_csv
import output_user

format = sys.argv[1]
filename = sys.argv[2]

if format == 'header':
    readfunc = userdb_csv.read_csv_header
elif format == 'noheader':
    readfunc = userdb_csv.read_csv_noheader
else:
    print('bad format', file=sys.stderr)
    sys.exit(1)

output_user.print_users(readfunc(filename))
