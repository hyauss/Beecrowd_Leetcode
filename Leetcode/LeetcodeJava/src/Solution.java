class Solution {
    public static int countOdds(int low, int high) {
        int oddNumbers = 0;
        if (low >= 0 && high >= low && high <= Math.pow(10, 9)) {
            for (; low <= high; low++) {
                if (low % 2 != 0) {
                    oddNumbers++;
                }
            }
            return oddNumbers;
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(countOdds(8, 10));
    }
}
