from typing import Optional


# Example Function
def create_cluster_from_data(data) -> Optional[object]:
    try:
        return Cluster(
            id=data["id"],
            name=data["name"],
            connected_state=data["state"]["connectedState"]
        )
    except Exception as e:
        print("Error processing cluster item: ", e)
        return None