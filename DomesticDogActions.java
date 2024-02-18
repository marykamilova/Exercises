public interface DomesticDogActions {
    void barks();
    void sleeps();
}

class Dog implements DomesticDogActions {

    @Override
    public void barks() {
        System.out.println("Woof");
    }

    @Override
    public void sleeps() {
        System.out.println("Snore");
    }

    public static void main(String... args) {
        Dog Yuki = new Dog();
        Yuki.barks();
    }
}