# API Meta

API Meta - is API for getting site meta without webscraping. It can be used for SEO analysis or meta tag scraping.

Built with FastAPI and BS4

## How it works?

This api have just 1 route - `/info`. In args you should pass `url` argument and the magic begins:

```json

{
   "title":[
      {
         "name":"title",
         "content":"Medium – Where good ideas find you.",
         "property":null,
         "other":{
            "data-rh":"true"
         }
      }
   ],
   "opengraph":[
      {
         "name":null,
         "content":"Medium is an open platform where readers find dynamic thinking, and where expert and undiscovered voices can share their writing on any topic.",
         "property":"og:description",
         "other":{
            "data-rh":"true"
         }
      }...
   ],
   "apps":{
      "twitter":[
         {
            "name":"twitter:title",
            "content":"Medium – Where good ideas find you.",
            "property":null,
            "other":{
               "data-rh":"true"
            }
         }...
      ]
   },
   "tags":[
      {
         "name":null,
         "content":null,
         "property":null,
         "other":{
            "data-rh":"true",
            "charset":"utf-8"
         }
      }...
   ]
}
```

Now API Meta return can parse this meta tags to categories:
* Opengraph
* Twitter
* Title

Other tags, which not belong to any category you can see in `tags`

# PR

I will be very grateful if you send any PR, that will categorize tags. Check `tags.py` for more information.