import csv


class ResetData():
    def reset_static():
        with open("sp_model/keypoint.csv", "r") as source:
            reader = csv.reader(source)

            with open("sp_model/keypoint.csv", "w") as result:
                writer = csv.writer(result)
                for r in reader:
                    writer.writerow()
        print("Static Data Reset Success!")

    def reset_moving():
        with open("sp_model/point_history.csv", "r") as source:
            reader = csv.reader(source)

            with open("sp_model/point_history.csv", "w") as result:
                writer = csv.writer(result)
                for r in reader:
                    writer.writerow()
        print("Moving Data Reset Success!")

    def reset_setting():  # 結束重設鏡頭跟手
        with open("setting.csv", "r") as source:
            reader = csv.reader(source)

            with open("setting.csv", "w") as result:
                writer = csv.writer(result)
                for r in reader:
                    writer.writerow()


# ResetData.reset_static()
# ResetData.reset_moving()
