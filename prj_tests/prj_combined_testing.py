from prj_backend_testing import backend_testing
from prj_frontend_testing import frontend_testing

m_id = "17"
m_user = "yana"


def combined_testing(user_id, username):
    backend_testing(user_id, username)
    user_name = frontend_testing(user_id)
    assert username == user_name


if __name__ == '__main__':
    combined_testing(m_id, m_user)

