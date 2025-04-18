---
title: How do I request landing clearance from ATC?
---

{{version_check("4.1")}}

## Info

To keep traffic flowing through spaceports and stations around the 'verse,
every location where you can store and retrieve your vehicles has an Air
Traffic Control (ATC) that gives landing or take-off permissions to all
pilots.

If you try to land in a hangar that is controlled by ATC without permission,
your ship can be temporarily impounded to keep doors and flight-paths clear for
other players.

Contacting ATC when you are close to your destination will assign you a
dedicated hangar where you can land, [repair & refuel](./refuel-repair.md), and
give you a HUD  marker to guide you in if you're unfamiliar with the location.

## Calling ATC

1. Approach to within ATC range of your destination. You will know that you are
close enough when a "Contact ATC" warning shows on your HUD, and the name of
the local ATC (e.g. "NBIS Spaceport") shows on your Comms MFD.

    - [How do I find the spaceport at each city?](../navigation/find-spaceport.md)

    > ***Note:*** It is recommmended to move within 5km of your destination
    before calling ATC as the marker for your hangar may not appear until you
    are that close.

1. Contact ATC

    === "Using Keybind"

        - Press the "Request ATC" keybind (`L Alt + N`).

    === "*Alternate*: Using HUD"

        - Locate your Comms MFD. If no MFD is set to Comms,
        [select it from the Menu](./configure-mfds.md).
        - Find the ATC channel for your destination - it is usually named after
        the spaceport or station, and is typically near the top of the list.

            > ***Note:*** Some spaceports, such as at jump points and above
            cities, have an extra Cargo channel; don't use this one.
        
        - Click the Open Channel icon on the right-hand side.

    === "*Alternate*: Using MobiGlass"

        - Open your Communications app (`F11`)
        - Click Friends.
        - Find the ATC channel for your destination - it is usually named after
        the spaceport or station, and is typically near the top of the list.

            > ***Note:*** Some spaceports, such as at jump points and above
            cities, have an extra Cargo channel; don't use this one.

        - Click the Open Channel icon on the right-hand side.

1. ATC will respond with confirmation when you are assigned a hangar; you may
receive a negative response if no hangars are available, or a short chirp if
ATC is overloaded.

1. If there are a large number of players landing or taking off, you may be
added to a queue; the notification will show the number of players in the queue,
along with a max wait time.

    ![Notification](./images/landing-atc/notification.jpg)

1. An icon will appear on your HUD showing the location of your hangar. It will
be marked with the name of your hangar, e.g. 'WhiskoTangey's Small Hangar'

    ![Marker](./images/landing-atc/marker.jpg)

1. Fly to the marker and land your ship. You will only have 100 seconds before
landing permission is revoked, so don't hang around!
