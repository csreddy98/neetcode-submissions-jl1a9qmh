class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> sCount = new HashMap<>();
        HashMap<Character, Integer> tCount = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            sCount.put(s.charAt(i), sCount.getOrDefault(s.charAt(i) + 1, 0));
            tCount.put(t.charAt(i), tCount.getOrDefault(t.charAt(i) + 1, 0));
        }

        return sCount.equals(tCount);
    }
}
