public class PasswordCheck {

    static void passwordLength(String password) throws ArithmeticException {
        if (password.length() < 10) {
            throw new ArithmeticException("Password is too short, try again");
        }
        else {
            System.out.println("Strong password");
        }
    }
    public static void main(String[] args) {
        passwordLength("afhj");
    }
}
