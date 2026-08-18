#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <net/ethernet.h>
#include <netinet/ip.h>
#include <netinet/if_ether.h>
#include <linux/if_packet.h>
#include <linux/if_ether.h>

#define BUFFER_SIZE 2048

int main() {
    int sockfd;
    char buffer[BUFFER_SIZE];
    struct sockaddr_ll addr;
    socklen_t addr_len = sizeof(struct sockaddr_ll);

    // Create a raw socket
    if ((sockfd = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL))) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    while (1) {
        int numbytes = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&addr, &addr_len);
        if (numbytes < 0) {
            perror("Recvfrom error");
            continue;
        }

        struct ethhdr *eth = (struct ethhdr *)buffer;
        unsigned short ether_type = ntohs(eth->h_proto);

        if (ether_type == ETH_P_IP) {
            struct iphdr *ip = (struct iphdr *)(buffer + sizeof(struct ethhdr));
            unsigned short ip_header_len = ip->ihl * 4;
            unsigned short total_len = ntohs(ip->tot_len);
            unsigned short proto = ip->protocol;

            printf("Upper Protocol: IP (header len: %d, total len: %d, proto: %d), ", ip_header_len, total_len, proto);
        } else if (ether_type == ETH_P_ARP) {
            printf("Upper Protocol: ARP, ");
        } else {
            printf("Upper Protocol: OTHER, ");
        }

        if (memcmp(eth->h_dest, "\xff\xff\xff\xff\xff\xff", 6) == 0) {
            printf("Broadcast: ");
        } else if (eth->h_dest[0] & 0x01) {
            printf("Multicast: ");
        } else {
            if (memcmp(eth->h_source, addr.sll_addr, 6) == 0) {
                printf("Outgoing: ");
            } else {
                printf("Incoming: ");
            }
        }

        for (int i = 0; i < numbytes; i++) {
            printf("%02x", (unsigned char)buffer[i]);
        }
        printf("\n");
    }

    close(sockfd);
    return 0;
}
