"""User-Agent detection for Paprika Recipe Manager."""

import logging
import platform
import plistlib
from pathlib import Path

logger = logging.getLogger(__name__)


def detect_user_agent() -> str | None:
    """Detect User-Agent from installed Paprika Recipe Manager application.

    Currently supports macOS only. Returns None on other platforms or if
    detection fails.

    Returns:
        User-Agent string, or None if app not found or detection fails.
    """
    if platform.system() != "Darwin":
        return None

    app_path = Path("/Applications/Paprika Recipe Manager 3.app")
    if not app_path.exists():
        return None

    try:
        # Read Info.plist
        plist_path = app_path / "Contents" / "Info.plist"
        if not plist_path.exists():
            return None

        with open(plist_path, "rb") as f:
            plist = plistlib.load(f)

        # Extract version info
        bundle_version = plist.get("CFBundleShortVersionString")
        build_number = plist.get("CFBundleVersion")
        bundle_id = plist.get("CFBundleIdentifier")

        if not all([bundle_version, build_number, bundle_id]):
            logger.warning(
                "Could not extract all required version info from Paprika app"
            )
            return None

        # Get macOS version
        macos_version = platform.mac_ver()[0]

        return (
            f"Paprika Recipe Manager 3/{bundle_version} "
            + f"({bundle_id}; build:{build_number}; macOS {macos_version})"
        )

    except Exception as e:
        logger.warning(f"Error detecting Paprika app User-Agent: {e}")
        return None
