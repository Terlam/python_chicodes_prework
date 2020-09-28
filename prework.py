# Question 1 - Write a function to print "Hello_USERNAME"
def hello_name(user_name):
    print('hello' + user_name.upper() + '!')
    
hello_name('terrell')

# Question 2
def odd_numbers():
    for i in range(0,101,2):
        print(i)


#Question 3
def max_num_in_list(a_list):
    max_num = max(a_list)
    print(max_num)

# Question 4


# Question 5
def is_consecutive(a_list):
    i=0
    status = True
    while i > len(a_list) -1:
        if a_list[i] +1 == a_list[i +1]:
            i += 1
        else:
            status = False
            break
    print(status)