package subscribers;

import interfaces.ISubscriber;

public class Subscriber implements ISubscriber{
	private String name;
	
	public Subscriber(String name) {
		this.name = name;
	}
	
	@Override
	public void update(String message) {
		System.out.println(this.name + " recibió el mensaje: " + message);
	}
}
