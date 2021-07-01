x=[]
def push_stack(x):
    x.append(int(input("ENTER ELEMENT TO BE PUSHED : ")))
def pop_stack():
    print("Popped element from stack is : ",x.pop())
def traversal(x):
    print(x)
choice=1
print("1. Inserting an element in stack !")
print("2. Deleting an element from stack !")
print("3. Displaying elements of stack !")
while choice==1 :
    ch = int(input("Enter the choice of operation to be performed on stack :"))
    if(ch==1):
        flag=1
        push_stack(x)
        while flag==1:
            flag = int(input("Do you want to continue the same operation ? (0-->NO and 1-->YES) : "))
            if flag==0:
                break
            push_stack(x)
    elif(ch==2):
        flag=1
        while flag==1:
            if not x:
                print("Stack has no more elements !")
                break
            else:
                pop_stack()
            flag = int(input("Do you want to continue the same operation ? (0-->NO and 1-->YES) : "))
            if flag == 0:
                break
    elif(ch==3):
        print("The elements of stack are --> ",end="")
        traversal(x)
    else:
        print("Wrong choice of operation on stack !")
    choice = int(input("Do you want to perform more operation ? (0-->NO and 1-->YES) : "))
    if choice == 0:
        break