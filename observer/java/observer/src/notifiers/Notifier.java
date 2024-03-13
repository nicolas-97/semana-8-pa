package notifiers;

import java.util.ArrayList;
import java.util.List;

import interfaces.ISubscriber;

public class Notifier {
	private List<ISubscriber> subscribers = new ArrayList<>();
	
	public void attach(ISubscriber subscriber) {
		this.subscribers.add(subscriber);
	}
	
	public void detachh(ISubscriber subscriber) {
		this.subscribers.remove(subscriber);
	}
	
	public void notify(String message) {
		for(ISubscriber subscriber : this.subscribers) {
			subscriber.update(message);
		}
	}
}
