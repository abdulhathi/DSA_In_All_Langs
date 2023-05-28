namespace Mathematics {
    public class FactorialOfANumber {
        public int Factorial(int num) {
            int fact = 1;
            while (num > 0) {
                fact *= num;
                num -= 1;
            }
            return fact;
        }
        public void Test() {
            Console.WriteLine(Factorial(6));
        }
    }
}