"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight

lamps_entity = "light.guest_room_lamps_group"
switch_name = "Guest Room Switch"


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = GuestRoomLight()
    add_entities([ent])


class GuestRoomLight(NewLight):
    """Guest Room Light."""

    def __init__(self) -> None:
        """Initialize Guest Room Light."""
        super(GuestRoomLight, self).__init__(
            "Guest Room Light", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities[lamps_entity] = None
        self.switch = switch_name
