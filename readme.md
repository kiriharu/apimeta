# API Meta

The API Meta service provides an API to get web-site meta by scraping it on your behalf. It could be used for SEO 
analysis or meta tag scraping.

Built with FastAPI and BeautifulSoup4.

## How does it work?

This API only has a single endpoint — `/info`. You have to access it with GET, providing `url` argument, and the magic 
would happen: 

```json
{
    "title": [
        {
            "name": "title",
            "content": "Medium – Where good ideas find you.",
            "property": null,
            "other": {
                "data-rh": "true"
            }
        }
    ],
    "opengraph": [
        {
            "name": null,
            "content": "Medium is an open platform where readers find dynamic thinking, and where expert and undiscovered voices can share their writing on any topic.",
            "property": "og:description",
            "other": {
                "data-rh": "true"
            }
        }, ...
    ],
    "apps": {
        "twitter": [
            {
                "name": "twitter:title",
                "content": "Medium – Where good ideas find you.",
                "property": null,
                "other": {
                    "data-rh": "true"
                }
            }, ...
        ]
    },
    "tags": [
        {
            "name": null,
            "content": null,
            "property": null,
            "other": {
                "data-rh": "true",
                "charset": "utf-8"
            }
        }, ...
    ]
}
```

Currently API Meta can return information on page title, [Open Graph](https://ogp.me/) tags, and [Twitter card](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/markup) markup.

The rest of the tags that API Meta cannot categorize at the moment go into `tags` collection.

## PR

I'd be very grateful for any PRs with additional tag categories support. Please get started [here](https://github.com/kiriharu/apimeta/blob/main/apimeta/tags.py). 
