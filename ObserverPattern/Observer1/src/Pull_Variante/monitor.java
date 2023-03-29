package Pull_Variante;

public class monitor implements Observer {

    private station ws;

    public monitor(station ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update() {
        double temp = ws.getTemp();
        double hum = ws.getHum();
        System.out.println("Temp: " + temp );
        System.out.println("Hum: " + hum);
    }
    
}