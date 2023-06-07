from wordcloud import WordCloud
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


if __name__ == "__main__":
    plt.rcParams["font.sans-serif"] = ["SimHei"]  #
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.unicode.ambiguous_as_wide", True)
    pd.set_option("display.unicode.east_asian_width", True)
    pd.set_option("display.width", 2000)
    # 数据读取
    m = pd.read_csv("movies.csv")
    m = m.dropna(subset=["DIRECTORS"])
    m = m.drop(
        ["SLUG", "ACTOR_IDS", "DIRECTOR_IDS", "OFFICIAL_SITE", "IMDB_ID"], axis=1
    )
    m = m[m["DOUBAN_SCORE"] > 0]

    # print(m)
    img = Image.open("static/picture/alice.jpeg")
    img_array = np.array(img)
    wc = WordCloud(
        background_color="white",
        font_path="Songti.ttc",
    )
    namelist = m["NAME"].tolist()
    # print(namelist)
    unique_string = (" ").join(namelist)
    print(unique_string)
