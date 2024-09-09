import pandas as pd
import os
from enum import Enum
from datetime import datetime
from configuration.configuration import get_root_dir
from services.formatter import format_timedelta


class Sheets(Enum):
    INCOMPLIANCE = 'Objects In Compliance'


def create_empty_file() -> str:
    # Get current datetime formatted
    now = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
    # Filename for your reports
    file_name = f'Rubrik_Compliance_{now}.xlsx'
    report_path = os.path.join(get_root_dir(), 'reports', file_name)

    return report_path


def generate_report(summary: dict, in_compliance: list[object]) -> str:
    REPORT_FILE = create_empty_file()

    writer = pd.ExcelWriter(REPORT_FILE, engine='openpyxl')

    # Involke all your functions that update your writer here
    writer = write_compliance_data(
        writer, in_compliance)

    writer.close()

    return REPORT_FILE


def write_compliance_data(writer: pd.ExcelWriter, db_list: list[object]) -> pd.ExcelWriter:
    writer.book.create_sheet(title=Sheets.INCOMPLIANCE.value)

    df_summary = pd.DataFrame([{
        # Write your column names and their values here. Exemple:
        # 'Cluster': db.cluster.name,
    } for db in db_list])
    df_summary.to_excel(writer, sheet_name=Sheets.INCOMPLIANCE.value, index=False)

    return writer