# Concerts Application

## Setup

1. Install dependencies:

    ```bash
    pip install sqlalchemy alembic
    ```

2. Initialize the database:

    ```bash
    alembic upgrade head
    ```

## Usage

### Models

- `Band`: Represents a musical band.
- `Venue`: Represents a concert venue.
- `Concert`: Represents a concert event, linking a band and a venue.

### Methods

- `Band.play_in_venue(venue, date)`: Creates a concert for the band.
- `Band.all_introductions()`: Returns all introductions for the band.
- `Band.most_performances()`: Returns the band with the most performances.
- `Venue.concert_on(date)`: Finds the first concert on a specific date.
- `Venue.most_frequent_band()`: Returns the band with the most concerts at the venue.

### Testing

Run the tests defined in `test_methods()` to validate the functionality.
