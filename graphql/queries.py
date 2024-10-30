from configuration.configuration import get_excluded_clusters_uuids

def all_cluster_info_query() -> tuple[str, dict]:
    variables = {
        "filter": {
            "productFilters": [
              {
                "productType": "CDM"
              }
            ],
            "excludeId": get_excluded_clusters_uuids()
        }
    }

    query = f"""query ListAllClustersInfo($filter: ClusterFilterInput,$sortBy: ClusterSortByEnum = ClusterName){{
      allClusterConnection(filter: $filter, sortBy: $sortBy){{
        nodes{{
          id
          name
          systemStatus
          pauseStatus
          status
          state{{
            connectedState
          }}
          passesConnectivityCheck
          lastConnectionTime
          metric{{
            totalCapacity
            usedCapacity
            snapshotCapacity
            systemCapacity: miscellaneousCapacity
            availableCapacity
            lastUpdateTime
          }}
          estimatedRunway
        }}
      }}
    }}"""

    return query, variables
