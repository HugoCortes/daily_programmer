using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace daily_programmer
{
    class solution_1
    {
        static void Main(string[] args)
        {
            String name = "", age = "", redditUser = "";
            name = GetInput("Enter your name: ");
            age = GetInput("Enter your age: ");
            redditUser = GetInput("Enter your Reddit username: ");
            Console.Write("Your name is {0}, you are {1} years old, and your username is {2}.", name, age, redditUser);
            Console.Read();
        }

        static String GetInput(string prompt)
        {
            String input = "";
            Console.Write(prompt);
            input = Console.ReadLine();
            return input;
        }
    }
}
