---
title: How do I upgrade or modify my ship?
---

{{version_check("3.23.0")}}

## Info

All vehicles have multiple components that you can exchange or upgrade, such as
weapons, shields, paints ("liveries"), quantum drives or power plants. Doing so
can improve the durability or performance of your ship; you can also remove
components to reduce the weight or power requirements.

You can acquire components by [buying them](./buying-components.md) at Platinum
Bay, Ship Weapons Shops or other stories, or by
[salvaging them](./salvage-components.md) from ships you find in the 'verse.

!!! warning "Compatible Components"

    Upgrades must match the size of the slot that you're installing them into -
    for example, an Aurora MR has a Size 1 Quantum Drive slot, and only Size 1
    drives will fit (such as the Atlas or VK-00). You can find out what slots
    are available on your ship, the components that will fit, and where to
    purchase them at [Erkul.games](https://erkul.games).

There are two ways to install new weapons & components on your ship, depending
on if they are [in your inventory](#using-your-mobiglass) or
[physicalised](#using-a-tractor-beam):

## Using your Mobiglass

!!! failure "Rented ships cannot be modified using the Mobiglass"

1. Make sure your ship is [stored](../ships/storing-ships.md) at your current
location, and the weapons/components to upgrade are in the local inventory (not
on the ship).

2. Open your Mobiglass (++f1++), and click the last icon to open the Vehicle
Loadout Manager.

    ![Vehicle Loadout Manager](
        ./images/swap-components-mobiglass-1.jpg){ width=600 }

3. Select the ship to modify from the dropdown in the top right.

    > ***Note:*** All ships that you own in-game are visible in the dropdown,
    but only ships that are stored in your current location will be selectable.

    ![Vehicle Loadout Manager](
        ./images/swap-components-mobiglass-2.jpg){ width=600 }

4. Click the component to modify; different component slots are listed on
different tabs, such a Systems or Weapons.

    ![Vehicle Loadout Manager](
        ./images/swap-components-mobiglass-3.jpg){ width=600 }

5. A list of compatible components are shown, with a number of available
components (unused, in inventory) and in-use (installed on this or other ships
stored at this location).

    ![Vehicle Loadout Manager](
        ./images/swap-components-mobiglass-4.jpg){ width=600 }

6. Click the component you want to install; it will be shown in the slot.

    ![Vehicle Loadout Manager](
        ./images/swap-components-mobiglass-5.jpg){ width=600 }

7. Click Save and Equip and your new component is installed.

    > ***Note:*** If you are changing multiple components, try not to change
    more than 3-5 components before saving, to avoid any modifications being
    missed.

??? tip "Insurance"

    Once you equip a new component in the Vehicle Loadout Manager, it becomes
    part of the insured setup for your ship. If you claim a replacement for your
    ship in future, it will include any components that you installed at no
    extra cost.

## Using a tractor beam

<!-- markdownlint-disable-next-line MD013 -->
!!! failure "Not all components can be modified with the tractor beam; e.g. Size 3 components are too large, and missile racks are fixed in place"

1. Move your ship and the physicalised component to a safe location where you
can use a [tractor tool](../fps/equipment/tractor-beam.md).

    > ***Note:*** You typically can't use tractor beams in an armistice area,
    but this restriction is lifted in hangars and on landing pads.

2. Sit in the pilot seat and Unlock Ports (++ralt+k++). If you are modifying a
vital component (e.g. a cooler or power plant) be sure to power off (++u++) your
ship to avoid damage.

3. Find the component slot on your ship, equip your tractor beam (++5++) and
switch it to Detaching/Detachment (++b++).

4. If there is already a component in the slot, detach it with the tractor beam:
    - Point the tool at the component & enable the beam (++"LMB"++).
    - Pull the component in the direction indicated by the arrow until it comes
    loose.

5. Pick up the new component with the tractor beam and move it close to the
slot; a silhouette of the component will appear.
    - If the silhouette is green, the component is correctly aligned; release
    the tractor beam and it will slot into place.
    - If the silhouette is yellow, the component is not lined up with the slot;
    rotate it (hold ++r++ and move the mouse) until the silhouette turns green.
    - If the silhouette is red, the component is not compatible with this slot -
    most likely it is the wrong size.

6. Sit in the pilot seat and Lock Ports (++ralt+k++)

7. The component is now installed.

<!-- markdownlint-disable-next-line MD013 -->
!!! info "You may need to cycle power (++u++ x2) on your ship to enable new components"

??? tip "Insurance"

    Components installed with a tractor beam are not insured until you next
    [store your ship](../ships/storing-ships.md). Once insured, if you claim a
    replacement for your ship in future, it will include any components that you
    installed at no extra cost.
