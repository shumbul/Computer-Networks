#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<unistd.h>
#include<string.h>
#include<arpa/inet.h>
#include<stdlib.h>

int main(){
	struct sockaddr_in server_addr;
//	char send_data[1024],recv_data[1024];
	int sockfd,connectfd;

	if((sockfd=socket(AF_INET,SOCK_STREAM,0))==-1){
		printf("error creating socket...");
		return 1;
	}

	server_addr.sin_family=AF_INET;
	server_addr.sin_port=htons(7002);
	server_addr.sin_addr.s_addr=inet_addr("127.0.0.1");

	if((connectfd=connect(sockfd,(struct sockaddr*)&server_addr,sizeof(server_addr)))==-1){
		printf("error connecting...");
		return 1;
	}

	FILE* fp;
	int ch=0,itr;
	long siz;
	char buff[2];
	char choice[2];
	char num1[10],num2[10],op[2],result[10];
	while(1){
//		printf("Enter choice\n");
		printf("Calculator\n");
		printf("-------------------------------------\n");
//		printf("2. Exit\n");
//		scanf("%s",choice);
		choice[0]='1';
		send(sockfd,choice,2,0);
		choice[1]='\0';
		switch(choice[0]){
			case '1':
				bzero(num1,10);
				printf("Enter first number :");
				scanf("%s",num1);
				send(sockfd,num1,10,0);
				bzero(op,2);
				printf("Enter operator :");
				scanf("%s",op);
				op[1]='\0';
				send(sockfd,op,2,0);
				bzero(num2,10);
				printf("Enter second number :");
				scanf("%s",num2);
				send(sockfd,num2,10,0);
				bzero(result,10);
				recv(sockfd,result,10,0);
				printf("Result of %s %s %s = %s\n",num1,op,num2,result);

			break;

			default:
				ch=-1;
			break;
		}
	}

	close(sockfd);
	return 0;

}
