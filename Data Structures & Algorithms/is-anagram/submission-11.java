class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> smap = new HashMap<>();
        Map<Character, Integer> tmap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            // char schar = s[i];
            // char tchar = t[i];
            int sval = smap.getOrDefault(s.charAt(i), 0) + 1;
            int tval = tmap.getOrDefault(t.charAt(i), 0) + 1;
            smap.put(s.charAt(i), sval);
            tmap.put(t.charAt(i), tval);
        }

        return smap.equals(tmap);
    }
}
