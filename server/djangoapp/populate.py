from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
            "country": "Japan",
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
            "country": "Germany",
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
            "country": "Germany",
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
            "country": "South Korea",
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
            "country": "Japan",
        },
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data["name"],
                description=data["description"],
                country=data["country"],
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "fuel_type": "PETROL",
            "transmission_type": "AUTO",
            "dealer_id": 1001,
            "car_make": car_make_instances[0],
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 1002,
            "car_make": car_make_instances[0],
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 1003,
            "car_make": car_make_instances[0],
        },
        {
            "name": "A Class",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "PETROL",
            "transmission_type": "AUTO",
            "dealer_id": 2001,
            "car_make": car_make_instances[1],
        },
        {
            "name": "C Class",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 2002,
            "car_make": car_make_instances[1],
        },
        {
            "name": "E Class",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 2003,
            "car_make": car_make_instances[1],
        },
        {
            "name": "A4",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 3001,
            "car_make": car_make_instances[2],
        },
        {
            "name": "A5",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "PETROL",
            "transmission_type": "AUTO",
            "dealer_id": 3002,
            "car_make": car_make_instances[2],
        },
        {
            "name": "A6",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 3003,
            "car_make": car_make_instances[2],
        },
        {
            "name": "Sorrento",
            "type": "SUV",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 4001,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Carnival",
            "type": "WAGON",
            "year": 2023,
            "fuel_type": "PETROL",
            "transmission_type": "AUTO",
            "dealer_id": 4002,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Cerato",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "PETROL",
            "transmission_type": "MANUAL",
            "dealer_id": 4003,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Corolla",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 5001,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Camry",
            "type": "SEDAN",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 5002,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Kluger",
            "type": "SUV",
            "year": 2023,
            "fuel_type": "HYBRID",
            "transmission_type": "AUTO",
            "dealer_id": 5003,
            "car_make": car_make_instances[4],
        },
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_make=data["car_make"],
            type=data["type"],
            year=data["year"],
            fuel_type=data["fuel_type"],
            transmission_type=data["transmission_type"],
            dealer_id=data["dealer_id"],
        )
