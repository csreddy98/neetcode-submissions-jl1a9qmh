class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> smap = new HashMap<>();
        Map<Character, Integer> tmap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char schar = s.charAt(i);
            char tchar = t.charAt(i);
            int sval = smap.getOrDefault(schar, 0) + 1;
            int tval = tmap.getOrDefault(tchar, 0) + 1;
            smap.put(schar, sval);
            tmap.put(tchar, tval);
        }

        return smap.equals(tmap);
    }
}
