package Pull_Variante;

public class client {
    
    public static void main(String[] args) {
        station ws = new station();
        colorSignal signal = new colorSignal(ws);
       
        monitor m = new monitor(ws);
        ws.setHum(60.6f);
        ws.setTemp(35.9f);
    }

}
