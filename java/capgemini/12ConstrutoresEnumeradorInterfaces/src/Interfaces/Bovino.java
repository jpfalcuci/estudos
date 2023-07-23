package Interfaces;

public class Bovino implements Animal {
	@Override
	public void animalSom() {
		System.out.println("Muuuu");
	}

	@Override
	public void animalComer() {
		System.out.println("Comendo capim");
	}
}
