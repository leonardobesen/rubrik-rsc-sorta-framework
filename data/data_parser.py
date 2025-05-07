import logging
from connection.wrapper import request
from model.cluster import Cluster
import graphql.queries
from data import data_operation

logger = logging.getLogger(__name__)


# Example Function
def get_all_cluster_info(access_token: str) -> list[Cluster]:
    """Fetch all clusters information"""
    clusters = []

    try:
        query, variables = graphql.queries.all_cluster_info_query()
        response = request(access_token, query, variables)
        nodes = response.get("data", {}).get(
            "allClusterConnection", {}).get("nodes", [])
    except Exception as e:
        logger.exception("Failed to fetch cluster data")
        raise LookupError("Unable to collect clusters data!") from e

    if not nodes:
        return []

    for item in nodes:
        cluster = data_operation.create_cluster_from_data(item)
        if cluster:
            clusters.append(cluster)

    return clusters
