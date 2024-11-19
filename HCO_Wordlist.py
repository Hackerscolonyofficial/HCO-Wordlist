import itertools, os
import colorama
import string, time
os.system('clear')
head_text = ''' \033[32m

          ██░ ██  ▄████▄   ▒█████                                         
         ▓██░ ██▒▒██▀ ▀█  ▒██▒  ██▒                                       
         ▒██▀▀██░▒▓█    ▄ ▒██░  ██▒                                       
         ░▓█ ░██ ▒▓▓▄ ▄██▒▒██   ██░                                       
         ░▓█▒░██▓▒ ▓███▀ ░░ ████▓▒░                                       
          ▒ ░░▒░▒░ ░▒ ▒  ░░ ▒░▒░▒░                                        
          ▒ ░▒░ ░  ░  ▒     ░ ▒ ▒░                                        
          ░  ░░ ░░        ░ ░ ░ ▒                                         
          ░  ░  ░░ ░          ░ ░                                         
                 ░                                                        
 █     █░ ▒█████   ██▀███  ▓█████▄  ██▓     ██▓  ██████ ▄▄▄█████▓  ██████ 
▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██    ▒ 
▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░░ ▓██▄   
░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌▒██░    ░██░  ▒   ██▒░ ▓██▓ ░   ▒   ██▒
░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██████▒░██░▒██████▒▒  ▒██▒ ░ ▒██████▒▒
░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ▒ ▒▓▒ ▒ ░
  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    ░ ░▒  ░ ░
  ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░   ░ ░    ▒ ░░  ░  ░    ░      ░  ░  ░  
    ░        ░ ░     ░        ░        ░  ░ ░        ░                 ░  
                            ░                                             

\033[33;1;35;5m
This Tool is Free For Our subscribers
We are Redirecting You To Our YouTube Channel
You Will Subscribe Our Channel
After Doing It You Will Able To Use Our Tool.... \033[0m'''

end_text = '''\033[31m
                ██   ██  ██████  ██████                                
                ██   ██ ██      ██    ██                               
                ███████ ██      ██    ██                               
                ██   ██ ██      ██    ██                               
                ██   ██  ██████  ██████                                
                                                                       
                                                                       
██     ██  ██████  ██████  ██████  ██      ██ ███████ ████████ ███████ 
██     ██ ██    ██ ██   ██ ██   ██ ██      ██ ██         ██    ██      
██  █  ██ ██    ██ ██████  ██   ██ ██      ██ ███████    ██    ███████ 
██ ███ ██ ██    ██ ██   ██ ██   ██ ██      ██      ██    ██         ██ 
 ███ ███   ██████  ██   ██ ██████  ███████ ██ ███████    ██    ███████ 
                                                                       
                                                                       
\033[37;45;5m
 __          _     _        _                   
(_     _| o |_)   |_) __ _ (_| __ _ __ __  _  __
__)|_|(_| | |     |   | (_)__| | (_|||||||(/_ | 
                                                

\033[0m'''




def typewriter(text):
    for txt in text:
        print(txt, end='', flush=True)
        time.sleep(0.02)
    print()

def generate_wordlist(length, chars):
    return (''.join(candidate) for candidate in itertools.product(chars, repeat=length))

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')

typewriter(head_text)
time.sleep(2)


channel_url = 'https://youtube.com/@hackers_colony_tech?si=7FEalwT2t0khmivd'

os.system(f'termux-open {channel_url}')
time.sleep(4)

os.system('clear')

typewriter(end_text)



sym = "\033[34m[\033[31m°•°\033[34m]\033[0m"


def main():
    length = int(input(f"{sym} \033[33;1mEnter password length: "))
    use_uppercase = input(f"{sym} \033[33;1m Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input(f"{sym} \033[33;1m Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input(f"{sym} \033[33;1m Include symbols? (y/n): ").lower() == 'y'
    file = input(f"{sym} \033[33;1m Enter file name (endswith .txt):  ")

    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    wordlist = generate_wordlist(length, chars)
    save_wordlist(wordlist, file)

    pa = os.getcwd()
    print("\033[36;1mYour file path is :\033[31m "+pa+'/'+file)

    channel_url = 'https://youtube.com/@hackers_colony_tech?si=7FEalwT2t0khmivd'

    os.system(f'termux-open {channel_url}')

if __name__ == "__main__":
    main()
