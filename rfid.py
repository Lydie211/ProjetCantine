"""import RPi.GPIO as GPIO"""

from mfrc522 import MFRC522
class RFID:
    reader = MFRC522()

    def __init__(self):
        print("Activation du lecteur RFID")


    def lireRfid(self):
        """Méthode qui permet de faire la lecture du badge
        Elle retourne l'id du badge"""
        try:
            print("Place your RFID tag or card near the reader...")
            id, text = self.reader.read()
            print(f"RFID Tag ID: {id}")

        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            GPIO.cleanup()
        badge_id = id
        return badge_id