#include <signal.h>
#include <stdio.h>
#include <sys/socket.h>
#include <sys/sendfile.h>
#include <netinet/in.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
typedef int MY_SOCKET_TYPE;
MY_SOCKET_TYPE s;
void sigterm_handler(int signum){
  printf("Closing socket");
  close(s);
  exit(0);
}
int main(int argc, char* argv[]){
  struct sigaction act;
  act.sa_handler = sigterm_handler;
  sigemptyset(&act.sa_mask);
  act.sa_flags=0;
  sigaction(SIGTERM, &act, NULL);
  sigaction(SIGINT, &act, NULL);
  s = socket(AF_INET, SOCK_STREAM, 0);
  struct sockaddr_in addr = {
    AF_INET,
    0x581b,
    0
  };
  bind(s, &addr, sizeof(addr));
  listen(s, 10);
  while(1){
    MY_SOCKET_TYPE client_fd = accept(s, 0, 0);
    char content[] = "<!DOCTYPE html><html><head><title>Mridul Gupta</title><style>body{background-color:#2e2e3a;}h1{font-family: sans-serif;margin-top:100px;color:#fcec52;text-align:center;}</style></head><body><h1>Hello World! I am Mridul Gupta.</h1></body></html>";
    char ok[4096] = {0};
    snprintf(ok, 4096, "HTTP/1.1 200 OK\r\nContent-type: text/html\r\nContent-length: %zu\r\n\r\n%s\r\n", strlen(content), content);
    send(client_fd, ok, sizeof(ok), 0);
    close(client_fd);
  }
  return 0;
}
