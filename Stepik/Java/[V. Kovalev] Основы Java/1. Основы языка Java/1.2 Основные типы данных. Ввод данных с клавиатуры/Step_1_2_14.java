/*  Step 14 - Сумма цифр

Дано трехзначное число. Найдите сумму его цифр.

test:
Sample Input:
179

Sample Output:
17
*/

import java.util.Scanner;

class Step_1_2_14
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int number = sc.nextInt();

            int first_number = number / 100;
            int second_number = (number / 10) % 10;
            int third_number = number % 10;

            System.out.println(first_number + second_number + third_number);
        }
    }
}