from argparse import ArgumentParser
from data_manager import get_length_file, append_user_data
from data_class import UserManager

parser = ArgumentParser(prog="send_email")
parser.add_argument("type", type = str, choices=["view", "message"])
parser.add_argument('-id', '--user_id', type = int)
parser.add_argument('-e', '--user_email', type = str)

args = parser.parse_args()
# print(args)
# print(args.user_id)
# print(args.user_email)
# print(get_length_file())
# append_user_data(user_name = "KienMN", user_email = "Kienmn97@gmail.com", amount = 189, date = None)
if args.type == "view":
	print(UserManager().get_user_data(args.user_id))
elif args.type == "message":
	print(UserManager().send_email(args.user_id))
