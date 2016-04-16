package com.daily_programmer;

import java.util.Scanner;

public class Main{
    double result;
    public void Multiplication(int M, int A){
        result = M*A;
        System.out.println(String.format("Answer is: %f", result));
    }

    public void Division(int x, int y){
        result = x / y;
        System.out.println(String.format("Answer is: %f", result));
    }

    public static void main(String[] args) {
        System.out.println("Physics calculator for Force, Mass, and Acceleration");
        Main calc = new Main();
        switch(GetInput(
                "1. F = M * A\n" +
                "2. A = F / M\n" +
                "3. M = F / A") ){

            case 1:
                calc.Multiplication(GetInput("Enter M: "), GetInput("Enter A"));
                break;
            case 2:
                calc.Division(GetInput("Enter F: "), GetInput("Enter M"));
                break;
            case 3:
                calc.Division(GetInput("Enter F: "), GetInput("Enter A"));
                break;
        }
    }

    public static int GetInput(String prompt){
        Scanner reader = new Scanner(System.in);
        System.out.println(prompt);
        return reader.nextInt();
    }

}
