public class LeetCodeTest {
    public static void main(String[] args) {
        LeetCode leetCodeApp = new LeetCode();
        leetCodeApp.checkTags("brian, michael");
        String newString = "";
        System.out.println(leetCodeApp.checkTags("brian michael"));
    }
}