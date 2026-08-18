#include <stdio.h> 
#include <unistd.h> 
#include <netdb.h> 
#include <stdlib.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <sys/types.h> 
#include <string.h> 
#define SA struct sockaddr 
#define size_buff_server 8
#define PORT 8080 


// Function for chating between client and server. 
void chat_func(int my_info, char client_ip[]) 
{ 	
	int flag = 1;
	//buffer save the respond 
	char buffer_server[size_buff_server]; 
	int ctr; 
	int is_first_time = 1;
	
	if(is_first_time){
		printf("\n%s $ ", client_ip);
		//this function will clear the buffer
			bzero(buffer_server, size_buff_server);
			int j = 0;
			//geting input from server
			while ((buffer_server[j++] = getchar()) != '\n');
				 

		// and send that to client 
			write(my_info, buffer_server, sizeof(buffer_server)); 
			bzero(buffer_server,size_buff_server);
	}

	//clear the buffer
	bzero(buffer_server, size_buff_server);

	while(1){
		int is_finished = 0;	
		//check if server get the respond completly or not 
		for(int j = 0; j < 8; j++){
			if(buffer_server[j] == '*'){
				is_finished = 1;
				break;
			}
		}

		if(is_finished == 1)
			//printig respond
			printf("%s**\n", buffer_server);
		else
			printf("%s", buffer_server);
		ctr = 0; 
	 
		if(is_finished == 1){
			printf("\n%s $ ", client_ip);
			bzero(buffer_server, size_buff_server);
			while ((buffer_server[ctr++] = getchar()) != '\n');
				 

			//send new command to client
			write(my_info, buffer_server, sizeof(buffer_server));  
			if (strncmp("finish", buffer_server, 6) == 0) { 
				printf("Server close the chat...\n"); 
				break; 
			} 
		
	
			bzero(buffer_server, size_buff_server); 
		}
//server by sending + shows to client that the respond is not complete!
		else if(is_first_time != 1 && is_finished != 1){
			bzero(buffer_server, size_buff_server);
			buffer_server[0] = '+';
			write(my_info, buffer_server, sizeof(buffer_server));
		}
		is_first_time = 0;
		//read respond and copy it in buffer
		read(my_info, buffer_server, sizeof(buffer_server)); 
	} 
} 


int main() 
{ 
	int my_socket, my_info, len_info; 
	struct sockaddr_in server_add, client_add; 

	// create socket
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
	server_add.sin_addr.s_addr = htonl(INADDR_ANY); 
	server_add.sin_port = htons(PORT); 

	// Binding 
	if ((bind(my_socket, (SA*)&server_add, sizeof(server_add))) != 0) { 
		printf("socket bind failed....\n"); 
		exit(0); 
	} 
	else
		printf("Socket binded...\n"); 

	// serever is listening...
	if ((listen(my_socket, 5)) != 0) { 
		printf("Listen failed...\n"); 
		exit(0); 
	} 
	else
		printf("Server is listening...\n"); 
	len_info = sizeof(client_add); 

	// accepting client
	my_info = accept(my_socket, (SA*)&client_add, &len_info); 
	if (my_info < 0) { 
		printf("server accept failed...\n"); 
		exit(0); 
	} 
	else
		printf("A new client connected to sever:\n");
		char client_ip[INET_ADDRSTRLEN];
		inet_ntop(AF_INET,&client_add.sin_addr, client_ip, INET6_ADDRSTRLEN);


	// Function for chatting between client and server 
	chat_func(my_info, client_ip); 

	// closing socket 
	close(my_socket); 
}

