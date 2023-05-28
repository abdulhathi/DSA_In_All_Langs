namespace Mathematics {
    public class CountDigits {
        public int CountDigitsInNumber(int num) {
            int count = 0;
            while (num > 0) {
                count += 1;
                num = num / 10;
            }
            return count;
        }
        public void Test() {
            Console.WriteLine(new CountDigits().CountDigitsInNumber(222));
        }
    }
}