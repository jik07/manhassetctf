#include <stdio.h>


int main() {
  char buf[1024];
  char flag[64];

  // Read in the flag
  FILE *fd = fopen("flag.txt", "r");
  if (fd == NULL){
    printf("'flag.txt' file not found, aborting.\n");
    return 1;
  }
  fgets(flag, 64, fd);

  printf("Enter your name:\n");
  fflush(stdout);
  scanf("%1024s", buf);
  printf("Greetings! Hello ");
  printf(buf);
  printf("\n");
  fflush(stdout);

  return 0;
}