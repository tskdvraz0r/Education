/*  Step 16 - Улитка

Улитка ползёт по вертикальному шесту высотой h метров, поднимаясь за день на a метров, а за ночь спускаясь на b метров. На какой день улитка доползёт до вершины шеста?
Программа получает на вход натуральные числа h, a, b. Гарантируется, что a>b.
Программа должна вывести одно натуральное число.

test:
Sample Input:
10
3
2

Sample Output:
8
*/

import java.util.Scanner;

class Step_1_2_16
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in))
        {
            int h = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();

            System.out.println((h - b - 1) / (a - b) + 1);
        }
    }
}