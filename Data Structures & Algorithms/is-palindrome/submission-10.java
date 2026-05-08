class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() == 0 || s.length() == 1) {
            return true;
        }
        int leftIndex = 0;
        int rightIndex = s.length() - 1;
        s = s.toLowerCase();

        while (leftIndex <= rightIndex) {
            while (leftIndex < rightIndex && !alphaNum(s.charAt(leftIndex))) {
                leftIndex++;
            }

            while (rightIndex > leftIndex && !alphaNum(s.charAt(rightIndex))) {
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

    public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
}
