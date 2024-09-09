def all_cluster_info_query() -> tuple[str, dict]:
    variables = {
        "filter": {
            "productFilters": [
                {
                    "productType": "CDM"
                }
            ]
        }
    }

    query = f"""query ListAllClustersInfo($filter: ClusterFilterInput,$sortBy: ClusterSortByEnum = ClusterName){{
      allClusterConnection(filter: $filter, sortBy: $sortBy){{
        nodes{{
          id
          name
          state{{
            connectedState
          }}
        }}
      }}
    }}"""

    return query, variables
