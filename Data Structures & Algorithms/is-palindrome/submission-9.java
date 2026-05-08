class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() == 0 || s.length() == 1) {
            return true;
        }
        int leftIndex = 0;
        int rightIndex = s.length() - 1;
        s = s.toLowerCase();

        while (leftIndex <= rightIndex) {
            while (leftIndex < rightIndex && !Character.isLetterOrDigit(s.charAt(leftIndex))) {
                leftIndex++;
            }

            while (rightIndex > leftIndex && !Character.isLetterOrDigit(s.charAt(rightIndex))) {
                rightIndex--;
            }

            if (s.charAt(leftIndex) == s.charAt(rightIndex)) {
                leftIndex++;
                rightIndex--;
            } else {
                return false;
            }
        }

        return true;
        
    }
}
