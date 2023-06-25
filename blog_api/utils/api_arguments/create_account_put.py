from flask_restful import reqparse


create_account_put_args = reqparse.RequestParser()
create_account_put_args.add_argument("user", type=str, help="A username is required.", required=True)
create_account_put_args.add_argument("password", type=str, help="A password is required.", required=True)
create_account_put_args.add_argument("email", type=str, help="An email is required.", required=True)
