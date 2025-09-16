import pandas as pd
import json
import matplotlib.pyplot as plt

with open("US_category_id.json", "r") as f:
    data = json.load(f)

json_us = pd.json_normalize(data["items"])

json_us = json_us[["id", "snippet.title"]]
json_us.rename(columns={"id": "category_id", "snippet.title": "category_name"}, inplace=True)


csv_us = pd.read_csv("USvideos.csv")

csv_us = csv_us.drop_duplicates()
csv_us = csv_us.fillna(0)
csv_us["publish_time"] = pd.to_datetime(csv_us["publish_time"])

csv_us["category_id"] = csv_us["category_id"].astype(str)
csv_us = csv_us.merge(json_us, on="category_id", how="left")
csv_us["publish_date"] = csv_us["publish_time"].dt.date
csv_us["publish_hour"] = csv_us["publish_time"].dt.hour
csv_us["publish_day"] = csv_us["publish_time"].dt.day_name()

# print(csv_us[["title", "category_name", "views"]].head())
# print(csv_us["category_name"].value_counts().head(10))

popular_categories = csv_us.groupby("category_name")["views"].mean().sort_values(ascending=False)
# print(popular_categories.head(10))

top_videos = csv_us.sort_values("views", ascending=False).head(10)
# print(top_videos[["title", "channel_title", "category_name", "views"]])

hourly_views = csv_us.groupby("publish_hour")["views"].mean()
# print(hourly_views)

csv_us["like_ratio"] = csv_us["likes"] / (csv_us["likes"] + csv_us["dislikes"] + 1)
csv_us["comment_ratio"] = csv_us["comment_count"] / (csv_us["views"] + 1)

# print(csv_us[["title", "like_ratio", "comment_ratio"]].head(10))


plt.figure(figsize=(10,6))
popular_categories.head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Categories by Avg Views")
plt.ylabel("Average Views")
plt.xticks(rotation=45, ha="right")

plt.figure(figsize=(10,6))
hourly_views.plot(kind="line", marker="o")
plt.title("Average Views by Publish Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Views")
plt.grid(True)

daily_views = csv_us.groupby("publish_day")["views"].mean().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

plt.figure(figsize=(10,6))
daily_views.plot(kind="bar", color="orange")
plt.title("Average Views by Day of Week")
plt.ylabel("Average Views")

top_channels = csv_us["channel_title"].value_counts().head(10)

plt.figure(figsize=(10,6))
top_channels.plot(kind="bar", color="green")
plt.title("Top 10 Channels with Most Trending Videos")
plt.ylabel("Number of Trending Videos")
plt.xticks(rotation=45, ha="right")

plt.figure(figsize=(10,6))
plt.scatter(csv_us["views"], csv_us["like_ratio"], alpha=0.3)
plt.title("Views vs Like Ratio")
plt.xlabel("Views")
plt.ylabel("Like Ratio")

plt.figure(figsize=(10,6))
plt.scatter(csv_us["views"], csv_us["comment_ratio"], alpha=0.3, color="red")
plt.title("Views vs Comment Ratio")
plt.xlabel("Views")
plt.ylabel("Comment Ratio")

# Show all plots at once
plt.show()
