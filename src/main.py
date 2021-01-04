import json
import os
import toHTML

def main():
    global cnvDir, textDir, webDir
    cnvDir, textDir, webDir = initDirs()
    jsonData = getJsonData()
    currentUser = getUsername(jsonData)
    getAllConversations(jsonData, currentUser)
    getMsgCount(jsonData, currentUser)

def getAllConversations(jsonData, currentUser):
    cnvsCount = len(jsonData)
    for conversation in jsonData:
        ok, tmp = getTargetUsername(conversation['participants'], currentUser)
        if ok:
            targetUser = tmp
            conversationsList = getConversationList(jsonData, targetUser, cnvsCount)
            getConversation(currentUser, targetUser, conversationsList)
            print(f'SUCCESS: Created conversation with {targetUser}.')
        else:
            multiplePartipants = tmp
            print(f'FAIL   : Can\'t create conversation with "{multiplePartipants}", because it does not contain 2 participants!')

def getConversationList(jsonData, targetUser, cnvsCount):
    conversationsList = []
    for i in range(cnvsCount):
        if targetUser in jsonData[i]['participants']:
            conversationsList.append(jsonData[i]['conversation'])
    return conversationsList

def getJsonData():
    print('Type the path to the the "messages.json" file you got from instagram data:')
    while True:
        jsonFilePath = input('--> ')
        try:
            jsonData = readJson(jsonFilePath)
            _ = jsonData[0]['participants']
            _ = jsonData[1]['conversation']
        except:
            print('FAIL: the path you gave is not to a valid instagram messages.json!')
            continue
        else:
            return jsonData

def readJson(jsonFilePath):
    jsonPath = os.path.join(jsonFilePath)
    with open(jsonPath, 'r') as dataFile:
        jsonData = dataFile.read()
    return json.loads(jsonData)

def initDirs():
    cnvDir = os.path.join(os.getcwd(), 'conversations')
    textDir = os.path.join(cnvDir, 'text-format')
    webDir = os.path.join(cnvDir, 'web-format')
    styleCssPath  = os.path.join(cnvDir, 'style.css')

    if not os.path.exists(cnvDir):
        os.mkdir(cnvDir)
    if not os.path.exists(textDir):
        os.mkdir(textDir)
    if not os.path.exists(webDir):
        os.mkdir(webDir)
    if not os.path.exists(styleCssPath):
        with open(styleCssPath, 'w') as styleFile:
            styleFile.write(toHTML.styleCss)
    return cnvDir, textDir, webDir

def getTargetUsername(participants, currentUser):
    if len(participants) == 2:
        if participants[0] != currentUser:
            targetUser = participants[0]
        else:
            targetUser = participants[1]
        return True, targetUser
    else:
        multiplePartipants = []
        for p in participants:
            if p != currentUser:
                multiplePartipants.append(p)
        return False, ', '.join(multiplePartipants)

def getUsername(jsonData):
    try:
        c1_name1 = jsonData[0]['participants'][0]
        c1_name2 = jsonData[0]['participants'][1]
        c2_name1 = jsonData[1]['participants'][0]
        c2_name2 = jsonData[1]['participants'][1]
    except:
        print('Less then two conversations exists, so you must type your username manually:')
        while True:
            res = input('--> ')
            if res:
                return res
            else:
                print('You must type a valid username!')
                continue
    else:
        if ( c1_name1 == c2_name1) or ( c1_name1 == c2_name2):
            return  c1_name1
        else:
            return c1_name2

def get_ctu(e):
    return e['created_at']
def getConversation(currentUser, targetUser, conversationsList):
    if len(targetUser) > len(currentUser):
        adjustLen = len(targetUser) + 1
    else:
        adjustLen = len(currentUser) + 1
    convListLen = len(conversationsList)

    path_textFormat = os.path.join(cnvDir, 'text-format', f'{targetUser}.txt')
    path_webFormat = os.path.join(cnvDir, 'web-format', f'{targetUser}.html')
    with open(path_textFormat, 'w') as convTxtFile, open(path_webFormat, 'w') as convHtmlFile:
        convHtmlFile.write( toHTML.initHeader(currentUser, targetUser) )
        for i in range(convListLen):
            #Initialsing it so the if statement will be
            #triggered for the first iteration of the for loop
            date_ymd = '-1'

            conversation = conversationsList[i]
            conversation.sort(key=get_ctu)
            # iterate through a list in reverse
            for convItem in conversation:
                if convItem['sender'] == currentUser:
                    sender = currentUser
                    posMsg = 'left'
                else:
                    sender = convItem['sender']
                    posMsg = 'right'

                try:
                    msg = convItem['text']
                except:
                    msg = '[NOT A MSG]'

                dateSent = convItem['created_at'][:16]

                old_date_ymd = date_ymd
                date_ymd = dateSent[:10]
                date_time= dateSent[11:16]
                if date_ymd > old_date_ymd:
                    convHtmlFile.write( toHTML.dateSeperator(str(date_ymd)))
                convLine = f'[{dateSent}] {sender.ljust(adjustLen)}: {str(msg)}'
                convTxtFile.write(convLine + '\n')
                convHtmlFile.write( toHTML.writeMsg(str(posMsg), str(msg), str(date_time)) )
        convHtmlFile.write( toHTML.closeHTML() )

def get_qtu(e):
    return e['msgQuantity']
def getMsgCount(jsonData, currentUser):
    listToShow = []
    for conversationObj in jsonData:
        if len(conversationObj['participants']) >= 2:
            if conversationObj['participants'][0] == currentUser:
                otherUserName = conversationObj['participants'][1]
            else:
                otherUserName = conversationObj['participants'][0]
            objectToShow = {
                'userName': otherUserName,
                'msgQuantity': len(conversationObj['conversation'])
            }
            listToShow.append(objectToShow)
    listToShow.sort(key=get_qtu, reverse=True)
    msgCountPath = os.path.join(cnvDir, 'messages-count.txt')
    with open(msgCountPath, 'w') as convQteFile:
        for objectToShow in listToShow:
            convQteLine = str(objectToShow['userName'].ljust(30)) + ' | ' + str(objectToShow['msgQuantity'])
            convQteFile.write(convQteLine + '\n')
    print('SUCCESS: Created message count with each user!')

if __name__ == '__main__':
    main()
