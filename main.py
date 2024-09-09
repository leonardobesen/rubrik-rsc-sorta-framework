import connection.connect as connect
import file_manager.write_to_file as write_to_excel
import file_manager.upload_to_google_drive as uploader
import configuration.configuration as config
from controller import controller


if __name__ == '__main__':
    # Establish connection with Rubrik RSC
    rsc_access_token = connect.open_session()

    print("Step 1. Collect and Process Data:")
    # compliance = controller.get_compliance(access_token=rsc_access_token)

    print("Step 2. Write to file:")
    # file_path = write_to_excel.generate_report(
    #     compliance=compliance
    # )

    print(f"Saved to file")

    # folder_id = config.get_drive_folder_id()
    # if folder_id is not None:
    #     uploader.upload_excel_to_drive(file_path, folder_id)

    # Close session
    connect.close_session(rsc_access_token)
