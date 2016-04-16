package com.daily_programmer;

import java.util.Scanner;

public class Main {

    String name, age, redditun;

    public Main(String name, String age, String redditun){
        this.name = name;
        this.age = age;
        this.redditun = redditun;
    }

    public void displayInfo(){
        System.out.println(String.format("Your name is %s, you are %s years old, and your username is %s."
                , name, age, redditun));
    }

    
    public static void main(String[] args) {
        Main user = new Main(GetInput("Enter your name:"), GetInput("Enter your age:"), GetInput("Enter your username"));
        user.displayInfo();
    }

    public static String GetInput(String prompt){
        Scanner reader = new Scanner(System.in);
        System.out.println(prompt);
        return reader.nextLine();
    }
}
