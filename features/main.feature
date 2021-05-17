Feature: Wikipedia music search
  As a Music lover
  I want to search for the song
  And to get key information about it

  Scenario Outline: Search for <name> song
    Given I open Google
    And I want to get info about a <name> song
      When I open Wikipedia
      Then Song producer is <group>
      And Release year is <release_year>

  Examples: Songs
    | name           | group        | release_year   |
    | Billie Jean | Michael Jackson | 1982           |
    |Through the Fire and Flames| DragonForce | 2005 |