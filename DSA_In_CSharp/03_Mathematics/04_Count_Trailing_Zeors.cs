namespace Mathematics
{
    
    public class CountTrailingZeros {
        // Count trailing zeros by divide by 5
        public int Count(int num) {
            int count = 0;
            while (num % 5 == 0) {
                num = num / 5;
                count += num;
            }
            return count;
        }
        public int CountMultipleOfFive(int num) {
            int count = 0;
            for (int i = 5; i <= num; i *= 5) {
                count = count + num / i;
            }
            return count;
        }
        public void Test() {
            Console.WriteLine(Count(100));
            Console.WriteLine(CountMultipleOfFive(251));
        }
    }
}