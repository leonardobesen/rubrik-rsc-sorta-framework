from connection.wrapper import request
from graphql import queries
import data.data_operation as data


# Example Function
def _get_all_cluster_info(access_token: str) -> list[object]:
    clusters_information = []

    # Gather clusters information
    query, variables = queries.all_cluster_info_query()

    try:
        response = request(access_token, query, variables)
    except Exception:
        raise LookupError("Unable to collect clusters data!")

    if not response["data"]:
        return []

    # Process cluster information
    for item in response["data"]["allClusterConnection"]["nodes"]:
        cluster = data.create_cluster_from_data(item)
        if cluster:
            clusters_information.append(cluster)

    return clusters_information
