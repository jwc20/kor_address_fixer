import pandas as pd
import re
import pprintpp as pp
import chardet

import datetime

date = datetime.datetime.now().strftime("%Y%m%d_%H%M")

remove_file = "remove_file.xlsx"
input_file_name = "categorized_addresses_20240419_1223.xlsx"

output_file_name = (
    "categorized_addresses_finished_{d}.xlsx".format(d=date)
)



sido_list = [
    "서울특별시",
    "부산광역시",
    "대구광역시",
    "인천광역시",
    "광주광역시",
    "대전광역시",
    "울산광역시",
    "세종특별자치시",
    "경기도",
    "강원특별자치도",
    "충청북도",
    "충청남도",
    "전북특별자치도",
    "전라남도",
    "경상북도",
    "경상남도",
    "제주특별자치도",
]


def main():
    address_data = pd.read_excel(input_file_name)
    # remove_data = pd.read_excel(remove_file)

    # unique_sido_df = pd.read_excel(remove_file)
    # unique_sigungu_df = pd.read_excel(remove_file)
    # unique_doromyong_df = pd.read_excel(remove_file)

    unique_sidos = pd.read_excel(remove_file)["unique_sido"].dropna().to_list()
    unique_sigungus = pd.read_excel(remove_file)["unique_sigungu"].dropna().to_list()
    unique_doromyongs = (
        pd.read_excel(remove_file)["unique_doromyong"].dropna().to_list()
    )

    # print(unique_sidos)
    # print(unique_sigungus)
    # print(unique_doromyongs)

    results = pd.DataFrame(columns=["sido", "sigungu", "doromyong", "detailed_address"])

    mapping_dict = {}

    for idx, row in address_data.iterrows():
        # sido	sigungu	doromyong	detailed_address
        # key = (row["sido"], row["sigungu"], row["doromyong"], row["detailed_address"])
        # mapping_dict[key] = (
        #     row["sido"],
        #     row["sigungu"],
        #     row["doromyong"],
        #     row["detailed_address"],
        # )

        # detailed_address_split = row['detailed_address'].split()
        found = False

        # print(str(row["detailed_address"][0]))
        # print(row["detailed_address"])
        # first_word = str(row["detailed_address"].split()[0].strip())

        # if first_word in unique_sidos:
        #     found = True
        #     row["detailed_address"].replace(first_word, "").strip()
        
        detailed_address = row["detailed_address"]

        sido_address = row["sido"].strip()
        sigungu_address = row["sigungu"].strip()
        doromyong_address = row["doromyong"].strip()



        for sido in unique_sidos:
            found = True
            if sido.strip() in detailed_address:
                # print(sido.strip())
                sido_address = sido.strip()
                detailed_address = detailed_address.replace(sido, "").strip()

        for sigungu in unique_sigungus:
            found = True
            # print(detailed_address)
            if sigungu.strip() in detailed_address:
                sigungu_address = sigungu.strip()
                detailed_address = detailed_address.replace(sigungu, "").strip()

        for doromyong in unique_doromyongs:
            found = True
            if doromyong.strip() in detailed_address:
                doromyong_address = doromyong.strip()
                detailed_address = detailed_address.replace(doromyong, "").strip()

        # print(detailed_address)

        results = results._append(
            {
                "sido": sido_address,
                "sigungu": sigungu_address,
                "doromyong": doromyong_address,
                "detailed_address": detailed_address.strip(),
            },
            ignore_index=True,
        )

    if not found:
        results = results._append(
            {
                "sido": None,
                "sigungu": None,
                "doromyong": None,
                "detailed_address": detailed_address.strip(),
            },
            ignore_index=True,
        )

    results.to_excel(output_file_name, index=False, engine="openpyxl")


if __name__ == "__main__":
    main()
    print("done")
    print("done")
    print("done")
    print("done")
    print("done")
