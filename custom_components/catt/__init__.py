from http import HTTPStatus
import requests
import logging
import asyncio
import aiohttp
import async_timeout

import json
import base64
import subprocess

from typing import Any

import voluptuous as vol

import homeassistant.loader as loader
from homeassistant.const import (STATE_UNKNOWN, EVENT_STATE_CHANGED)
import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from homeassistant.helpers import discovery

from homeassistant.core import (
    HomeAssistant,
    ServiceResponse,
    ServiceCall,
    SupportsResponse,
)

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


CONFIG_SCHEMA = vol.Schema({DOMAIN: {}}, extra=vol.ALLOW_EXTRA)

CMD_BASE = ["catt", "-d"]
VALIDATE_ARGS = ["info", "-j"]
STOP_ARGS = ["stop"]
SCAN_CMD = ["catt", "scan"]
HELP_CMD = ["catt", "-h"]

def subp_run(cmd, allow_failure: bool = False) -> subprocess.CompletedProcess:
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if not allow_failure and output.returncode != 0:
        #raise CattTestError('The command "{}" failed.'.format(" ".join(cmd)))
        _LOGGER.error(f'[{DOMAIN}] The command "{cmd}" failed.')
    return output


async def async_setup(hass, config):

    if DOMAIN not in config:
        return True

    return True


async def async_setup_entry(hass, config_entry):
    """Set up this integration using UI."""

    if hass.data.get(DOMAIN) is not None:
        return False

    if config_entry.source == config_entries.SOURCE_IMPORT:
        hass.async_create_task(hass.config_entries.async_remove(config_entry.entry_id))
        return False

    session = async_get_clientsession(hass)

    # scan add service
    async def scan(service):
        output = subp_run( SCAN_CMD ).stdout
        _LOGGER.error(f'[{DOMAIN}] scan service call -> {output}')

        return { "output" : output}

    hass.services.async_register(DOMAIN, "scan", scan, supports_response=SupportsResponse.ONLY,)

    # help add service
    async def help(service):
        output = subp_run( HELP_CMD ).stdout
        _LOGGER.error(f'[{DOMAIN}] help service call -> {output}')

        return { "help" : output }

    hass.services.async_register(DOMAIN, "help", help, supports_response=SupportsResponse.ONLY,)


    async def stop(service):
        dname = service.data["friendly_name"]

        _LOGGER.error(f'[{DOMAIN}] stop service call -> {dname}')

        _LOGGER.info(subp_run(CMD_BASE + [dname] + STOP_ARGS).stdout)

    hass.services.async_register(DOMAIN, "stop", stop)


    async def command(service):
        dname = service.data["friendly_name"]
        cmd   = service.data["command"]
        param = service.data["param"]

        _LOGGER.error(f'[{DOMAIN}] command service call -> {dname}, {cmd}, {param}')

        _LOGGER.info(subp_run(CMD_BASE + [dname] + [cmd] + [param]).stdout)

    hass.services.async_register(DOMAIN, "command", command)

    return True

