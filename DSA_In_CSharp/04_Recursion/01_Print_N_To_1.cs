namespace Recursion
{
    public class PrintNToOne {
        List<int> result = new List<int>();
        public List<int> PrintRecursively(int n) {
            if (n == 0)
                return result;
            result.Add(n);
            return PrintRecursively(n-1);
        }
        public void Test() {
            var result = PrintRecursively(5);
            Console.WriteLine(string.Join(",", result));
        }
    }
}