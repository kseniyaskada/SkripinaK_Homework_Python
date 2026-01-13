from address import Address
from mailing import Mailing

sender = Address("125435", "Moscow", "Taganskaya", "16", "432")
recipient = Address("029610", "Saint-Perersburg", "Volkovskaya", "11", "8923")

mailing = Mailing(
    to_address=recipient,
    from_address=sender,
    track="37UHJD78W3429",
    cost="490"
)

print("Отправление " + mailing.track + " из " + mailing.from_address.index +
      ", " + mailing.from_address.city + ", " + mailing.from_address.street
      + ", " + mailing.from_address.house + " - " +
      mailing.from_address.apartment + " в " + mailing.to_address.index +
      ", " + mailing.to_address.city + ", " + mailing.to_address.street +
      ", " + mailing.to_address.house + " - " + mailing.to_address.apartment
      + ". " + "Стоимость " + mailing.cost + " рублей.")
