#include <iostream>

int foo()
{
  return 10;
}
int main()
{
  int a = 0;
  int b = 20;

  a++ && ++b;

  std::cout << a << std::endl;
}