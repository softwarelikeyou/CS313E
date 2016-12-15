import sys


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

#function goes through file returns a string for each tag
def getTag(file):
    tag = ''
    recording = False
    while True:
        char = file.read(1)
        if not char:
            return ''
        if char == '<':
            recording = True
            continue
        if (char == '>' or char == ' ') and len(tag) != 0:
            return tag
        if recording == True:
            tag += char
            continue
          
def main():
    #intialize lists of exceptions, valid tags and tags
    EXCEPTIONS = ['br', 'meta', 'hr']
    VALIDTAGS = []
    tags = []
    #open file
    html = open("UNTITLED.txt", "r")
    #create a list of get tag
    while True:
        tag = getTag(html)
        if len(tag) == 0:
            break       
        tags.append(tag)

    print()
    #print tags
    print(tags)
    print()
    #declare stack
    m = Stack()
    #go through stack to find matches
    for tag in tags:
        if tag[0] == '/':
            if tag[1:] == m.peek():
                print('Tag ', m.pop(), ' matches top of stack:  stack is now ', m.items)
            else:
                print('Error:  tag is ', tag[1:], ' but top of stack is ', m.pop())
                #change why does it keep going through program needs to end
                sys.exit()
        else:
            if tag in EXCEPTIONS:
                print('Tag ', tag, ' does not need to match:  stack is still ', m.items)
               #change add exceptions to validtags
                if tag not in VALIDTAGS:
                     VALIDTAGS.append(tag)
                     print('Adding', tag, ' to list of valid tags') 
                continue
            m.push(tag)
            if tag not in VALIDTAGS and tag[0] != '/':
                VALIDTAGS.append(tag)
                print('Adding', tag, ' to list of valid tags') 
            print('Tag ', tag, ' pushed: stack is now ', m.items)

    print()
    #end processesing 
    if m.isEmpty():
        print('Processing complete.  No mismatches found.')
    else:
        print('Processing complete.  Unmatched tags remain on stack: ', m.items)

    print()
    EXCEPTIONS.sort()
    VALIDTAGS.sort()
    #final contents of sorted exceptions and validtags
    print('Exception tags are: ', EXCEPTIONS)
    print()
    print('Valid tags are: ', VALIDTAGS)
    
main()
