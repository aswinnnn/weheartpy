### CHANGELOG
- `v0.2.4` - Fixed image saving functionality. This would have been a major error but was caught early through the issues page.
- `v0.2.3` - using `user-agent` has been made default. Fixed major bug in `search_entries` so you might wanna update to this version to use that correctly.
- `v0.2.2` - Big update, the library uses weheartit's natural API to bring `Entry` data.
-  - this features a whole new ton of information you can use from entries such as a views, hearts, tags, titles and creation dates.
-  - It also includes a `.creator` attribute which is a `User` object of the creator of the post.
-  - If you notice anything slow, its the API calls to weheartit.com. The IO time can be a pain if you have slow internet, nothing I can fix on my side.
- `v0.2.1` - Implement save feature, lets users save images locally.