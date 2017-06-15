import collections

FAILURE = -1
SUCCESS = 0
CONTINUE = 1

num_cookies, min_s = [int(x) for x in input().split()]
alist = input().split()
nlist = [int(c) for c in alist]
nlist.sort()

cookies = collections.deque(nlist)

print(cookies)

def sweeten(c1, c2):
    return c1+2*c2

def one_iter(cookies):
    if len(cookies) == 1:
        if cookies[0] >= min_s:
            return SUCCESS, None
        else:
            return FAILURE, None
    if cookies[0] >= min_s and cookies[1] >= min_s:
        return SUCCESS
    c1 = cookies.popleft()
    c2 = cookies.popleft()
    new_cookie = sweeten(c1,c2)

    return CONTINUE, new_cookie

counter = 0
while True: 
    r, new_cookie = one_iter(cookies)
    cookies.append(new_cookie)
    c = list(cookies)
    c.sort()
    cookies = collections.deque(c)
   
    if r == FAILURE:
        print(FAILURE)
        break
    elif r == SUCCESS:
        print(counter)
        break
        
    counter = counter+1
       
            







