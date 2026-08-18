#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netpacket/packet.h>
#include <net/ethernet.h>
#include <arpa/inet.h>

#define BUFFER_SIZE 2048

void print_packet_info(struct sockaddr_ll *addr, unsigned short ethertype) {
    // Display higher layer protocol type
    printf("Upper Protocol: ");
    switch (ethertype) {
        case ETH_P_IP:
            printf("IP, ");
            break;
        case ETH_P_ARP:
            printf("ARP, ");
            break;
        default:
            printf("Other (0x%04x), ", ethertype);
            break;
    }

    // Display packet type
    if (addr->sll_pkttype == PACKET_BROADCAST) {
        printf("Broadcast: ");
    } else if (addr->sll_pkttype == PACKET_MULTICAST) {
        printf("Multicast: ");
    } else if (addr->sll_pkttype == PACKET_HOST) {
        printf("Incoming: ");
    } else if (addr->sll_pkttype == PACKET_OUTGOING) {
        printf("Outgoing: ");
    } else {
        printf("Other type of packet: ");
    }
}

void print_packet_hex(const unsigned char *buffer, int length) {
    for (int i = 0; i < length; i++) {
        printf("%02x", buffer[i]);
    }
    printf("\n");
}

int main() {
    int sockfd;
    char buffer[BUFFER_SIZE];
    struct sockaddr_ll addr;
    socklen_t addr_len = sizeof(struct sockaddr_ll);
    ssize_t numbytes;
    struct ethhdr *eth_header;

    // Create a raw socket
    sockfd = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (sockfd == -1) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    while (1) {
        numbytes = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&addr, &addr_len);
        if (numbytes == -1) {
            perror("recvfrom");
            close(sockfd);
            exit(EXIT_FAILURE);
        }

        eth_header = (struct ethhdr *)buffer;
        print_packet_info(&addr, ntohs(eth_header->h_proto));
        print_packet_hex((unsigned char *)buffer, numbytes);
    }

    close(sockfd);
    return 0;
}
