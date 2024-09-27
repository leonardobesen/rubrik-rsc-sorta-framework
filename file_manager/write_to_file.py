import pandas as pd
import os
from enum import Enum
from datetime import datetime
from configuration.configuration import get_root_dir
from services.formatter import format_timedelta
from model.cluster import Cluster


class Sheets(Enum):
    CLUSTERS = 'Clusters'


def _create_empty_file(report_name: str) -> str:
    # Get current datetime formatted
    now = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
    # Filename for your reports
    file_name = f'{report_name}_{now}.xlsx'
    report_path = os.path.join(get_root_dir(), 'reports', file_name)

    return report_path


def generate_report(report_name: str, clusters: list[Cluster]) -> str:
    REPORT_FILE = _create_empty_file(report_name)

    writer = pd.ExcelWriter(REPORT_FILE, engine='openpyxl')

    # Involke all your functions that update your writer here
    writer = write_cluster_data(writer, clusters)

    writer.close()

    return REPORT_FILE


def write_cluster_data(writer: pd.ExcelWriter, clusters: list[Cluster]) -> pd.ExcelWriter:
    writer.book.create_sheet(title=Sheets.CLUSTERS.value)

    df = pd.DataFrame([{
        # Write your column names and their values here. Exemple:
        'Cluster': cluster.name,
    } for cluster in clusters])
    df.to_excel(writer, sheet_name=Sheets.CLUSTERS.value, index=False)

    return writer
