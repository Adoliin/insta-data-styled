def initHeader(currentUser, targetUser):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{targetUser}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <div class="conversation-container">
    <div class="users">
      <div class="user ">
        <div class="user-left">
          <p>
            {currentUser}
          </p>
        </div>
      </div>
      <div class="user">
        <div class="user-right">
          <p>
            {targetUser}
          </p>
        </div>
      </div>
    </div>
"""

def closeHTML():
    return """
    </div>
</body>
</html>
"""

def writeMsg(posMsg, msg, sentDate):
    if posMsg == 'left':
        msgBubble = f"""
    <div class="message-container msg-container-left">
      <div class="msg msg-left">
        <p>
          {msg}
        </p>
      </div>
      <div class="sent-date">
        <p>
          {sentDate}
        </p>
      </div>
    </div>
"""
    if posMsg == 'right':
        msgBubble = f"""
    <div class="message-container msg-container-right">
      <div class="msg msg-right">
        <p>
          {msg}
        </p>
      </div>
      <div class="sent-date">
        <p>
          {sentDate}
        </p>
      </div>
    </div>
"""
    return msgBubble

def dateSeperator(date):
    return f"""
    <div class="date-separator">
      {date}
    </div>
"""

styleCss = r"""
* {
  margin: 0;
  padding:0;
  box-sizing: border-box;
}

body {
  display: flex;
  justify-content: center;
  background-color: #EEEEEE;
}

.date-separator {
  font-size: 1.5rem;
  width: 100%;
  text-align: center;
  background-color: #F7DBD7;
  color: black;
  font-style: bold;
}

.users {
  width: 100%;
  display: flex;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  font-style: bold;
}

.user {
  width: 50%;
  justify-content: center;
  display: flex;
  font-size: 2rem;
}

.user-left {
  border-radius: 10px 100px / 120px;
  background-color: #9CE79E;
  padding: 0.5rem;
}
.user-right{
  border-radius: 10px 100px / 120px;
  background-color: #9CC0E7;
  padding: 0.5rem;
}

.conversation-container {
  display: flex;
  flex-direction: column;
  width: 80%;
  align-items: center;
}
.message-container {
  display: flex;
  width: 100%;
  align-items: center;
  flex-direction: column;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

.msg-container-right {
  flex-direction: row-reverse;
}
.msg-container-left {
  flex-direction: row;
}

.sent-date {
  margin-right: 0.5rem;
  margin-left: 0.5rem;
  border-radius: 25% 10%;
  font-style: italic;
  background-color: #DCDCDC;
  color: black;
  font-size: 1.1rem;
  padding: 0.4rem;
}

.msg{
  width: 50%;
  padding: 1rem;
  font-size: 2rem;
  border-radius: 30px;
}

.msg-left {
  background-color: #9CE79E;
  color: black;
}

.msg-right {
  background-color: #9CC0E7;
  color: black;
}
"""
