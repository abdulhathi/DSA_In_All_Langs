namespace Mathematics {
    public class PalindromeNumber {
        public bool checkIsPalindromeNumber(int num) {
            int temp = num, revNum = 0;
            while (temp > 0) {
                revNum *= 10;
                revNum = revNum + (temp % 10);
                temp /= 10;
            }
            return num == revNum;
        }
        public void Test() {
            Console.WriteLine("101 : "+ checkIsPalindromeNumber(101));
            Console.WriteLine("1011 : "+ checkIsPalindromeNumber(1011));
        }
    }
}