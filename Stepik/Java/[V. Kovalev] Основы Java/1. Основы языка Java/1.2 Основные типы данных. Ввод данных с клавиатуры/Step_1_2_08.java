/*  Step 08 - Произведение

Напишите программу, которая считывает три целых числа и выводит их произведение. 

test:
Sample Input:
5
4
2

Sample Output:
40
*/

import java.util.Scanner;

class Step_1_2_08
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            System.out.println(a * b * c);
        }
    }
}