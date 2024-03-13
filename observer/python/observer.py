#Definimos la interfaz para los suscriptores
class ISubscriber:
    def update(self, message):
        pass


#Definimos el notificador
class Notifier:
    def __init__(self) -> None:
        self._subscribers = []
    
    def attach(self, subscriber: ISubscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
    
    def detach(self, subscriber: ISubscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
    
    def notify(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)

# creamos un suscriptor concreto
class Subscriber(ISubscriber):
    def __init__(self, name) -> None:
        self._name = name
        super().__init__()

    def update(self, message):
        print(f"{self._name} recibió el mensaje: {message}")


if __name__ == '__main__':
    #Insrtanciamos el notificador
    notifier = Notifier()

    # creamos los suscriptores
    subscriber_one = Subscriber("Nicolas")
    subscriber_two = Subscriber("Juan")

    # agregamos el suscriptor al notificador
    notifier.attach(subscriber_one)
    notifier.attach(subscriber_two)

    #SImulamos el evento que lanza la notificacion
    notifier.notify("Ha ocurrido el evento")

    # Eliminamos un suscriptor
    notifier.detach(subscriber_one)

    # Notificamos de nuevo
    notifier.notify("Solo quedó un observador.")
