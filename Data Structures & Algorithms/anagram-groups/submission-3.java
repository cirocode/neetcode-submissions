class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // My code while looking up syntax. Correct answer just very messy.
    //     List<List<String>> groups = new ArrayList<>();

    //     HashMap<String, List<String>> anagram_group = new HashMap<>();


    //     for (String words:strs) {
    //         List<String> group = new ArrayList<>();
    //         int[] seen = new int[26];
    //         StringBuilder sb = new StringBuilder();
    //         for (int i = 0; i < words.length(); i++) {
    //             seen[words.charAt(i) - 'a']++;
    //         }

    //         for (int count:seen) {
    //             sb.append('#');
    //             sb.append(count);
    //         }

    //         if (anagram_group.containsKey(sb.toString())) {
    //             anagram_group.get(sb.toString()).add(words);
    //         } else {
    //             group.add(words);
    //             anagram_group.put(sb.toString(), group);
    //         }
    //     }


    //     for (List<String> i:anagram_group.values()) {
            
    //         groups.add(i);
    //     }

    //     return groups;
    // }
        Map<String, List<String>> res = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
