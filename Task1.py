import os
import shutil
import logging
from datetime import datetime


# Creating log file
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def create_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            logging.info(f"{folder_name} folder created")
            
    except Exception as error:
        logging.error(f"Folder creation error: {error}")



def organize_files(path):

    try:

        if not os.path.exists(path):
            print("Folder does not exist")
            return


        file_list = os.listdir(path)


        for file in file_list:

            old_path = os.path.join(path, file)


            # ignore folders
            if os.path.isdir(old_path):
                continue


            extension = file.split(".")[-1].lower()


            if extension in ["jpg", "png", "jpeg"]:
                folder = "Images"


            elif extension in ["pdf", "docx", "txt"]:
                folder = "Documents"


            elif extension in ["mp3", "wav"]:
                folder = "Music"


            elif extension in ["mp4", "mkv"]:
                folder = "Videos"


            else:
                folder = "Others"



            new_folder = os.path.join(path, folder)

            create_folder(new_folder)



            new_path = os.path.join(new_folder, file)



            shutil.move(old_path, new_path)



            print(file, "moved to", folder)

            logging.info(
                f"{file} moved to {folder}"
            )



        print("\nFile organization completed successfully")


    except Exception as error:

        print("Something went wrong")

        logging.error(
            f"Sorting error: {error}"
        )




def rename_files(path):

    try:

        files = os.listdir(path)

        count = 1


        for file in files:


            old_name = os.path.join(path,file)


            if os.path.isfile(old_name):

                extension = file.split(".")[-1]


                new_name = os.path.join(
                    path,
                    f"File_{count}.{extension}"
                )


                os.rename(
                    old_name,
                    new_name
                )


                print(
                    file,
                    "renamed to",
                    f"File_{count}.{extension}"
                )


                logging.info(
                    f"{file} renamed"
                )


                count += 1



    except Exception as error:

        logging.error(
            f"Rename error: {error}"
        )





def main():

    print("------------------------------")
    print(" File Automation System ")
    print("------------------------------")


    folder_path = input(
        "Enter folder path: "
    )


    print("\nChoose Operation")
    print("1. Sort Files")
    print("2. Rename Files")


    choice = input(
        "Enter choice: "
    )


    if choice == "1":

        organize_files(folder_path)



    elif choice == "2":

        rename_files(folder_path)



    else:

        print("Invalid choice")



if __name__ == "__main__":

    main()