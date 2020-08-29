def initHeader():
    header = """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <title>Chat app</title>
            <link rel="stylesheet" href="style.css">
        </head>

        <!--This is for refreshing the page everytime I make a change-->
        <script type="text/javascript" src="http://livejs.com/live.js"></script>

        <!--Fonts-->
        <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap" rel="stylesheet">

        <body>
            <div class="conversation-container">
    """
    return header

def closeHTML():
    closer = """
            </div>
        </body>
        </html>
    """
    return closer

def writeMsg(posMsg, msg, sentDate):
    if posMsg == 'left':
        msgBubble = """
            <div class="message-container msg-container-left">
                <div class="msg-left">
                    <p class="msg-text">
                        """+msg+"""
                    </p>
                </div>
                <div class="sent-date">
                    """+sentDate+"""
                </div>
            </div>
        """
    if posMsg == 'right':
        msgBubble = """
        <div class="message-container msg-container-right">
            <div class="sent-date">
                """+sentDate+"""
            </div>
         
            <div class="msg-right">
                <p class="msg-text">
                    """+msg+"""
                </p>
            </div>
        </div>
        """
    return msgBubble

def dateSeperator(date):
    dateSepHTML = """
        <div class="date-seperator">
            *-------------------- """+date+""" --------------------*
        </div>
    """
    return dateSepHTML
