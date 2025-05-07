import connection.connect as connect
import file_manager.write_to_file as write_to_file
import file_manager.upload_to_google_drive as uploader
import configuration.configuration as config
from controller import controller
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # Establish connection with Rubrik RSC
    rsc_access_token = connect.open_session()

    print("Collecting Data...")
    cluster_info = controller.get_all_cluster_info(
        access_token=rsc_access_token)

    print("Writing to file...")
    file_path = write_to_file.generate_report(
        cluster_info=cluster_info
    )

    print(f"Saved to file {file_path}")

    folder_id = config.get_drive_folder_id()
    if folder_id is not None:
        uploader.upload_excel_to_drive(file_path, folder_id)

    # Close session
    connect.close_session(rsc_access_token)
