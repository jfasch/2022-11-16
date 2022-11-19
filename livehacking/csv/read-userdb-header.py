import sys
import userdb_csv
import output_user

users = userdb_csv.read_csv_header(sys.argv[1])
output_user.print_users(users)
