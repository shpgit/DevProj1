import requests
from prj_db_connector import validate_user


def backend_testing(user_id, user_name):
    web_rq = f"http://127.0.0.1:5000/users/{user_id}"

    try:
        post_rq = requests.post(web_rq, json={"user_name": user_name})
        if post_rq.ok:
            print(post_rq.json())
        else:
            post_rq_err = post_rq.json()
            print("error: somthing went wrong!", post_rq_err['reason'],
                  "status code:", post_rq.status_code)

    except requests.exceptions.ConnectionError as reqExecConErr:
        print(reqExecConErr, "\n\ncheck if rest_app.py is running?")

    get_req = requests.get(web_rq)
    get_res_user_name = get_req.json()[user_name]

    if get_res_user_name == user_name and (get_req.status_code == 200):
        print("No Error", get_res_user_name, "equal to:", user_name,
              "\nstatus code is: ", get_req.status_code)
    else:
        print("Error:", get_res_user_name, "is not:", user_name)

    # checking user info from DB

    try:
        validate_user_info = validate_user(user_id, user_name)

        if validate_user_info != "somthing went wrong":
            print("\ndb query: \n", user_name, " is stored in the db correctly")

    except UnboundLocalError as Err:
        print("\nThere is no match in the db.")


if __name__ == '__main__':
    backend_testing(17, "tal")




