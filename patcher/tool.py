"""
File        : tool.py
Author      : Silous
Created on  : 2025-10-08
Description : call tool to repack the game.
"""

# == Imports ==================================================================


from logging import Logger
from pathlib import Path

# -------------------- Import Lib User -------------------
from patcher import config
from patcher.utils import xdelta
from patcher.utils.logger import get_logger

# == Global Variables =========================================================

_logger: Logger = get_logger(__name__)


# == Functions ================================================================


def repack() -> None:
    """whole patching process."""
    xdelta.apply_xdelta_patch(
        target_file=str(Path(config.GAME_FOLDER) / "00000000.cfsi"),
        patch_file=str(config.PATCH_FOLDER / "00000000.cfsi.xdelta"),
    )
