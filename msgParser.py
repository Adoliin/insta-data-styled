#!/usr/bin/python3
import json
import os
from pprint import pprint

# Read from database
with open('test.json','r') as dataFile:
    dataJSON = dataFile.read()
data = json.loads(dataJSON)

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
        with open('CNV-'+targetUser+'.txt', 'w') as convFile:
            for i in range(convListLen):
                conversation = conversationsList[i]
                conversation.sort(key=self.get_ctu)
                for convItem in conversation:
                    if convItem['sender'] == self.currentUserName:
                        sender = 'X'
                    else:
                        sender = convItem['sender']
                        
                    try:
                        msg = convItem['text']
                    except:
                        msg = '~~~'
                        
                    convLine = sender.ljust(adjustLen)+': '+ str(msg)
                    convFile.write(convLine + '\n')
        print('Conversation with %s is created.' %(targetUser))





if __name__ == '__main__':
    changeDir()
    currentUser = InstaProfile()
    targetUser = input('Type your target user: ')
    userFound, conversationsList = currentUser.targetExists(targetUser)
    if userFound == True:
        currentUser.returnConversation(targetUser, conversationsList)
    else:
        print('"%s" is not found :(' % (targetUser))
    currentUser.showCloseUsers()

