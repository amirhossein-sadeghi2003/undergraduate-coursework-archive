#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netpacket/packet.h>
#include <net/ethernet.h>
#include <arpa/inet.h>

#define BUFFER_SIZE 2048

void print_packet(unsigned char *buffer, int size) {
    for (int i = 0; i < size; i++) {
        //if (i != 0 && i % 16 == 0)  //printf("\n");
        printf("%.2x", buffer[i]);
    }
    printf("\n");
}

void print_packet_type(struct sockaddr_ll *sockaddr_ll) {
    switch (sockaddr_ll->sll_pkttype) {
        case PACKET_HOST:
            printf("Packet Type: Incoming\n");
            break;
        case PACKET_BROADCAST:
            printf("Packet Type: Broadcast\n");
            break;
        case PACKET_MULTICAST:
            printf("Packet Type: Multicast\n");
            break;
        case PACKET_OUTGOING:
            printf("Packet Type: Outgoing\n");
            break;
        default:
            printf("Packet Type: Other\n");
    }
}

int main() {
    int sockfd, len;
    char buffer[BUFFER_SIZE];
    struct sockaddr_ll phyaddr;

    sockfd = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (sockfd < 0) {
        perror("Socket creation failed");
        return 1;
    }

    while (1) {
        len = sizeof(struct sockaddr_ll);
        int n = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&phyaddr, &len);
        if (n < 0) {
            perror("Recvfrom error");
            return 1;
        }

        //printf("Received Packet:\n");
        print_packet_type(&phyaddr);
        print_packet((unsigned char *)buffer, n);
        
        printf("\n");
    }

    close(sockfd);
    return 0;
}
