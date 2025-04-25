# Part 2  Jana,Lana,Tariq
import socket
import threading
import datetime

PORT = 5051
# broadcast_ip we use Radmin vpn online network not the one from my laptop ipconfig
broadcast_ip = '26.255.255.255'  
#this line retrieves the local IP address of the machine by getting the hostname, 
#resolving it to IP addresses, and selecting the first IP address from the list.
local_ip = socket.gethostbyname_ex(socket.gethostname())[2][0]
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
buffer=1024 # max num of data will be recived

def bring_time_of_now():
    # build in function that bring the time now
    return datetime.datetime.now().strftime("%H:%M:%S")

def mange_messeges(SOCKET_, received_messeges):
    while True:
        data, addr = SOCKET_.recvfrom(buffer)
       # cheak weather the messege is from peer itself or not
        if addr[0] != local_ip:
            messege = data.decode('utf-8')
            current_time = bring_time_of_now()
            received_messege = f"received a message from {messege.split(":")[0]} at {current_time}"
            received_messeges.append(messege)
            print(f"from peer {full_name}")
            print(received_messege)

def print_messages(messeges):
    print(f"\nPeer {full_name}") 
    # j represent the index of the tuple in messege list 
    for j, messege in enumerate(messeges, 1):
        print(f"{j}- {messege[0]}")


def print_full_messege(messeges, command):
   
    try:
        l = int(command[:-1]) - 1  
        print("\nFull message:")
        print(messeges[l][1])  
        #catches potential errors that may occur during the execution of the code inside the try block. 
        #If there's either an IndexError (which means the index l is out of range for the messages list) or 
        #a ValueError (which means the command couldn't be converted to an integer), it prints "Invalid command or index."
    except (IndexError, ValueError):
        print("Invalid command or index.")

def manage_sending_messege(SOCKET_, received_messeges):
    while True:
        com = input("\n please enter your message or [Digit_D] => (Message OR #D) ")

        # here we have two choices if u send Degit_D then the messege is sent to the peer server 
        if com.upper().endswith('D') and com[:-1].isdigit():
            print_full_messege(received_messeges, com)
        #else the messege is sent to other peers in the broadcast  
        else:
            full_message = f"{full_name}: {com}"
            SOCKET_.sendto(full_message.encode('utf-8'), (broadcast_ip, PORT))

def construct_peers():
    # creating a new socket
    SOCKET_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #tells the socket to allow the reuse of addresses
    SOCKET_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    SOCKET_.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    SOCKET_.bind((local_ip, PORT))
   
    #to save the recived messeges
    Received_messeges = []
    # to send messeges for all peers at the same time 
    #once the messege sent from one peer it sends to other
    threading.Thread(target=mange_messeges, args=(SOCKET_,  Received_messeges), daemon=True).start()
    manage_sending_messege(SOCKET_,  Received_messeges)

if __name__ == "__main__":
    construct_peers()






