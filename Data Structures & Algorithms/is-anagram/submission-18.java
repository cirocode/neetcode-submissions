class Solution {
    public boolean isAnagram(String s, String t) {
        // Instinctual I want to keep count of the number of times a letter shows up
        // That would be O(n) but

        if (s.length() != t.length()) {
            return false;
        }

        int[] counts = new int[26];

        int size_s = s.length();
        for (int i = 0; i < size_s; i++) {

            counts[s.charAt(i) - 'a']++;
            counts[t.charAt(i) - 'a']--;
        };

        for (int val : counts) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
}
