#protected mthd
'''
class Instagram:
    def __init__(self):
        self._post=[]
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)
harika=Instagram()
print(harika.accesspost)
harika.accesspost='class and object'
print(harika.accesspost)
'''

#inheritance
'''1.single inheritence
2.multiple-many parents witgh single cghild
3.level
4.hi
5.hy'''
#single inheritance'
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")
harika=whatsappv1()
print("v1-harika")
harika.message()


subha=whatsappv2()
print("v2-subha")
subha.message()
subha.calls()
'''
#multiple inheritance
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")
        
class whatsappv2:
    def calls(self):
        print("You can do video/audio calls")
                
class whatsappv3:
    def media(self):
        print("You can share your photos/videos")
                
class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")
        
harika=whatsappv4()
print("v4-harika")
harika.message()
harika.calls()
harika.media()
harika.status()
'''
#multilevel inheritance
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")
        
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")
                
class whatsappv3(whatsappv2):
    def media(self):
        print("You can share your photos/videos")
                
class whatsappv4(whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")
        
harika=whatsappv4()
print("v4-harika")
harika.message()
harika.calls()
harika.media()
harika.status()
'''
#hierachical inhgeritance-many childerns and single parent
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")
        
class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people ")
                
class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")
harika=whatsappv3()
print("v3-harika")
harika.message()
harika.stickers()
'''
#hybrid inheritance-any combination
'''
class whatsappv1:
    def message(self):
        print("You can send messages to people")
        
class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people ")
                
class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")
class whatsappv4(whatsappv3,whatsappv2):
    def gift(self):
        print("You can send messages with stickers to people")
        
        
harika=whatsappv4()
print("v4")
harika.message()
harika.stickers()
harika.emojis()
harika.gift()
'''
#using super mthd
'''
class wpv1:
    def status(self):
        print("you can upload images/videos")
class wpv2(wpv1):
    def status(self):
        super().status()
        print("you can react and reply")
class wpv3(wpv2):
    def status(self):
        super().status()
        print("you can like and reshare")
harika=wpv3()
harika.status()
'''

'''
class wpv1:
    def status(self):
        print("you can upload images/videos")
class wpv2(wpv1):
    def status(self):
        print("you can react and reply")
class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("you can like and reshare")
harika=wpv3()
harika.status()
'''
