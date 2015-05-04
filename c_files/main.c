#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void convert(int thousands, int hundreds, int tens, int ones)
{
char *num[] = {"", "One", "Two", "Three", "Four", "Five", "Six",
	       "Seven", "Eight", "Nine"};

char *for_ten[] = {"", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty",
		   "Seventy", "Eighty", "Ninty"};

char *af_ten[] = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
		  "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Ninteen"};

  printf("\nThe year in words is:\n");

  printf("%s thousand", num[thousands]);
  if (hundreds != 0)
    printf(" %s hundred", num[hundreds]);

  if (tens != 1)
    printf(" %s %s", for_ten[tens], num[ones]);
  else
    printf(" %s", af_ten[ones]);
}


int main()
{
int year;
int n1000, n100, n10, n1;

  TRACE("main beginning!");

  printf("\nEnter the year (4 digits): ");
  scanf("%d", &year);

  if (year > 9999 || year < 1000)
  {
    printf("\nError !! The year must contain 4 digits.");
    exit(EXIT_FAILURE);
  }

  TRACE("Reached here. I want to print the float number %f", 3.14159);

  n1000 = year/1000;
  n100 = ((year)%1000)/100;
  n10 = (year%100)/10;
  n1 = ((year%10)%10);

  convert(n1000, n100, n10, n1);

  TRACE("worker name is %s and id is %d", worker.name, worker.id);

return 0;
}
