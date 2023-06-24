from beerlog.core import get_beers_from_database, add_beer_to_database


def test_add_beer_to_database():
    assert add_beer_to_database("Blue Moon", "Witibier", 10, 3, 6)


def test_get_beers_from_database():
    """Method of unit test: AAA"""

    # Arrange
    add_beer_to_database("Blue Moon", "Witibier", 10, 3, 6)

    # Act
    results = get_beers_from_database()

    # Assert
    assert len(results) > 0
