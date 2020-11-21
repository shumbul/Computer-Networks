#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<unistd.h>
#include<string.h>
#include<arpa/inet.h>
#include<stdlib.h>

int main(){
	
	struct sockaddr_in server_addr,client_addr;
	int sockfd,bytes_recv,connectfd,true=1;
	socklen_t size;

	sockfd=socket(AF_INET,SOCK_STREAM,0);

	if(sockfd==-1){
		printf("error creating socket...");
		return 1;
	}

	bzero((char *) &server_addr, sizeof(server_addr));
	server_addr.sin_family=AF_INET;
	server_addr.sin_port=htons(7002);
	server_addr.sin_addr.s_addr=INADDR_ANY;

	if((bind(sockfd,(struct sockaddr*)&server_addr,sizeof(server_addr)))==-1){
		printf("error binding...");
		return 1;
	}

	if(listen(sockfd,5)==-1){
		printf("error listening...");
		return 1;
	}

	printf("server waiting for client...\n");

	size=sizeof(client_addr);
	connectfd=accept(sockfd,(struct sockaddr*)&client_addr,&size);

	printf("got connected to client...\n");

	int ch=0;
	long siz;
	char buff[2];
	char choice[2],temp[10],op[2];
	int num1,num2;
	int result;
	char res[10];
	while(1){
		recv(connectfd,choice,2,0);
		choice[1]='\0';
		switch(choice[0]){
			case '1':
				bzero(temp,10);
				recv(connectfd,temp,10,0);
				printf("received data : %s\n",temp);
				num1=atoi(temp);
				bzero(op,2);
				recv(connectfd,op,2,0);
				printf("received data : %s\n",op);
				bzero(temp,10);
				recv(connectfd,temp,10,0);
				printf("received data : %s\n",temp);
				num2=atoi(temp);

				switch(op[0]){
					case '+':
						result=num1+num2;
					break;
					case '-':
						result=num1-num2;
					break;
					case '*':
						result=num1*num2;
					break;
					case '/':
						result=num1/num2;
					break;
				}
				printf("result is : %d\n",result);
				sprintf(res,"%d",result);
				send(connectfd,res,10,0);
			break;
			default:
				ch=-1;
			break;
		}
	}

	close(sockfd);

	return 0;
}

