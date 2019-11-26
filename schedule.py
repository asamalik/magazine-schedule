#!/usr/bin/python3

import tempfile, urllib.request, os, csv, datetime


def load_data(data_url):
    data = []

    with tempfile.TemporaryDirectory() as workdir:
        filename = os.path.join(workdir, "data.csv")

        urllib.request.urlretrieve(data_url, filename)

        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(dict(row))
    
    return data


def get_scheduled_posts(data):
    scheduled_posts = []

    for row in data:
        if row["due_date"]:
            date = datetime.date.fromisoformat(row["due_date"])
            if date >= datetime.date.today():
                scheduled_posts.append(row)
    
    scheduled_posts_sorted = sorted(scheduled_posts, key=lambda k: k["due_date"])

    return scheduled_posts_sorted

def main():
    data_url = "https://teams-api.fedoraproject.org/api/v1/userstories/csv?uuid=3498c3c483a64e0bb778461451a9055f"
    data = load_data(data_url)
    
    scheduled_posts = get_scheduled_posts(data)

    for post in scheduled_posts:
        date = datetime.date.fromisoformat(post["due_date"])
        print("{date}: #{id} {title}".format(
            date=date.strftime("%a %d %b %Y"),
            id=post["ref"],
            title=post["subject"]
        ))


if __name__ == "__main__":
    main()