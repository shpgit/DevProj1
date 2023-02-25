import requests
from prj_db_connector import validate_user

ins_id = "10"
ins_user = "felix"


def backend_testing(user_id, user_name):
    web_rq = f"http://127.0.0.1:5000/users/{user_id}"

    try:
        post_rq = requests.post(web_rq, json={"user_name": user_name})
        if post_rq.ok:
            print("check post request: \n", "post request was send successfully")
        else:
            print("error: somthing went wrong! \n", post_rq.json()['reason'])

    except requests.exceptions.ConnectionError as reqExecConErr:
        print(reqExecConErr, "\n\ncheck if rest_app.py is running?")

    get_req = requests.get(web_rq)
    get_res_user_name = get_req.json()['user name']

    if get_res_user_name == user_name and (get_req.status_code == 200):
        print("\n\ncheck if user_name and user_id are matching: \n", "No Error, all match")
    else:
        print("\n\ncheck if user_name and user_id are matching: \n", "Error:", get_res_user_name, "is not:", user_name)

    # checking user info from DB

    try:
        validate_user_info = validate_user(user_id, user_name)

        if validate_user_info != "somthing went wrong":
            print("\ndb query: \n", "username '", user_name, "'is stored with index number", user_id, "in the db")

    except UnboundLocalError as Err:
        print("\ndb query: \n", "There is no match in the db.")


if __name__ == '__main__':
    backend_testing(ins_id, ins_user)




