package Factory;

public class HamburgSalami extends CreatePizza {

	public void backen() {
		System.out.println("Hamburg Salami backen");
	}
	public void schneiden() {
		System.out.println("Hamburg Salami schneiden");
	}
	public void einpacken() {
		System.out.println("Hamburg Salami einpacken");
	}
}