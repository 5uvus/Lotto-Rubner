package Push_Variante;

public class monitor implements Observer {

    private station ws;

    public monitor(station ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update(float temp, float hum) {
        double temp1 = temp;
        double hum1 = hum;
        System.out.println("Temp: " + temp1 );
        System.out.println("Hum: " + hum1);
    }
    
}