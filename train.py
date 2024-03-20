import random

class Train:
    def __init__(self, train_no, source, destination, total_seats):
        self.train_no = train_no
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats

class ReservationSystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def check_train_availability(self, source, destination):
        available_trains = []
        for train in self.trains:
            if train.source == source and train.destination == destination:
                available_trains.append(train)
        return available_trains

    def check_seat_availability(self, train):
        return train.available_seats

    def book_ticket(self, train):
        if train.available_seats > 0:
            pnr = random.randint(1000, 9999)
            train.available_seats -= 1
            return pnr
        else:
            return None


def main():
    system = ReservationSystem()

    # Create some train objects and add them to the system
    train1 = Train("12345", "A", "B", 100)
    train2 = Train("67890", "B", "C", 50)
    system.add_train(train1)
    system.add_train(train2)

    while True:
        print("\n===== Railway Reservation Management System =====")
        print("1. Check Train Availability")
        print("2. Check Seat Availability")
        print("3. Book Ticket")
        print("4. Exit")
        print(" Train Availability: Train-1: No:- 12345 ", "Source Station:- A ",  "Destination Station:- B")
        print("                     Train-2: No:- 67890 ", "Source Station:- B ",  "Destination Station:- C")

        choice = input("Enter your choice: ")

        if choice == "1":
            source = input("Enter source station: ")
            destination = input("Enter destination station: ")
            available_trains = system.check_train_availability(source, destination)
            if available_trains:
                print("Available Trains:")
                for train in available_trains:
                    print(f"Train No: {train.train_no}, Source: {train.source}, Destination: {train.destination}")
            else:
                print("No trains available for the given source and destination.")

        elif choice == "2":
            train_no = input("Enter train number: ")
            train = None
            for t in system.trains:
                if t.train_no == train_no:
                    train = t
                    break
            if train:
                available_seats = system.check_seat_availability(train)
                print(f"Available seats in Train No {train.train_no}: {available_seats}")
            else:
                print("Invalid train number.")

        elif choice == "3":
            train_no = input("Enter train number: ")
            train = None
            for t in system.trains:
                if t.train_no == train_no:
                    train = t
                    break
            if train:
                pnr = system.book_ticket(train)
                if pnr:
                    print(f"Ticket booked successfully! Your PNR: {pnr}")
                else:
                    print("Sorry, no seats available.")
            else:
                print("Invalid train number.")

        elif choice == "4":
            print("Thank you for using the Railway Reservation Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()