#!/usr/bin/python3
import json
import os
from pprint import pprint
from modules import toHTML

# Read from database
with open('test.json','r') as dataFile:
    dataJSON = dataFile.read()
data = json.loads(dataJSON)

def main():
    changeDir()
    currentUser = InstaProfile()
    targetUser = input('Type your target user: ')
    userFound, conversationsList = currentUser.targetExists(targetUser)
    if userFound == True:
        currentUser.returnConversation(targetUser, conversationsList)
    else:
        print('"%s" is not found :(' % (targetUser))
    # resCU = input('Create close users?[y/N]')
    # if resCU == 'y':
    # currentUser.showCloseUsers()

def changeDir():
    cnvDir = os.getcwd() + '/conversations'
    if os.path.exists(cnvDir) == False:
        os.mkdir(cnvDir)
    os.chdir(cnvDir)

class InstaProfile:
    def __init__(self):
        self.conversationNum = len(data)
        self.currentUserName = self.getUserName('current')

    def getUserName(self, option):
        a = data[0]['participants'][0]
        b = data[0]['participants'][1]
        c = data[1]['participants'][0]
        d = data[1]['participants'][1]
        if (a == c) or (a == d):
            return a
        else:
            return b
    # return if the target exists or not, in the affirmative it also returns
    # a list containing all the messages exchanged between him and target
    def targetExists(self, targetUser):
        conversationsList = []
        for i in range(self.conversationNum):
            if targetUser in data[i]['participants']:
                conversationsList.append(data[i]['conversation'])
        if len(conversationsList) > 0:
            return True, conversationsList
        else:
            return False, []

    def get_qtu(self,e):
        return e['msgQuantity']
    #print users by the most talked to
    def showCloseUsers(self):
        listToShow = []
        for conversationObj in data:
            if len(conversationObj['participants']) >= 2:
                if conversationObj['participants'][0] == self.currentUserName:
                    otherUserName = conversationObj['participants'][1]
                else:
                    otherUserName = conversationObj['participants'][0]
                objectToShow = {
                    'userName': otherUserName,
                    'msgQuantity': len(conversationObj['conversation'])
                }
                listToShow.append(objectToShow)
        listToShow.sort(key=self.get_qtu, reverse=True)
        #pprint(listToShow)
        with open(self.currentUserName+'-conv-qte.txt', 'w') as convQteFile:
            for objectToShow in listToShow:
                convQteLine = str(objectToShow['userName'].ljust(30)) + ' | ' + str(objectToShow['msgQuantity'])
                convQteFile.write(convQteLine + '\n')
        print('Close users created!')



    def get_ctu(self,e):
        return e['created_at']
    def returnConversation(self, targetUser, conversationsList):
        adjustLen = len(targetUser) + 1
        convListLen = len(conversationsList)
        with open(targetUser+'-CNV.txt', 'w') as convTxtFile, open('./frontend/'+targetUser+'-CNV.html', 'w') as convHtmlFile:
            convHtmlFile.write( toHTML.initHeader(targetUser) )
            for i in range(convListLen):
                conversation = conversationsList[i]
                conversation.sort(key=self.get_ctu)

                date_ymd = '-1' #Initialsing it so the if statement will be
                #triggered for the first iteration of the for loop

                # iterate through a list in reverse
                for convItem in conversation:
                    if convItem['sender'] == self.currentUserName:
                        sender = 'X'
                        posMsg = 'right'
                    else:
                        sender = convItem['sender']
                        posMsg = 'left'

                    try:
                        msg = convItem['text']
                    except:
                        msg = '~~~'

                    dateSent = convItem['created_at'][:16]

                    old_date_ymd = date_ymd
                    date_ymd = dateSent[:10]
                    date_time= dateSent[11:16]
                    if date_ymd > old_date_ymd:
                        convHtmlFile.write( toHTML.dateSeperator(str(date_ymd)))
                    convLine = sender.ljust(adjustLen)+': '+ str(msg)
                    convTxtFile.write(convLine + '\n')
                    convHtmlFile.write( toHTML.writeMsg(str(posMsg), str(msg), str(date_time)) )
            convHtmlFile.write( toHTML.closeHTML() )
        print('Conversation with %s is created.' %(targetUser))

if __name__ == '__main__':
    main()
