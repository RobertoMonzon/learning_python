# Create an instance of the Alarm class, which has a method called snooze(amount_minutes). The method should print the message on the screen.

# "The alarm has been snooped {amount_minutes} minutes"

class Alarm:
    def snooze(self,amount_minutes):
        print(f"The alarm has been snooped {amount_minutes} minutes")

monday=Alarm()
monday.snooze(14)
