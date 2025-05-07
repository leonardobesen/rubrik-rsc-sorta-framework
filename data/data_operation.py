import logging
from model.cluster import Cluster

logger = logging.getLogger(__name__)


def create_cluster_from_data(data: dict) -> Cluster | None:
    """Create a Cluster object from a dictionary of data."""
    try:
        return Cluster(
            id=data["id"],
            name=data["name"],
            connected_state=data.get("state", {}).get("connectedState"),
        )
    except KeyError as e:
        logger.error(
            f"Missing expected cluster data field: {e}", exc_info=True)
    except Exception as e:
        logger.exception(
            "Unexpected error while creating Cluster object", exc_info=True)
    return None
