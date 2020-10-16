from skpy import Skype
from skpy import SkypeAuthException

username = ""
password = ""
token_file_name = "token_file.txt"
send_to_user = ""
send_message = "test msg; ignore"


def connect_skype(user, pwd, token):
    s = Skype(connect=False)
    s.conn.setTokenFile(token)
    try:
        s.conn.readToken()
    except SkypeAuthException:
        s.conn.setUserPwd(user, pwd)
        s.conn.getSkypeToken()
        s.conn.writeToken()
    finally:
        sk = Skype(user, pwd, tokenFile=token)
    return sk

sk = connect_skype(username, password, token_file_name) # connect to Skype

# print(sk.user) # you

for cont in sk.contacts:
    if send_to_user in cont.id:
        cont.chat.sendMsg(send_message)
        break;
