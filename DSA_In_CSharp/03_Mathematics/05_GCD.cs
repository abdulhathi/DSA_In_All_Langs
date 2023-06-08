namespace Mathematics
{
    public class GreatestCommonDevisor {
        public int GCD(int a, int b) {
            if (b == 0)
                return a;
            return GCD(b, a % b);
        }
        public void Test() {
            Console.WriteLine(GCD(4, 6));
        }
    }
}