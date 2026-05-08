class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String stringValue : strs) {
            int sizeOfString = stringValue.length();
            sb.append(sizeOfString + "#" + stringValue);
        }

        System.out.println(sb.toString());

        return sb.toString();

    }

    public List<String> decode(String str) {
        List<String> response = new ArrayList<>();

        int index = 0;
        int prevIndex = index;


        while (index < str.length()) {
            char currentChar = str.charAt(index);
            if (currentChar == ('#')) {
                int sizeOfString = Integer.parseInt(str.substring(prevIndex, index));
                index += 1;
                response.add(str.substring(index, index + sizeOfString));
                index = index + sizeOfString;
                prevIndex = index;
            } else {
                index++;
            }
            
        }

        return response;
    }
}
