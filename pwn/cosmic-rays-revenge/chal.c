#include <stdio.h>

int unchangeableNum = 0x12345678;

int main() {
  char buf[1024];
  char flag[64];


  printf("Do you think you could change the unchangeableNum?\n");
  fflush(stdout);
  scanf("%1024s", buf);
  printf("Here's your input: ");
  printf(buf);
  printf("\n");
  fflush(stdout);

  if (unchangeableNum == 0xdeadbeef) {
    printf("Woah, cosmic rays must've changed the variable...\n");

    // Read in the flag
    FILE *fd = fopen("flag.txt", "r");
    fgets(flag, 64, fd);

    printf("%s", flag);
    fflush(stdout);
  }
  else {
    printf("unchangableNum = 0x%x\n", unchangeableNum);
    printf("Haha no flag for you!\n");
    fflush(stdout);
  }

  return 0;
}