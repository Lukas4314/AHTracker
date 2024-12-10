import getNewData, addingToDataBase,lowestAvergeBinFileMaker, medianBinFileMaker, flipFinder2, flipFilter, notificationScript
import time


def main():
    while True:
        getNewData.update_raw_data()
        flipFinder2.main()
        
        #addingToDataBase.main()
        #medianBinFileMaker.main()
        #lowestAvergeBinFileMaker.main()
        
        
        flipFilter.filtrer_flips(100, 30*1000*1000, 300*1000)
        notificationScript.check_and_update_json("qualified_flips.json", "1flips.json")
        
        print("Just updated")
        time.sleep(10)


if __name__ == "__main__":
    main()