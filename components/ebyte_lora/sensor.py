import esphome.codegen as cg
from esphome.components.sensor import new_sensor, sensor_schema
from esphome.config_validation import All, has_at_least_one_key
from esphome.const import CONF_ID

from ... import (
    CONF_NETWORK_ID,
    CONF_REMOTE_ID,
    CONF_EBYTE_LORA_COMPONENT_ID,
    SENSOR_SCHEMA,
    require_internal_with_name,
)

DEPENDENCIES = ["ebyte_lora"]

CONFIG_SCHEMA = All(
    sensor_schema().extend(SENSOR_SCHEMA),
    has_at_least_one_key(CONF_ID, CONF_REMOTE_ID),
    require_internal_with_name,
)


async def to_code(config):
    var = await new_sensor(config)
    comp = await cg.get_variable(config[CONF_EBYTE_LORA_COMPONENT_ID])
    remote_id = str(config.get(CONF_REMOTE_ID) or config.get(CONF_ID))
    cg.add(comp.add_remote_sensor(config[CONF_NETWORK_ID], remote_id, var))