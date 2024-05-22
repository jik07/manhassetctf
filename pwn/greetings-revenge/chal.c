#include <stdio.h>

void flag() {
  FILE *fd = fopen("flag.txt", "r");
  fgets(flag, 64, fd);

  printf("%s", flag);
  fflush(stdout);
}

int main() {
  char buf[1024];

  printf("Enter your name:\n");
  fflush(stdout);
  scanf("%1024s", buf);
  printf("Greetings! Hello ");
  printf(buf);
  printf("\n");
  fflush(stdout);

  return 0;
}