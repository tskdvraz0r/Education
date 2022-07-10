/*  Step - ВАЛЛ-И 1

Путешествуя, ВАЛЛ-И попал в логово к Дракону. Чтобы остаться в живых ему надо угадать число, которое задумали его головы.
Первая голова называет любое целое число, вторая - увеличивает его на 3, а третья результат уменьшает в 2 раза.
Составьте программу, которая позволит ВАЛЛ-И безошибочно вычислять результат.



test:
Sample Input:
10

Sample Output:
6.5
*/

import java.util.Scanner;

class Step_1_3_01
{
    public static void main(String[] args)
    {
        try (Scanner sc = new Scanner(System.in)) {
            double number = sc.nextDouble();

            System.out.println((number + 3) / 2);
        }
    }
}