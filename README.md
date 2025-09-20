The Campaign for North Africa: The Desert War 1940-1943
=

# Overview

* Implement most of the mechanics of playing the game in software,
  enabling human players to play without the administrivia
* Support multiple players on a "team", playing distinct roles
* Support both "teams" in a game
* Potentially support an external game board: either cardboard or
  table top simulator
  * Given the number of counters involved in the game, this might not
    make sense?
* Implement as a Python server, with a FastAPI interface, and
  JavaScript front-end
  * Maybe ReactPy?
* Counters have associated info
  * §2.2 

## Units

* From §3.21:
  * Infantry type
  * Tank type
  * Recce type
  * Artillery type
  * Anti-tank type
  * Anti-aircraft type
  * Headquarters
  * Engineers
  * Tank recovery squadrons
  * Squadron ground support units
  * Dummy tank formations
  * Trucks
  * All these types have a matching counter (see the manifest in §4.22
    except Dummy Tanks which don't have a counter (why?)
* From §3.22:
  * for Barrage and Aircraft (Strafing and Bombardment) attacks, the
    following classes are used:
    * _Infantry_ class
      * Infantry type
      * Engineers
      * Headquarters (_with_ defensive Close Assault Rating but _without_ an Armour Protection Rating)
      * Recce Type _without_ an armour protection rating
    * _Armour_ class
      * Tank type
      * Dummy Tank Formations
      * Tank recovery squadrons
      * Headquarters _with_ an Armour Protection Rating
      * Recce type _with_ an Armour Protection Rating
      * Artillery and Anti-tank units _with_ an Armour Protection Rating (SPA and Tank Destroyers)
    * _Gun_ class
      * Artillery, Anti-aircraft, and Anti-tank units of any TOE Strength Points but _without_ an Armour Protection Rating
        * Including Headquarters and infantry with Barrage capability
    * _Truck_ class
      * All trucks
  * *Note*: artillery or anti-tank units that have weapons (TOE strength
    points) with an armour protection rating and weapons without an
    armour protection rating are considered two units for target
    purposes.
  
### Headquarters Units (§3.3)

* Headquarters Units have two purposes:
  * Command coordination for all the units under them, and
  * They represent all the units attached to them on the game map
* §3.31: a Headquarters Unit fights with the combined strength of all its attached combat units
* §3.32: a Headquarters Unit has the Capability Point Allowance of the _slowest_ of its attached units
* §3.33: a Headquarters Unit representing a full division has 5
  stacking points.  If it has no attached units it has zero stacking
  points.
  * Stacking points limit the number of units that can occupy a map hex.
  * See also §9.2
* §3.34: some Headquarters Units have artillery assigned.  They may
  use their combat strengths, and losses are taken as normal losses,
  but when all the gun TOE Strength Points are eliminated, the HQ
  reverts to a non-combat HQ rather than being destroyed.
* TOE stands for "Table of Organization and Equipment", which details
  the structure and equipment of military units. It provides specific
  information about the composition and organization of forces

### Combat Units (§3.4)
### Unit Characteristics (§3.5)


# Game Loop and Interaction

* For each turn, stage, phase, and segment, each player should be prompted to create Actions.
* Allowed or possible Actions will depend upon the moment in the game
* Where multiple Actions are allowed, the player must submit a final "done" Action
* It should be possible to filter both the prompts and allowed Actions according to a player's role
  * But that could come as a second phase of development: it's not necessary.
* The prompts should describe the moment, and indicate the class(es) of possible actions
* Events should also be notified: arriving convoys, combat results, etc.
  * This could be interspersed with the prompts?
  * Or, using a TUI, in a separate window?
* Practically, I think perhaps a web-based game client
  * Connecting to a game server
    * FastAPI?
    * Starlette?
    * WebSockets?
  * The UI should probably show
    * The map
    * Game time, both turn/stage/phase/segment and historical date
    * Prompts and events
    * A way to submit actions
  

