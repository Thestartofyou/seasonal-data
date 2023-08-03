def get_seasonal_produce(plu_number):
    seasonal_data = {
        '4011': ['Spring', 'Summer', 'Fall'],
        '4225': ['Spring', 'Summer'],
        '3035': ['Fall', 'Winter'],
        '84011': ['Year-round'],
        '93000': ['Year-round'],
        # Add more PLU data here as needed
    }

    if plu_number in seasonal_data:
        return seasonal_data[plu_number]
    else:
        return []

if __name__ == "__main__":
    # Assuming the user enters the PLU number
    plu_number = input("Enter the PLU number of the fruit or vegetable: ")
    seasonal_availability = get_seasonal_produce(plu_number)

    if not seasonal_availability:
        print("Seasonal availability for this PLU number is not available.")
    else:
        seasons = ', '.join(seasonal_availability)
        print(f"PLU {plu_number} is available in the following seasons: {seasons}.")

def get_seasonal_produce(plu_number):
    seasonal_data = {
        '4011': ['Spring', 'Summer', 'Fall'],
        '4225': ['Spring', 'Summer'],
        '3035': ['Fall', 'Winter'],
        '84011': ['Year-round'],
        '93000': ['Year-round'],
        # Add more PLU data here as needed
    }

    if plu_number in seasonal_data:
        return seasonal_data[plu_number]
    else:
        return []

if __name__ == "__main__":
    # Assuming the user enters the PLU number
    plu_number = input("Enter the PLU number of the fruit or vegetable: ")
    seasonal_availability = get_seasonal_produce(plu_number)

    if not seasonal_availability:
        print("Seasonal availability for this PLU number is not available.")
    else:
        seasons = ', '.join(seasonal_availability)
        print(f"PLU {plu_number} is available in the following seasons: {seasons}.")
