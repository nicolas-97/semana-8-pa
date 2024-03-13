import notifiers.Notifier;
import subscribers.Subscriber;

public class Main {

	public static void main(String[] args) {
		Notifier notifier = new Notifier();
		
		Subscriber subscriberOne = new Subscriber("Nicolas");
		Subscriber subscriberTwo = new Subscriber("Juan");
		
		notifier.attach(subscriberOne);
		notifier.attach(subscriberTwo);
		
		notifier.notify("Hola a todos");
		
		notifier.detachh(subscriberOne);
		
		notifier.notify("Ahora solo tenemos un suscriptor");
	}

}
