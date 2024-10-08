import data.data_parser as data_parser
from model.cluster import Cluster


# Example Function
def run_query_on_all_clusters(access_token: str) -> list[Cluster]:
    results = []
    clusters = data_parser.get_all_cluster_info(access_token)

    for cluster in clusters:
        # object = data_parser.your_query()
        results.append(object)

    return results
