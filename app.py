from bokeh.embed import components
from flask import Flask
from flask import render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
import matplotlib as mpl


app = Flask(__name__)


pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 2000)
# 数据读取
m = pd.read_csv("movies.csv")
m = m.dropna(subset=["DIRECTORS"])
m = m.drop(["SLUG", "ACTOR_IDS", "DIRECTOR_IDS", "OFFICIAL_SITE", "IMDB_ID"], axis=1)
m = m[m["DOUBAN_SCORE"] > 0]
score = m["DOUBAN_SCORE"]


def dic1(data, typei):
    dic_type_lp = {}
    datai = data[data["GENRES"].str.contains(typei)]
    lp_pre_i = len(datai[datai["DOUBAN_SCORE"] < 6.1]) / len(datai)
    dic_type_lp["typename"] = typei
    dic_type_lp["typecount"] = len(datai)
    dic_type_lp["type_lp_pre"] = lp_pre_i
    return dic_type_lp


def my_type():
    my_type = m[m["GENRES"].notnull()]
    return my_type


@app.route("/")
def index():  # put application's code here
    return render_template("index1.html")


@app.route("/scoreBar")
def scoreBar():  # put application's code here
    # pandas 配置文件参数更改
    Barlist = score.values.tolist()
    Barlist.sort()
    # print(Barlist)
    result = pd.value_counts(Barlist)
    result = result.sort_index()

    # 画柱形图
    plt.figure(figsize=(24, 8))
    plt.rcParams["font.sans-serif"] = ["Songti SC"]
    plt.title("电影豆瓣评分分布柱形图", fontsize=30)
    plt.xlabel("电影豆瓣评分", fontsize=30)
    plt.ylabel("频数", fontsize=30)
    plt.xticks(fontsize=10)
    result.plot.bar()
    plt.savefig("static/picture/scoreBar.png")

    #
    plt.figure(figsize=(24, 8))
    plt.rcParams["font.sans-serif"] = ["Songti SC"]
    plt.title("电影豆瓣评分分布折线图", fontsize=30)
    plt.xlabel("电影豆瓣评分", fontsize=30)
    plt.ylabel("频数", fontsize=30)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=15)
    result.plot()
    plt.savefig("static/picture/scorePlot.png")

    return render_template("scoreBar.html")


@app.route("/scoreBokeh")
def scoreBokeh():
    typist = []
    for i in m[m["GENRES"].notnull()]["GENRES"].str.replace(" ", "").str.split("/"):
        typist.extend(i)
    typist = list(set(typist))
    typist.sort()

    lst_type_lp = []
    for i in typist:
        dici = dic1(my_type(), i)
        # print(dici)
        lst_type_lp.append(dici)
    m_type_lp = pd.DataFrame(lst_type_lp)

    type_lp_top20 = m_type_lp.sort_values(by="type_lp_pre", ascending=False)
    type_lp_top20["size"] = type_lp_top20["typecount"] ** 0.5 * 2
    source = ColumnDataSource(type_lp_top20)

    lst_type = type_lp_top20["typename"].tolist()
    hover = HoverTool(tooltips=[("数据量", "@typecount"), ("烂片率", "@type_lp_pre")])

    output_file("templates/pic1.html")
    p = figure(
        x_range=lst_type,
        width=5500,
        height=800,
        title="不同电影题材的烂片比例",
        tools=[hover, "reset,xwheel_zoom,pan,crosshair,box_select"],
    )
    p.circle(
        x="typename",
        y="type_lp_pre",
        source=source,
        size="size",
        line_color="black",
        fill_color="red",
        fill_alpha=0.5,
    )
    script, div = components(p)
    return render_template("scoreBokeh.html", script=script, div=div)


@app.route("/lpRank250")
def lpRank250():
    m1 = m.sort_values(by=["DOUBAN_SCORE"], ascending=[True])
    m2 = m1.head(250)
    m2["index"] = range(len(m2))
    m2["index"] = m2["index"] + 1
    m2 = m2.values
    m2 = m2.tolist()
    # print(m2)
    return render_template("lpRank250.html", m2=m2)


@app.route("/hpRank250")
def hpRank250():
    m1 = m.sort_values(by=["DOUBAN_SCORE"], ascending=[False])
    m2 = m1.head(250)
    m2["index"] = range(len(m2))
    m2["index"] = m2["index"] + 1
    m2 = m2.values
    m2 = m2.tolist()
    # print(m2)
    return render_template("hpRank250.html", m2=m2)


@app.route("/Titanic")
def Titanic():
    return render_template("Titanic.html")


@app.route("/wordcloud")
def wordcloud():
    return render_template("wordcloud.html")


if __name__ == "__main__":
    app.run()
