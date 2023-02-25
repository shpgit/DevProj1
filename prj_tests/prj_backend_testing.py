import requests
from prj_db_connector import add_user, get_user


def backend_testing(user_id, user_name):
    web_get = f"http://127.0.0.1:5000/users/{user_id}"
    web_post = f"http://127.0.0.1:5000/users/{user_id}"
    try:
        post_rq = requests.post(
            web_post,
            json={"user_name": user_name()}
        )
        if post_rq.ok:
            print(post_rq.json())
        else:
            post_err = post_rq.json()
            print("error: somthing went wrong!", post_err['reason'],
                  "status code:", post_rq.status_code)

    except requests.exceptions.ConnectionError as reqExecConErr:
        print(reqExecConErr, "\n\ncheck if rest_app.py is running?")

    get_request = requests.get(web_get)
    get_response_user_name = get_request.json()['user_name']

    if get_response_user_name == user_name and (get_request.status_code == 200 or get_request.status_code == 201):
        print("No Error", get_response_user_name, "equal to:", user_name,
              "\nstatus code is: ", get_request.status_code)
    else:
        print("Error:", get_response_user_name, "is not equal to:", user_name)



