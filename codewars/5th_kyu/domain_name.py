'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    answer = ''
    for i in range(len(url)):
        
        if url[i] == '/' or url[i] == '.':
            while url[i+1] == '/':
                answer += url[i+1]
            # print('answer: ', answer)
            # while url[i+1] != '/' or url[i+1] != '.':
            #     answer += url[i+1]
            #     print('answer: ', answer)
    print(answer)
 



    
if __name__ == "__main__":
    domain_name("http://github.com/carbonfive/raygun")