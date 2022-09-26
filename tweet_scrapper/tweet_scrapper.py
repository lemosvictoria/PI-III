from datetime import datetime, timedelta
from sys import argv

import pandas as pd
import twint


ID_SEARCH_TERMS = {
    "bolsonaro": 1,
    "ciro": 2,
    "lula": 3
}


if __name__ == "__main__":
    print(f'START - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

    search_term = argv[1]
    time_before = argv[2]
    saving_path = argv[3][0:-1] if argv[3][-1] == "/" else argv[3]
    date = datetime.now().strftime('%Y-%m-%dT%H-%M')
    file_absolute_name = f"{saving_path}/tweets_{search_term}_{date}.csv"

    if search_term in ID_SEARCH_TERMS:
        c = twint.Config()
        c.Search = search_term
        c.Since = (datetime.now() - timedelta(hours=int(time_before), minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
        c.Store_csv = True
        c.Output = file_absolute_name
        c.Hide_output = True

        try:
            twint.run.Search(c)
        except Exception as err:
            print(err)

        scrapped_data = pd.read_csv(file_absolute_name)
        scrapped_data["search_id"] = ID_SEARCH_TERMS[search_term]
        scrapped_data["search_term"] = search_term
        scrapped_data.to_csv(file_absolute_name, index=False)
    else:
        print("SEARCH TERM NOT ALLOWED!")

    print(f'END - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
