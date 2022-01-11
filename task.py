
import sys

text_file = open("task.txt", "a")



def sorter(file_name):
    file_contents = [line.rstrip('\n') for line in file_name.readlines()] # Text should not get printed with an extra space
    file_name.close()
    big_ls = []
    for i in range(len(file_contents)):
        m = file_contents[i].split()
        m[1 : ] = [' '.join(m[1 : ])]
        m[0] = int(m[0]) #Converting to string type varna vo file sort nahi hota
        big_ls.append(m)
    big_ls.sort(key = lambda x: x[0])
        
#This loop appends a index
    for i in range(len(file_contents)):
        big_ls[i].append(i+1)
    return big_ls

##########Function for Deletion#######################################
def deletion(deletion_index):
    text_file = open('task.txt', 'r')
    file_contents = sorter(text_file)
    for i in range(len(file_contents)):
        #sys.stdout.buffer.write(file_contents[i][2])
        #sys.stdout.buffer.write(sys.argv[2])
        if str(file_contents[i][2]) == str(deletion_index):
            del file_contents[i]
            #sys.stdout.buffer.write(file_contents[0])
            new_content = [str(k[0])+' '+k[1] for k in file_contents]
            #sys.stdout.buffer.write(new_content)
            
            del_file = open("task.txt", "w")

            for element in new_content:

                del_file.write(element + "\n")

            del_file.close()

            break
        elif i == len(file_contents)-1:
            q = 'Error: task with index #' +str(sys.argv[2])+ ' does not exist. Nothing deleted.'
            sys.stdout.buffer.write(q.encode('utf8'))

#######################################Our Help Function###############   

if len(sys.argv) < 2:
    w = '''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics'''
    sys.stdout.buffer.write(w.encode('utf8'))

#Help Function
elif sys.argv[1] == "help":
    w = '''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics'''
    sys.stdout.buffer.write(w.encode('utf8'))

    
###########################TO add an item in a list we use this part of code################################
elif sys.argv[1] == "add":
    try:
        text_file.write(sys.argv[2] + " ")
        text_file.write(sys.argv[3] + "\n")
        print(sys.argv[2])
        text_file.close()
        e = "Added task: " + '"' + str(sys.argv[3]) + '" ' + "with priority " + str(sys.argv[2])
        sys.stdout.buffer.write(e.encode('utf8'))
    except:
        b = 'Error: Missing tasks string. Nothing added!'
        sys.stdout.buffer.write(b.encode('utf8'))

###########################TO ls an item in a list we use this part of code################################
elif sys.argv[1] == "ls":
    text_file = open('task.txt', 'r')
    file_contents = sorter(text_file)
    if file_contents == [] or file_contents == None:
        x = 'There are no pending tasks!'
        sys.stdout.buffer.write(x.encode('utf8'))
    else:
        for i in range(len(file_contents)):
            r = str(file_contents[i][2]) + '. ' + str(file_contents[i][1])  + ' ['+ str(file_contents[i][0]) + ']' + '\n'
            sys.stdout.buffer.write(r.encode('utf8'))

###########################TO del an item in a list we use this part of code################################
elif sys.argv[1] == "del":
    try:
        deletion(sys.argv[2])
        v = 'Deleted task #' + str(sys.argv[2])
        sys.stdout.buffer.write(v.encode('utf8'))

    except:
        v = 'Error: Missing NUMBER for deleting tasks.'
        sys.stdout.buffer.write(v.encode('utf8'))

###########################TO complete an item in a list we use this part of code################################
elif sys.argv[1] == "done":
    text_file = open('task.txt', 'r')
    file_contents = sorter(text_file)
    #sys.stdout.buffer.write(file_contents)
    try:
        for i in range(len(file_contents)):
            if str(file_contents[i][2]) == str(sys.argv[2]):

                comp_file = open("completed.txt", "a")
                comp_file.write(file_contents[i][1] + "\n")
                comp_file.close()
                t = 'Marked item as done.'
                sys.stdout.buffer.write(t.encode('utf8'))
                deletion(sys.argv[2])
                break
            elif i == len(file_contents)-1:
                t = 'Error: no incomplete item with index #' + str(sys.argv[2]) + ' exists.'
                sys.stdout.buffer.write(t.encode('utf8'))
    except:
        t = 'Error: Missing NUMBER for marking tasks as done.'
        sys.stdout.buffer.write(t.encode('utf8'))

###########################TO generate a report we use this part of code################################
elif sys.argv[1] == "report":
    
    text_file = open('task.txt', 'r')
    file_contents = sorter(text_file)
    y = 'Pending : ' + str(len(file_contents)) + '\n'
    sys.stdout.buffer.write(y.encode('utf8'))
    for i in range(len(file_contents)):
        u = str(file_contents[i][2]) + '. ' + str(file_contents[i][1]) + ' ['+ str(file_contents[i][0]) + ']' + '\n' + '\n'
        sys.stdout.buffer.write(u.encode('utf8'))
    text_file.close()
    
    text_file = open('completed.txt', 'r')
    file_contents = [line.rstrip('\n') for line in text_file.readlines()] # Text should not get sys.stdout.buffer.writeed with an extra space
    text_file.close()
    p = 'Completed : ' + str(len(file_contents)) + '\n'
    sys.stdout.buffer.write(p.encode('utf8'))
    for i in range(len(file_contents)):
        g = str(i+1) + '. ' + str(file_contents[i]) + '\n'
        sys.stdout.buffer.write(g.encode('utf8'))

        


