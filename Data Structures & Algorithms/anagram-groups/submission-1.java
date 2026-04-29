class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groups = new ArrayList<>();

        HashMap<String, List<String>> anagram_group = new HashMap<>();


        for (String words:strs) {
            List<String> group = new ArrayList<>();
            int[] seen = new int[26];
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < words.length(); i++) {
                seen[words.charAt(i) - 'a']++;
            }

            for (int count:seen) {
                sb.append('#');
                sb.append(count);
            }

            if (anagram_group.containsKey(sb.toString())) {
                anagram_group.get(sb.toString()).add(words);
            } else {
                group.add(words);
                anagram_group.put(sb.toString(), group);
            }
        }


        for (List<String> i:anagram_group.values()) {
            
            groups.add(i);
        }

        return groups;
    }
}
