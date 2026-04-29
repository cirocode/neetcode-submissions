class Solution {
    public boolean isAnagram(String s, String t) {
        // Instinctual I want to keep count of the number of times a letter shows up
        // That would be O(n) but

        if (s.length() != t.length()) {
            return false;
        }

        int[] transform = new int[26];
        Arrays.fill(transform, 0);
        int reference_a = (int) 'a';
        Integer size_s = s.length();
        for (int i = 0; i < size_s; i++) {
            char character_s = s.charAt(i);
            char character_t = t.charAt(i);
            int ascii_s = (int) character_s;
            int ascii_t = (int) character_t;


            transform[ascii_s - reference_a] += 1;
            transform[ascii_t - reference_a] -= 1;
        };

        for (int i = 0; i < transform.length; i++) {
            System.out.println(transform[i]);
            if (transform[i] != 0) {
                return false;
            }
        }

        return true;
    }
}
